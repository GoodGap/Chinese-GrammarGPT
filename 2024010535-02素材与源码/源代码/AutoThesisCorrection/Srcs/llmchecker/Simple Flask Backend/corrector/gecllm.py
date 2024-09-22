from tqdm import tqdm
from transformers import AutoConfig, AutoModel, AutoTokenizer
import os
import pandas as pd
import numpy as np
import datasets
import transformers
import torch
import torch.nn as nn
import warnings
import pickle
import pynvml
from resp2edit import resp2edit
warnings.filterwarnings("ignore")
class LLMCorrector():
    def __init__(self,model=None,tokenizer=None):
        """

        :param model:模型对象
        :param tokenizer: 模型分词器对象
        """
        pynvml.nvmlInit()
        self.model=model if model!=None else self.__ModelInitialize('/root/workspace/mymodel','/root/workspace/ChatGLM2-6B-main/ptuning/output/CGEC-chatglm2-6b-pt-128-2e-2/checkpoint-3000/pytorch_model.bin')#如果没有指定模型，此函数重新部署模型，在这里修改参数。
        self.tokenizer=tokenizer if tokenizer!=None else self.__TokenizerInitialize('mymodel')#如果没有加载分词器，则重新加载分词器，路径在此处修改。
        self.his=[("因为污染也很高，我们要回收垃圾。为什么?塑料、电池、垃圾是我们做的东西。 -> ","因为污染很严重，所以我们要回收垃圾。为什么?因为塑料、电池等垃圾是我们人类造出来的东西。"),
                  ("最近吸烟者率是越来越多，而且吸烟者的年龄层是越来越少。这些问题是现在最重要的事。 -> ","最近吸烟率是越来越高，而且吸烟者的年龄层是越来越低。这些问题是现在最重要的事。"),
                  ("不仅他学习某种习惯，他们性格也开始养成。 -> ","他们不仅开始学习某种习惯，他们的性格也开始形成。"),
                  ("这世界上是很残酷的。 -> ","这世界是很残酷的。"),
                  ("每一刻都用得无可挑剔。 -> ","每一刻都用得无可挑剔。")]#人为构造的模型的历史记录，不用更改

    def __TokenizerInitialize(self,model_params_path):
        """

        :param model_params_path:模型文件路径，里面也包含了分词器
        :return: 一个重新部署的分词器对象
        """
        # 载入Tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_params_path, trust_remote_code=True)
        return tokenizer

    def __ModelInitialize(self,model_params_path,finetune_params_path):
        """

        :param model_params_path:本地下载的模型参数地址
        :param finetune_params_path: 微调参数地址，需要精确到文件名
        :return: 重新部署到GPU的模型对象
        """
        # 检查是否有GPU以及GPU是否有足够内存加载模型。
        available_gpu_exists=False
        if torch.cuda.is_available():
            device_count=torch.cuda.device_count()
            for i in range(device_count):# 这里遍历所有的GPU找能用的，实验室配给我们5，6号卡可能要改成(5,7)
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)#这些都是模板
                if(meminfo.free/1024**3>=13):    #chatglm-6b占用显存11-12G，这里找至少13G可用显存的GPU，要是资源实在紧张可以把这个改成'>=12'.
                    print(f'Device {i} is available!')
                    os.environ["CUDA_VISIBLE_DEVICES"] = str(i)
                    available_gpu_exists=True
                    break
            if available_gpu_exists==False:
                raise MemoryError('No GPU available to load model.Please check whether the model is already loaded.')
        else:
            raise ModuleNotFoundError('No GPU found on this device,please check if you are running this program on GPU.')

        # 加载chatglm2-6b模型
        config = AutoConfig.from_pretrained(model_params_path, trust_remote_code=True, pre_seq_len=128)
        #config是用来配置一部分模型参数的，不用改动。
        model = AutoModel.from_pretrained(model_params_path, config=config, trust_remote_code=True)
        #加载微调参数文件
        prefix_state_dict = torch.load(
            finetune_params_path)#根据实际情况修改这一行为微调参数文件路径，要精确到.bin文件
        new_prefix_state_dict = {}
        for k, v in prefix_state_dict.items():
            if k.startswith("transformer.prefix_encoder."):
                new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
        model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)

        # 量化操作，减少模型的大小和计算量，不影响性能。
        model = model.quantize(4)  # 参数映射为8位整数，4bit的量化精度，也可以设定为8.
        model = model.half().cuda()
        model.transformer.prefix_encoder.float()
        # 设置为评估模式，推理速度更快。
        model = model.eval()

        print('Successfully built model ChatGLM2-6B!')
        return model

    def __get_prompt(self,text):
        """

        :param text:待纠错的句子
        :return: 适合模型识别的提示词，跟历史his一起使用
        """
        prompt = """中文语法纠错任务：将一段中文句子进行修正，如果句子没有明显语病则返回原句。

        下面是一些范例:

        学生大概做飞机去北京。 -> 学生大概坐飞机去北京。\n
        我觉得他很大胆，他不去外国。他觉得如果要改转变中国，所以就要从中国做的研究。  -> 我觉得他很大胆，他不去外国。他觉得如果要改变中国，就要在中国做研究。\n
        吸烟者反对这样的措施。 -> 吸烟者反对这样的措施。\n

        请对下述句子进行修正。返回你修改后的句子，无需其它说明和解释。

        xxxxxx ->

        """
        return prompt.replace('xxxxxx',text)

    def GEC_Classification(self):
        """
        :return: 暂时还没写。
        """
        pass

    def GEC_Correction(self,text):
        """
        :param text：输入模型的句子。
        :return:修改后返回的编辑序列列表。
        """
        prompt = self.__get_prompt(text)
        response, _ = self.model.chat(self.tokenizer, prompt, history=self.his)
        # edits=self.__Resp_to_Edit(response,text)
        return response

    def __Resp_to_Edit(self,response,source,max_unchanged_words = 0):
        """
        :param response:    模型返回的改句。
        :param source:  输入模型的句子。
        :max_unchanged_words:   编辑粒度，见函数原型。
        :return:   通过对比字符串得到的编辑序列。
        """
        return resp2edit(source,response,max_unchanged_words)

