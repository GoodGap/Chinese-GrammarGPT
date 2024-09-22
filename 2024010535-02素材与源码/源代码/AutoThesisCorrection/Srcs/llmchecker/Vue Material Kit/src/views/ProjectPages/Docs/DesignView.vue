<script setup lang="ts">
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import GLMTraining from "@/assets/img/project/GLM预训练原理.png";
import Transformer from "@/assets/img/project/transformer.png";
</script>
<template>
  <BaseLayout title="软件设计" :breadcrumb="[{ label: '文档', route: '#' }, { label: '软件设计' }]">
    <div class="border-radius-xl overflow-hidden shadow-lg mb-7 p-4 text-black">
      <div class='typora-export-content'>
        <div id='write' class=''>
          <h1 id='大语言模型下的文本智能纠错研究'><span>大语言模型下的文本智能纠错研究</span></h1>
          <h2 id='数据结构与算法'><span>数据结构与算法</span></h2>
          <h3 id='一数据格式规范'><span>一、数据格式规范</span></h3>
          <p><span>因为这是一个以大语言模型为核心的工程项目，所以需要在数据集的构建、请求的构建以及后端数据的收集上拥有符合模型要求的格式。</span></p>
          <h4 id='1数据集格式规范'><span>1.数据集格式规范</span></h4>
          <h5 id='a人工处理阶段'><span>a.人工处理阶段</span></h5>
          <p><span>在收集数据的初级阶段，需要自动化地或者人工地构建原始数据集和调整数据。为此，我们制定了基本的数据规范：</span></p>
          <p><span>使用csv文件格式存储原始数据。这种存储方式的优点是能够快速批量读取和处理数据，并且能够转化为适合统一修改格式的Python数据结构。我们为最新一轮模型微调所使用的csv格式如下表所示。</span>
          </p>
          <figure class='table-figure'>
            <table>
              <thead>
                <tr>
                  <th><span>id</span></th>
                  <th><span>病句</span></th>
                  <th><span>错误类型</span></th>
                  <th><span>正确句子</span></th>
                  <th><span>修改理由</span></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><span>1</span></td>
                  <td><span>由于加强了$\cdots$</span></td>
                  <td><span>搭配不当</span></td>
                  <td><span>由于加强了$\cdots$</span></td>
                  <td><span>“生产量”不能作为$\cdots$</span></td>
                </tr>
                <tr>
                  <td><span>2</span></td>
                  <td><span>以损人利己手段$\cdots$</span></td>
                  <td><span>结构混乱</span></td>
                  <td><span>以损人利己的手段$\cdots$</span></td>
                  <td><span>病句中$\cdots$</span></td>
                </tr>
                <tr>
                  <td><span>3</span></td>
                  <td><span>$\cdots$</span></td>
                  <td>&nbsp;</td>
                  <td>&nbsp;</td>
                  <td>&nbsp;</td>
                </tr>
              </tbody>
            </table>
          </figure>
          <h5 id='b机器处理阶段'><span>b.机器处理阶段</span></h5>
          <p><span>在数据收集完毕之后，我们需要将csv文件转换为适合机器处理的python数据格式。我们参考了ChatGLM2-6B的官方微调手册，将微调数据集中每一条数据处理成如下的字典格式：</span>
            <span> </span>
          </p>
          <pre class="md-fences md-end-block ty-contain-cm modeLoaded" spellcheck="false"
            lang="python"><div class="CodeMirror cm-s-inner cm-s-null-scroll CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 9.5px; left: 8px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: currentcolor;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: currentcolor;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation"><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">{</span></pre>
      </div>
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">'Prompt'</span>:<span class="cm-string">f'prompt_template,</span>{<span class="cm-variable">error_sentence</span>}<span class="cm-string">'</span>,</span></pre>
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">'Response'</span>:<span class="cm-string">f'</span>{<span class="cm-variable">correct_sentence</span>}<span class="cm-string">,</span>{<span class="cm-variable">error_type</span>}<span class="cm-string"> because </span>{<span class="cm-variable">reason</span>}<span class="cm-string">.'</span></span></pre>
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;">}</span></pre>
    </div>
  </div>
  </div>
  </div>
  </div>
  <div
    style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 92px;">
  </div>
  <div class="CodeMirror-gutters" style="display: none; height: 92px;"></div>
  </div>
  </div>
  </pre>
    <p><span>其中，</span><code>prompt_template</code><span>是适合的提示词模板，其余信息取自我们在数据集中收集到的内容。</span></p>
    <p><span>为了提高微调数据集的构建效率，我们还构建了另一个json数据结构来存放csv文件的读取结果。</span></p>
    <pre class="md-fences md-end-block ty-contain-cm modeLoaded" spellcheck="false"
      lang="python"><div class="CodeMirror cm-s-inner cm-s-null-scroll CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 9.5px; left: 8px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: currentcolor;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: currentcolor;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre>
  </div>
  <div class="CodeMirror-measure"></div>
  <div style="position: relative; z-index: 1;"></div>
  <div class="CodeMirror-code" role="presentation" style="">
    <div class="CodeMirror-activeline" style="position: relative;">
      <div class="CodeMirror-activeline-background CodeMirror-linebackground"></div>
      <div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div>
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;">{</span></pre>
    </div>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">'id'</span>:<span class="cm-builtin">id</span>,</span></pre>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">'error_sentence'</span>:<span class="cm-string">'错误句子'</span>,</span></pre>
    </div>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">'error_type'</span>:<span class="cm-string">'错误类型'</span>,</span></pre>
    </div>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">'correct_sentence'</span>:<span class="cm-string">'正确句子'</span>,</span></pre>
    </div>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-string">'reason'</span>:<span class="cm-string">'修改理由'</span></span></pre>
    </div>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;">}</span></pre>
  </div>
  </div>
  </div>
  </div>
  </div>
  <div
    style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 161px;">
  </div>
  <div class="CodeMirror-gutters" style="display: none; height: 161px;"></div>
  </div>
  </div>
  </pre>
    <h5 id='c提示词模板'><span>c.提示词模板</span></h5>
    <p><span>我们就ChatGLM2-6B模型特性，开展了一系列提示词工程实验，最后确定了能够让模型稳定输出的提示词模板。</span></p>
    <pre class="md-fences md-end-block ty-contain-cm modeLoaded" spellcheck="false" lang="python"
      style="break-inside: unset;"><div class="CodeMirror cm-s-inner cm-s-null-scroll CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 9.5px; left: 8px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: currentcolor;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: currentcolor;"><div class="CodeMirror-measure"><pre>x</pre>
  </div>
  <div class="CodeMirror-measure"></div>
  <div style="position: relative; z-index: 1;"></div>
  <div class="CodeMirror-code" role="presentation" style="">
    <div class="CodeMirror-activeline" style="position: relative;">
      <div class="CodeMirror-activeline-background CodeMirror-linebackground"></div>
      <div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div>
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">prompt</span> <span class="cm-operator">=</span> <span class="cm-string">"""中文语法纠错任务：将一段中文句子进行修正，如果句子没有明显语病则返回原句。</span></span></pre>
    </div>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
    </div>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">例如:</span></span></pre>
    </div>
    <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">学生大概做飞机去北京。 -&gt; 学生大概坐飞机去北京。\n</span></span></pre>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">吸烟者反对这样的措施。 -&gt; 吸烟者反对这样的措施。\n</span></span></pre>
    <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">请对下述句子进行修正。返回你修改后的句子，无需其它说明和解释。</span></span></pre>
    <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">xxxxxx -&gt;</span></span></pre>
    </div>
    <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">"""</span></span></pre>
    <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">get_prompt</span>(<span class="cm-variable">text</span>):</span></pre>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;">&nbsp; &nbsp; <span class="cm-keyword">return</span> <span class="cm-variable">prompt</span>.<span class="cm-property">replace</span>(<span class="cm-string">'xxxxxx'</span>,<span class="cm-variable">text</span>)</span></pre>
  </div>
  </div>
  </div>
  </div>
  </div>
  <div
    style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 345px;">
  </div>
  <div class="CodeMirror-gutters" style="display: none; height: 345px;"></div>
  </div>
  </div>
  </pre>
    <p><span>在微调阶段，为了提升模型推理的能力，我们构建了专用于微调的提示词模板：</span></p>
    <pre class="md-fences md-end-block ty-contain-cm modeLoaded" spellcheck="false"
      lang="python"><div class="CodeMirror cm-s-inner cm-s-null-scroll CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 9.5px; left: 8px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: currentcolor;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: currentcolor;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre>
  </div>
  <div class="CodeMirror-measure"></div>
  <div style="position: relative; z-index: 1;"></div>
  <div class="CodeMirror-code" role="presentation">
    <div class="CodeMirror-activeline" style="position: relative;">
      <div class="CodeMirror-activeline-background CodeMirror-linebackground"></div>
      <div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div>
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">prompt</span><span class="cm-operator">=</span><span class="cm-string">f"假设你是一个擅长中文语法纠错任务的语言学家，\</span></span></pre>
    </div>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">下面我将提供给你一个病句，请你基于中文语言规范和习惯，对这句话进行改正，\</span></span></pre>
    </div>
    <div class="" style="position: relative;">
      <pre class=" CodeMirror-line "
        role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">并且说明原因。\n</span>{<span class="cm-variable">error_sentence</span>}<span class="cm-string">"</span></span></pre>
    </div>
  </div>
  </div>
  </div>
  </div>
  </div>
  <div
    style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 69px;">
  </div>
  <div class="CodeMirror-gutters" style="display: none; height: 69px;"></div>
  </div>
  </div>
  </pre>
    <p><span>这样我们能够人为地构建模型的预期回答格式标准，从而让模型在处理这类问题时更加敏锐。</span></p>
    <h3 id='二算法分析'><span>二、算法分析</span></h3>
    <h4 id='1模型算法'><span>1.模型算法</span></h4>
    <p><span>本项目所使用的模型是国产开源大模型ChatGLM2-6B.该模型是使用transformer编解码器协同控制训练得到的，项目在部署和调用模型的过程中，主要是采用GLM的前向传播算法。</span></p>
    <p><span>2022年，Zhengxiao Du
        等提出了自回归空白填充预训练的通用语言模型(GLM)，该模型通过添加二维位置编码和允许任意顺序预测跨度，改进了空白填充预训练，从而在自然语言理解、条件生成和无条件生成的广泛任务中，在相同模型大小和数据的情况下优于 BERT、T5
        和 GPT 等大模型，并且在语句纠错方面表现出很大潜力。GLM 预训练阶段的具体运行机制可参考下图。</span>
      <img :src="GLMTraining" referrerpolicy="no-referrer">
      <span>GLM基于自回归的空白填充进行训练。模型通过训练来重构跨度，并使用双向和单向的注意力机制将输入分为掩码token和非掩码token。非掩码token可以互相看到（attention），而掩码的token不能看到后面的。在训练过程中，模型需要预测被mask的token，以此为基础进行参数更新。此外，位置编码也使用了2维的编码技术，来表示跨间和跨内信息。这样，GLM框架可以适配NLU和生成的任务。</span>
    </p>
    <p><span>我们使用的是预训练模型，在调用的时候直接运用模型推理算法。这个推理算法本质是多头注意力机制的一种实现方式，GLM团队在模型推理过程中研发了Multi-Query
        Attention（MQA）技术，这是对多头注意力机制Multi head Attention（MHA）的一种优化实现，它通过同时处理多个查询并利用注意力机制，可以提高模型的性能和用户体验。</span>
      <span>在基于注意力机制的推理过程中，模型会基于提供的查询请求字段，通过transformer架构计算请求中最值得注意的关键字词，并且基于此预测出接下来最可能生成的词语。如此递归循环往复，实现自回归的逐字句生成回复。下图展现了利用transformer架构做模型推理的过程。</span>
      <img :src="Transformer" referrerpolicy="no-referrer">
    </p>
    <h4 id='2数据处理和微调算法'><span>2.数据处理和微调算法</span></h4>
    <pre class="md-fences md-end-block ty-contain-cm modeLoaded" spellcheck="false"
      lang=""><div class="CodeMirror cm-s-inner cm-s-null-scroll CodeMirror-wrap" lang=""><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 9.5px; left: 8px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: currentcolor;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: currentcolor;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">data = read(dataset)</span></pre>
  </div>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;">originals = []</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;">for origin in data:</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;  prompt = prompt_template+origin</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;  response = model.chat(prompt)</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;  corrections.append(response)</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;">write(corrections, outputs)</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;">for correction in corrections:</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;  content = extract_content(correction)</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;  print(content) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></pre>
  </div>
  </div>
  </div>
  </div>
  </div>
  <div
    style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 230px;">
  </div>
  <div class="CodeMirror-gutters" style="display: none; height: 230px;"></div>
  </div>
  </div>
  </pre>
    <h4 id='3全参数微调算法'><span>3.全参数微调算法</span></h4>
    <pre class="md-fences md-end-block ty-contain-cm modeLoaded" spellcheck="false" lang="python"
      style="break-inside: unset;"><div class="CodeMirror cm-s-inner cm-s-null-scroll CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 9.5px; left: 8px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: currentcolor;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: currentcolor;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">transformers</span> <span class="cm-keyword">import</span> <span class="cm-variable">GPT2LMHeadModel</span>, <span class="cm-variable">GPT2Tokenizer</span></span></pre>
  </div>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">torch</span>.<span class="cm-property">utils</span>.<span class="cm-property">data</span> <span class="cm-keyword">import</span> <span class="cm-variable">Dataset</span>, <span class="cm-variable">DataLoader</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">torch</span></span></pre>
  <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 定义自定义数据集类</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">class</span> <span class="cm-def">ChatDataset</span>(<span class="cm-variable">Dataset</span>):</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-keyword">def</span> <span class="cm-def">__init__</span>(<span class="cm-variable-2">self</span>, <span class="cm-variable">data</span>)</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-keyword">def</span> <span class="cm-def">__len__</span>(<span class="cm-variable-2">self</span>)</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-keyword">def</span> <span class="cm-def">__getitem__</span>(<span class="cm-variable-2">self</span>, <span class="cm-variable">idx</span>)<span class="cm-comment">#read batch</span></span></pre>
  <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 加载数据并创建数据加载器</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">train_data</span> <span class="cm-operator">=</span> [<span class="cm-operator">...</span>] &nbsp;<span class="cm-comment"># 自定义的训练数据集，包含输入文本和目标文本</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">dataset</span> <span class="cm-operator">=</span> <span class="cm-variable">ChatDataset</span>(<span class="cm-variable">train_data</span>)</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">train_loader</span> <span class="cm-operator">=</span> <span class="cm-variable">DataLoader</span>(<span class="cm-variable">dataset</span>)</span></pre>
  <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 加载预训练的 ChatGPT-LM-6B 模型</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">model</span> <span class="cm-operator">=</span> <span class="cm-variable">ChatGLM2</span><span class="cm-operator">-</span><span class="cm-number">6</span><span class="cm-variable">B</span>.<span class="cm-property">from_pretrained</span>()</span></pre>
  <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 开始训练</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">model</span>.<span class="cm-property">train</span>()</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">for</span> <span class="cm-variable">epoch</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">num_epochs</span>):</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">compute</span> <span class="cm-variable">loss</span>;</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">compute</span> <span class="cm-variable">optimizer</span>;</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">loss</span>.<span class="cm-property">backward</span>()</span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-variable">optimizer</span>.<span class="cm-property">step</span>()</span></pre>
  <pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="" cm-zwsp="">
</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 保存微调后的模型</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">model</span>.<span class="cm-property">save_pretrained</span>(<span class="cm-string">"path/to/save/model"</span>)</span></pre>
  </div>
  </div>
  </div>
  </div>
  </div>
  <div
    style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 644px;">
  </div>
  <div class="CodeMirror-gutters" style="display: none; height: 644px;"></div>
  </div>
  </div>
  </pre>
    <p>&nbsp;</p>
    <h2 id='前后端'><span>前后端</span></h2>
    <h3 id='数据管理说明'><span>数据管理说明</span></h3>
    <p><span>用户数据使用 MySQL 数据库进行管理，建表语句如下。</span></p>
    <pre class="md-fences md-end-block ty-contain-cm modeLoaded md-focus" spellcheck="false"
      lang="sql"><div class="CodeMirror cm-s-inner cm-s-null-scroll CodeMirror-wrap CodeMirror-focused" lang="sql"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 170.5px; left: 336.373413px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: currentcolor;"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: currentcolor;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div class="" style="position: relative;"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">CREATE</span> <span class="cm-keyword">TABLE</span> <span class="cm-variable-2">`userdata`</span> <span class="cm-bracket">(</span></span></pre>
  </div>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-variable-2">`id`</span> <span class="cm-type">int</span><span class="cm-bracket">(</span><span class="cm-number">11</span><span class="cm-bracket">)</span> <span class="cm-keyword">NOT</span> <span class="cm-atom">NULL</span> <span class="cm-keyword">AUTO_INCREMENT</span><span class="cm-punctuation">,</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-variable-2">`username`</span> <span class="cm-type">varchar</span><span class="cm-bracket">(</span><span class="cm-number">20</span><span class="cm-bracket">)</span> <span class="cm-keyword">NOT</span> <span class="cm-atom">NULL</span><span class="cm-punctuation">,</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-variable-2">`password`</span> <span class="cm-type">varchar</span><span class="cm-bracket">(</span><span class="cm-number">255</span><span class="cm-bracket">)</span> <span class="cm-keyword">NOT</span> <span class="cm-atom">NULL</span><span class="cm-punctuation">,</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-variable-2">`role`</span> <span class="cm-type">tinyint</span><span class="cm-bracket">(</span><span class="cm-number">1</span><span class="cm-bracket">)</span> <span class="cm-keyword">NOT</span> <span class="cm-atom">NULL</span><span class="cm-punctuation">,</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-variable-2">`telephone`</span> <span class="cm-type">varchar</span><span class="cm-bracket">(</span><span class="cm-number">255</span><span class="cm-bracket">)</span> <span class="cm-keyword">NOT</span> <span class="cm-atom">NULL</span><span class="cm-punctuation">,</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-variable-2">`email`</span> <span class="cm-type">varchar</span><span class="cm-bracket">(</span><span class="cm-number">255</span><span class="cm-bracket">)</span> <span class="cm-keyword">NOT</span> <span class="cm-atom">NULL</span><span class="cm-punctuation">,</span></span></pre>
  <div class="CodeMirror-activeline" style="position: relative;">
    <div class="CodeMirror-activeline-background CodeMirror-linebackground"></div>
    <div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div>
    <pre class=" CodeMirror-line "
      role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-variable-2">`address`</span> <span class="cm-type">varchar</span><span class="cm-bracket">(</span><span class="cm-number">255</span><span class="cm-bracket">)</span> <span class="cm-keyword">DEFAULT</span> <span class="cm-atom">NULL</span><span class="cm-punctuation">,</span></span></pre>
  </div>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-keyword">PRIMARY</span> <span class="cm-keyword">KEY</span> <span class="cm-bracket">(</span><span class="cm-variable-2">`id`</span><span class="cm-bracket">)</span><span class="cm-punctuation">,</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-keyword">UNIQUE</span> <span class="cm-keyword">KEY</span> <span class="cm-variable-2">`telephone`</span> <span class="cm-bracket">(</span><span class="cm-variable-2">`telephone`</span><span class="cm-bracket">)</span><span class="cm-punctuation">,</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp;<span class="cm-keyword">UNIQUE</span> <span class="cm-keyword">KEY</span> <span class="cm-variable-2">`email`</span> <span class="cm-bracket">(</span><span class="cm-variable-2">`email`</span><span class="cm-bracket">)</span></span></pre>
  <pre class=" CodeMirror-line "
    role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-bracket">)</span> <span class="cm-keyword">ENGINE</span><span class="cm-operator">=</span><span class="cm-keyword">InnoDB</span> <span class="cm-keyword">DEFAULT</span> <span class="cm-builtin">CHARSET</span><span class="cm-operator">=</span>utf8<span class="cm-punctuation">;</span></span></pre>
  </div>
  </div>
  </div>
  </div>
  </div>
  <div
    style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 276px;">
  </div>
  <div class="CodeMirror-gutters" style="display: none; height: 276px;"></div>
  </div>
  </div>
  </pre>
    <p><span>用户登录验证的 token 等信息使用 Redis 数据库进行管理。</span></p>
    <p><span>用户文件采用文件系统进行管理，根据用户 id 分别位于不同目录下。</span></p>
    </div>
    </div>
    </div>
  </BaseLayout>
</template>

<style scoped>
html {
  overflow-x: initial !important;
}

:root {
  --bg-color: #ffffff;
  --text-color: #333333;
  --select-text-bg-color: #B5D6FC;
  --select-text-font-color: auto;
  --monospace: "Lucida Console", Consolas, "Courier", monospace;
  --title-bar-height: 20px;
}

.mac-os-11 {
  --title-bar-height: 28px;
}

html {
  font-size: 14px;
  background-color: var(--bg-color);
  color: var(--text-color);
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}

h1,
h2,
h3,
h4,
h5 {
  white-space: pre-wrap;
}

body {
  margin: 0px;
  padding: 0px;
  height: auto;
  inset: 0px;
  font-size: 1rem;
  line-height: 1.428571;
  overflow-x: hidden;
  background: inherit;
}

iframe {
  margin: auto;
}

a.url {
  word-break: break-all;
}

a:active,
a:hover {
  outline: 0px;
}

.in-text-selection,
::selection {
  text-shadow: none;
  background: var(--select-text-bg-color);
  color: var(--select-text-font-color);
}

#write {
  margin: 0px auto;
  height: auto;
  width: inherit;
  word-break: normal;
  overflow-wrap: break-word;
  position: relative;
  white-space: normal;
  overflow-x: visible;
  padding-top: 36px;
}

#write.first-line-indent p {
  text-indent: 2em;
}

#write.first-line-indent li p,
#write.first-line-indent p * {
  text-indent: 0px;
}

#write.first-line-indent li {
  margin-left: 2em;
}

.for-image #write {
  padding-left: 8px;
  padding-right: 8px;
}

body.typora-export {
  padding-left: 30px;
  padding-right: 30px;
}

.typora-export .footnote-line,
.typora-export li,
.typora-export p {
  white-space: pre-wrap;
}

.typora-export .task-list-item input {
  pointer-events: none;
}

@media screen and (max-width: 500px) {
  body.typora-export {
    padding-left: 0px;
    padding-right: 0px;
  }

  #write {
    padding-left: 20px;
    padding-right: 20px;
  }
}

#write li>figure:last-child {
  margin-bottom: 0.5rem;
}

#write ol,
#write ul {
  position: relative;
}

img {
  max-width: 100%;
  vertical-align: middle;
  image-orientation: from-image;
}

button,
input,
select,
textarea {
  color: inherit;
  font-style: inherit;
  font-variant-caps: inherit;
  font-weight: inherit;
  font-stretch: inherit;
  font-size: inherit;
  line-height: inherit;
  font-family: inherit;
  font-size-adjust: inherit;
  font-kerning: inherit;
  font-variant-alternates: inherit;
  font-variant-ligatures: inherit;
  font-variant-numeric: inherit;
  font-variant-east-asian: inherit;
  font-variant-position: inherit;
  font-feature-settings: inherit;
  font-optical-sizing: inherit;
  font-variation-settings: inherit;
}

input[type="checkbox"],
input[type="radio"] {
  line-height: normal;
  padding: 0px;
}

*,
::after,
::before {
  box-sizing: border-box;
}

#write h1,
#write h2,
#write h3,
#write h4,
#write h5,
#write h6,
#write p,
#write pre {
  width: inherit;
}

#write h1,
#write h2,
#write h3,
#write h4,
#write h5,
#write h6,
#write p {
  position: relative;
}

p {
  line-height: inherit;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  break-after: avoid-page;
  break-inside: avoid;
  orphans: 4;
}

p {
  orphans: 4;
}

h1 {
  font-size: 2rem;
}

h2 {
  font-size: 1.8rem;
}

h3 {
  font-size: 1.6rem;
}

h4 {
  font-size: 1.4rem;
}

h5 {
  font-size: 1.2rem;
}

h6 {
  font-size: 1rem;
}

.md-math-block,
.md-rawblock,
h1,
h2,
h3,
h4,
h5,
h6,
p {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.hidden {
  display: none;
}

.md-blockmeta {
  color: rgb(204, 204, 204);
  font-weight: 700;
  font-style: italic;
}

a {
  cursor: pointer;
}

sup.md-footnote {
  padding: 2px 4px;
  background-color: rgba(238, 238, 238, 0.7);
  color: rgb(85, 85, 85);
  border-radius: 4px;
  cursor: pointer;
}

sup.md-footnote a,
sup.md-footnote a:hover {
  color: inherit;
  text-transform: inherit;
  text-decoration: inherit;
}

#write input[type="checkbox"] {
  cursor: pointer;
  width: inherit;
  height: inherit;
}

figure {
  overflow-x: auto;
  margin: 1.2em 0px;
  max-width: calc(100% + 16px);
  padding: 0px;
}

figure>table {
  margin: 0px;
}

thead,
tr {
  break-inside: avoid;
  break-after: auto;
}

thead {
  display: table-header-group;
}

table {
  border-collapse: collapse;
  border-spacing: 0px;
  width: 100%;
  overflow: auto;
  break-inside: auto;
  text-align: left;
}

table.md-table td {
  min-width: 32px;
}

.CodeMirror-gutters {
  border-right-width: 0px;
  border-right-style: none;
  border-right-color: currentcolor;
  background-color: inherit;
}

.CodeMirror-linenumber {
  -webkit-user-select: none;
}

.CodeMirror {
  text-align: left;
}

.CodeMirror-placeholder {
  opacity: 0.3;
}

.CodeMirror pre {
  padding: 0px 4px;
}

.CodeMirror-lines {
  padding: 0px;
}

div.hr:focus {
  cursor: none;
}

#write pre {
  white-space: pre-wrap;
}

#write.fences-no-line-wrapping pre {
  white-space: pre;
}

#write pre.ty-contain-cm {
  white-space: normal;
}

.CodeMirror-gutters {
  margin-right: 4px;
}

.md-fences {
  font-size: 0.9rem;
  display: block;
  break-inside: avoid;
  text-align: left;
  overflow: visible;
  white-space: pre;
  background: inherit;
  position: relative !important;
}

.md-fences-adv-panel {
  width: 100%;
  margin-top: 10px;
  text-align: center;
  padding-top: 0px;
  padding-bottom: 8px;
  overflow-x: auto;
}

#write .md-fences.mock-cm {
  white-space: pre-wrap;
}

.md-fences.md-fences-with-lineno {
  padding-left: 0px;
}

#write.fences-no-line-wrapping .md-fences.mock-cm {
  white-space: pre;
  overflow-x: auto;
}

.md-fences.mock-cm.md-fences-with-lineno {
  padding-left: 8px;
}

.CodeMirror-line,
twitterwidget {
  break-inside: avoid;
}

svg {
  break-inside: avoid;
}

.footnotes {
  opacity: 0.8;
  font-size: 0.9rem;
  margin-top: 1em;
  margin-bottom: 1em;
}

.footnotes+.footnotes {
  margin-top: 0px;
}

.md-reset {
  margin: 0px;
  padding: 0px;
  border: 0px;
  outline: 0px;
  vertical-align: top;
  background: 0px 0px;
  text-decoration: none;
  text-shadow: none;
  float: none;
  position: static;
  width: auto;
  height: auto;
  white-space: nowrap;
  cursor: inherit;
  line-height: normal;
  font-weight: 400;
  text-align: left;
  box-sizing: content-box;
  direction: ltr;
}

li div {
  padding-top: 0px;
}

blockquote {
  margin: 1rem 0px;
}

li .mathjax-block,
li p {
  margin: 0.5rem 0px;
}

li blockquote {
  margin: 1rem 0px;
}

li {
  margin: 0px;
  position: relative;
}

blockquote> :last-child {
  margin-bottom: 0px;
}

blockquote> :first-child,
li> :first-child {
  margin-top: 0px;
}

.footnotes-area {
  color: rgb(136, 136, 136);
  margin-top: 0.714rem;
  padding-bottom: 0.143rem;
  white-space: normal;
}

#write .footnote-line {
  white-space: pre-wrap;
}

@media print {

  body,
  html {
    border: 1px solid transparent;
    height: 99%;
    break-after: avoid;
    break-before: avoid;
    font-variant-ligatures: no-common-ligatures;
  }

  #write {
    margin-top: 0px;
    border-color: transparent !important;
    padding-top: 0px !important;
    padding-bottom: 0px !important;
  }

  .typora-export * {
    print-color-adjust: exact;
  }

  .typora-export #write {
    break-after: avoid;
  }

  .typora-export #write::after {
    height: 0px;
  }

  .is-mac table {
    break-inside: avoid;
  }

  #write>p:nth-child(1) {
    margin-top: 0px;
  }

  .typora-export-show-outline .typora-export-sidebar {
    display: none;
  }

  figure {
    overflow-x: visible;
  }
}

.footnote-line {
  margin-top: 0.714em;
  font-size: 0.7em;
}

a img,
img a {
  cursor: pointer;
}

pre.md-meta-block {
  font-size: 0.8rem;
  min-height: 0.8rem;
  white-space: pre-wrap;
  background: rgb(204, 204, 204);
  display: block;
  overflow-x: hidden;
}

p>.md-image:only-child:not(.md-img-error) img,
p>img:only-child {
  display: block;
  margin: auto;
}

#write.first-line-indent p>.md-image:only-child:not(.md-img-error) img {
  left: -2em;
  position: relative;
}

p>.md-image:only-child {
  display: inline-block;
  width: 100%;
}

#write .MathJax_Display {
  margin: 0.8em 0px 0px;
}

.md-math-block {
  width: 100%;
}

.md-math-block:not(:empty)::after {
  display: none;
}

.MathJax_ref {
  fill: currentcolor;
}

[contenteditable="true"]:active,
[contenteditable="true"]:focus,
[contenteditable="false"]:active,
[contenteditable="false"]:focus {
  outline: 0px;
  box-shadow: none;
}

.md-task-list-item {
  position: relative;
  list-style-type: none;
}

.task-list-item.md-task-list-item {
  padding-left: 0px;
}

.md-task-list-item>input {
  position: absolute;
  top: 0px;
  left: 0px;
  margin-left: -1.2em;
  margin-top: calc(1em - 10px);
  border: medium;
}

.math {
  font-size: 1rem;
}

.md-toc {
  min-height: 3.58rem;
  position: relative;
  font-size: 0.9rem;
  border-radius: 10px;
}

.md-toc-content {
  position: relative;
  margin-left: 0px;
}

.md-toc-content::after,
.md-toc::after {
  display: none;
}

.md-toc-item {
  display: block;
  color: rgb(65, 131, 196);
}

.md-toc-item a {
  text-decoration: none;
}

.md-toc-inner:hover {
  text-decoration: underline;
}

.md-toc-inner {
  display: inline-block;
  cursor: pointer;
}

.md-toc-h1 .md-toc-inner {
  margin-left: 0px;
  font-weight: 700;
}

.md-toc-h2 .md-toc-inner {
  margin-left: 2em;
}

.md-toc-h3 .md-toc-inner {
  margin-left: 4em;
}

.md-toc-h4 .md-toc-inner {
  margin-left: 6em;
}

.md-toc-h5 .md-toc-inner {
  margin-left: 8em;
}

.md-toc-h6 .md-toc-inner {
  margin-left: 10em;
}

@media screen and (max-width: 48em) {
  .md-toc-h3 .md-toc-inner {
    margin-left: 3.5em;
  }

  .md-toc-h4 .md-toc-inner {
    margin-left: 5em;
  }

  .md-toc-h5 .md-toc-inner {
    margin-left: 6.5em;
  }

  .md-toc-h6 .md-toc-inner {
    margin-left: 8em;
  }
}

a.md-toc-inner {
  font-size: inherit;
  font-style: inherit;
  font-weight: inherit;
  line-height: inherit;
}

.footnote-line a:not(.reversefootnote) {
  color: inherit;
}

.reversefootnote {
  font-family: ui-monospace, sans-serif;
}

.md-attr {
  display: none;
}

.md-fn-count::after {
  content: ".";
}

code,
pre,
samp,
tt {
  font-family: var(--monospace);
}

kbd {
  margin: 0px 0.1em;
  padding: 0.1em 0.6em;
  font-size: 0.8em;
  color: rgb(36, 39, 41);
  background: rgb(255, 255, 255);
  border: 1px solid rgb(173, 179, 185);
  border-radius: 3px;
  box-shadow: rgba(12, 13, 14, 0.2) 0px 1px 0px, rgb(255, 255, 255) 0px 0px 0px 2px inset;
  white-space: nowrap;
  vertical-align: middle;
}

.md-comment {
  color: rgb(162, 127, 3);
  opacity: 0.6;
  font-family: var(--monospace);
}

code {
  text-align: left;
  vertical-align: initial;
}

a.md-print-anchor {
  white-space: pre !important;
  border-width: medium !important;
  border-style: none !important;
  border-color: currentcolor !important;
  display: inline-block !important;
  position: absolute !important;
  width: 1px !important;
  right: 0px !important;
  outline: 0px !important;
  background: 0px 0px !important;
  text-decoration: initial !important;
  text-shadow: initial !important;
}

.os-windows.monocolor-emoji .md-emoji {
  font-family: "Segoe UI Symbol", sans-serif;
}

.md-diagram-panel>svg {
  max-width: 100%;
}

[lang="flow"] svg,
[lang="mermaid"] svg {
  max-width: 100%;
  height: auto;
}

[lang="mermaid"] .node text {
  font-size: 1rem;
}

table tr th {
  border-bottom-width: 0px;
  border-bottom-style: none;
  border-bottom-color: currentcolor;
}

video {
  max-width: 100%;
  display: block;
  margin: 0px auto;
}

iframe {
  max-width: 100%;
  width: 100%;
  border: medium;
}

.highlight td,
.highlight tr {
  border: 0px;
}

mark {
  background: rgb(255, 255, 0);
  color: rgb(0, 0, 0);
}

.md-html-inline .md-plain,
.md-html-inline strong,
mark .md-inline-math,
mark strong {
  color: inherit;
}

.md-expand mark .md-meta {
  opacity: 0.3 !important;
}

mark .md-meta {
  color: rgb(0, 0, 0);
}

@media print {

  .typora-export h1,
  .typora-export h2,
  .typora-export h3,
  .typora-export h4,
  .typora-export h5,
  .typora-export h6 {
    break-inside: avoid;
  }
}

.md-diagram-panel .messageText {
  stroke: none !important;
}

.md-diagram-panel .start-state {
  fill: var(--node-fill);
}

.md-diagram-panel .edgeLabel rect {
  opacity: 1 !important;
}

.md-fences.md-fences-math {
  font-size: 1em;
}

.md-fences-advanced:not(.md-focus) {
  padding: 0px;
  white-space: nowrap;
  border: 0px;
}

.md-fences-advanced:not(.md-focus) {
  background: inherit;
}

.typora-export-show-outline .typora-export-content {
  max-width: 1440px;
  margin: auto;
  display: flex;
  flex-direction: row;
}

.typora-export-sidebar {
  width: 300px;
  font-size: 0.8rem;
  margin-top: 80px;
  margin-right: 18px;
}

.typora-export-show-outline #write {
  --webkit-flex: 2;
  flex: 2 1 0%;
}

.typora-export-sidebar .outline-content {
  position: fixed;
  top: 0px;
  max-height: 100%;
  overflow: hidden auto;
  padding-bottom: 30px;
  padding-top: 60px;
  width: 300px;
}

@media screen and (max-width: 1024px) {

  .typora-export-sidebar,
  .typora-export-sidebar .outline-content {
    width: 240px;
  }
}

@media screen and (max-width: 800px) {
  .typora-export-sidebar {
    display: none;
  }
}

.outline-content li,
.outline-content ul {
  margin-left: 0px;
  margin-right: 0px;
  padding-left: 0px;
  padding-right: 0px;
  list-style: none;
  overflow-wrap: anywhere;
}

.outline-content ul {
  margin-top: 0px;
  margin-bottom: 0px;
}

.outline-content strong {
  font-weight: 400;
}

.outline-expander {
  width: 1rem;
  height: 1.428571rem;
  position: relative;
  display: table-cell;
  vertical-align: middle;
  cursor: pointer;
  padding-left: 4px;
}

.outline-expander::before {
  content: "";
  position: relative;
  font-family: Ionicons;
  display: inline-block;
  font-size: 8px;
  vertical-align: middle;
}

.outline-item {
  padding-top: 3px;
  padding-bottom: 3px;
  cursor: pointer;
}

.outline-expander:hover::before {
  content: "";
}

.outline-h1>.outline-item {
  padding-left: 0px;
}

.outline-h2>.outline-item {
  padding-left: 1em;
}

.outline-h3>.outline-item {
  padding-left: 2em;
}

.outline-h4>.outline-item {
  padding-left: 3em;
}

.outline-h5>.outline-item {
  padding-left: 4em;
}

.outline-h6>.outline-item {
  padding-left: 5em;
}

.outline-label {
  cursor: pointer;
  display: table-cell;
  vertical-align: middle;
  text-decoration: none;
  color: inherit;
}

.outline-label:hover {
  text-decoration: underline;
}

.outline-item:hover {
  border-color: rgb(245, 245, 245);
  background-color: var(--item-hover-bg-color);
}

.outline-item:hover {
  margin-left: -28px;
  margin-right: -28px;
  border-left-width: 28px;
  border-left-style: solid;
  border-left-color: transparent;
  border-right-width: 28px;
  border-right-style: solid;
  border-right-color: transparent;
}

.outline-item-single .outline-expander::before,
.outline-item-single .outline-expander:hover::before {
  display: none;
}

.outline-item-open>.outline-item>.outline-expander::before {
  content: "";
}

.outline-children {
  display: none;
}

.info-panel-tab-wrapper {
  display: none;
}

.outline-item-open>.outline-children {
  display: block;
}

.typora-export .outline-item {
  padding-top: 1px;
  padding-bottom: 1px;
}

.typora-export .outline-item:hover {
  margin-right: -8px;
  border-right-width: 8px;
  border-right-style: solid;
  border-right-color: transparent;
}

.typora-export .outline-expander::before {
  content: "+";
  font-family: inherit;
  top: -1px;
}

.typora-export .outline-expander:hover::before,
.typora-export .outline-item-open>.outline-item>.outline-expander::before {
  content: "−";
}

.typora-export-collapse-outline .outline-children {
  display: none;
}

.typora-export-collapse-outline .outline-item-open>.outline-children,
.typora-export-no-collapse-outline .outline-children {
  display: block;
}

.typora-export-no-collapse-outline .outline-expander::before {
  content: "" !important;
}

.typora-export-show-outline .outline-item-active>.outline-item .outline-label {
  font-weight: 700;
}

.md-inline-math-container mjx-container {
  zoom: 0.95;
}

mjx-container {
  break-inside: avoid;
}


.CodeMirror {
  height: auto;
}

.CodeMirror.cm-s-inner {
  background: inherit;
}

.CodeMirror-scroll {
  overflow: auto hidden;
  z-index: 3;
}

.CodeMirror-gutter-filler,
.CodeMirror-scrollbar-filler {
  background-color: rgb(255, 255, 255);
}

.CodeMirror-gutters {
  border-right-width: 1px;
  border-right-style: solid;
  border-right-color: rgb(221, 221, 221);
  background: inherit;
  white-space: nowrap;
}

.CodeMirror-linenumber {
  padding: 0px 3px 0px 5px;
  text-align: right;
  color: rgb(153, 153, 153);
}

.cm-s-inner .cm-keyword {
  color: rgb(119, 0, 136);
}

.cm-s-inner .cm-atom,
.cm-s-inner.cm-atom {
  color: rgb(34, 17, 153);
}

.cm-s-inner .cm-number {
  color: rgb(17, 102, 68);
}

.cm-s-inner .cm-def {
  color: rgb(0, 0, 255);
}

.cm-s-inner .cm-variable {
  color: rgb(0, 0, 0);
}

.cm-s-inner .cm-variable-2 {
  color: rgb(0, 85, 170);
}

.cm-s-inner .cm-variable-3 {
  color: rgb(0, 136, 85);
}

.cm-s-inner .cm-string {
  color: rgb(170, 17, 17);
}

.cm-s-inner .cm-property {
  color: rgb(0, 0, 0);
}

.cm-s-inner .cm-operator {
  color: rgb(152, 26, 26);
}

.cm-s-inner .cm-comment,
.cm-s-inner.cm-comment {
  color: rgb(170, 85, 0);
}

.cm-s-inner .cm-string-2 {
  color: rgb(255, 85, 0);
}

.cm-s-inner .cm-meta {
  color: rgb(85, 85, 85);
}

.cm-s-inner .cm-qualifier {
  color: rgb(85, 85, 85);
}

.cm-s-inner .cm-builtin {
  color: rgb(51, 0, 170);
}

.cm-s-inner .cm-bracket {
  color: rgb(153, 153, 119);
}

.cm-s-inner .cm-tag {
  color: rgb(17, 119, 0);
}

.cm-s-inner .cm-attribute {
  color: rgb(0, 0, 204);
}

.cm-s-inner .cm-header,
.cm-s-inner.cm-header {
  color: rgb(0, 0, 255);
}

.cm-s-inner .cm-quote,
.cm-s-inner.cm-quote {
  color: rgb(0, 153, 0);
}

.cm-s-inner .cm-hr,
.cm-s-inner.cm-hr {
  color: rgb(153, 153, 153);
}

.cm-s-inner .cm-link,
.cm-s-inner.cm-link {
  color: rgb(0, 0, 204);
}

.cm-negative {
  color: rgb(221, 68, 68);
}

.cm-positive {
  color: rgb(34, 153, 34);
}

.cm-header,
.cm-strong {
  font-weight: 700;
}

.cm-del {
  text-decoration: line-through;
}

.cm-em {
  font-style: italic;
}

.cm-link {
  text-decoration: underline;
}

.cm-error {
  color: red;
}

.cm-invalidchar {
  color: red;
}

.cm-constant {
  color: rgb(38, 139, 210);
}

.cm-defined {
  color: rgb(181, 137, 0);
}

div.CodeMirror span.CodeMirror-matchingbracket {
  color: rgb(0, 255, 0);
}

div.CodeMirror span.CodeMirror-nonmatchingbracket {
  color: rgb(255, 34, 34);
}

.cm-s-inner .CodeMirror-activeline-background {
  background: inherit;
}

.CodeMirror {
  position: relative;
  overflow: hidden;
}

.CodeMirror-scroll {
  height: 100%;
  outline: 0px;
  position: relative;
  box-sizing: content-box;
  background: inherit;
}

.CodeMirror-sizer {
  position: relative;
}

.CodeMirror-gutter-filler,
.CodeMirror-hscrollbar,
.CodeMirror-scrollbar-filler,
.CodeMirror-vscrollbar {
  position: absolute;
  z-index: 6;
  display: none;
  outline: 0px;
}

.CodeMirror-vscrollbar {
  right: 0px;
  top: 0px;
  overflow: hidden;
}

.CodeMirror-hscrollbar {
  bottom: 0px;
  left: 0px;
  overflow: auto hidden;
}

.CodeMirror-scrollbar-filler {
  right: 0px;
  bottom: 0px;
}

.CodeMirror-gutter-filler {
  left: 0px;
  bottom: 0px;
}

.CodeMirror-gutters {
  position: absolute;
  left: 0px;
  top: 0px;
  padding-bottom: 10px;
  z-index: 3;
  overflow-y: hidden;
}

.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  box-sizing: content-box;
  padding-bottom: 30px;
  margin-bottom: -32px;
  display: inline-block;
}

.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: 0px 0px !important;
  border: medium !important;
}

.CodeMirror-gutter-background {
  position: absolute;
  top: 0px;
  bottom: 0px;
  z-index: 4;
}

.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}

.CodeMirror-lines {
  cursor: text;
}

.CodeMirror pre {
  border-radius: 0px;
  border-width: 0px;
  background: 0px 0px;
  font-family: inherit;
  font-size: inherit;
  margin: 0px;
  white-space: pre;
  overflow-wrap: normal;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
}

.CodeMirror-wrap pre {
  overflow-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-code pre {
  border-right-width: 30px;
  border-right-style: solid;
  border-right-color: transparent;
  width: fit-content;
}

.CodeMirror-wrap .CodeMirror-code pre {
  border-right-width: medium;
  border-right-style: none;
  border-right-color: currentcolor;
  width: auto;
}

.CodeMirror-linebackground {
  position: absolute;
  inset: 0px;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  overflow: auto;
}

.CodeMirror-wrap .CodeMirror-scroll {
  overflow-x: hidden;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0px;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-measure pre {
  position: static;
}

.CodeMirror div.CodeMirror-cursor {
  position: absolute;
  visibility: hidden;
  border-right-width: medium;
  border-right-style: none;
  border-right-color: currentcolor;
  width: 0px;
}

.CodeMirror div.CodeMirror-cursor {
  visibility: hidden;
}

.CodeMirror-focused div.CodeMirror-cursor {
  visibility: inherit;
}

.cm-searching {
  background: rgba(255, 255, 0, 0.4);
}

span.cm-underlined {
  text-decoration: underline;
}

span.cm-strikethrough {
  text-decoration: line-through;
}

.cm-tw-syntaxerror {
  color: rgb(255, 255, 255);
  background-color: rgb(153, 0, 0);
}

.cm-tw-deleted {
  text-decoration: line-through;
}

.cm-tw-header5 {
  font-weight: 700;
}

.cm-tw-listitem:first-child {
  padding-left: 10px;
}

.cm-tw-box {
  border-style: solid;
  border-right-width: 1px;
  border-bottom-width: 1px;
  border-left-width: 1px;
  border-color: inherit;
  border-top-width: 0px !important;
}

.cm-tw-underline {
  text-decoration: underline;
}

@media print {
  .CodeMirror div.CodeMirror-cursor {
    visibility: hidden;
  }
}


:root {
  --side-bar-bg-color: #fafafa;
  --control-text-color: #777;
}

@include-when-export url(https://fonts.googleapis.com/css?family=Open+Sans:400italic,700italic,700,400&subset=latin,latin-ext);

/* open-sans-regular - latin-ext_latin */
/* open-sans-italic - latin-ext_latin */
/* open-sans-700 - latin-ext_latin */
/* open-sans-700italic - latin-ext_latin */
html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
}

body {
  font-family: "Open Sans", "Clear Sans", "Helvetica Neue", Helvetica, Arial, 'Segoe UI Emoji', sans-serif;
  color: rgb(51, 51, 51);
  line-height: 1.6;
}

#write {
  max-width: 860px;
  margin: 0 auto;
  padding: 30px;
  padding-bottom: 100px;
}

@media only screen and (min-width: 1400px) {
  #write {
    max-width: 1024px;
  }
}

@media only screen and (min-width: 1800px) {
  #write {
    max-width: 1200px;
  }
}

#write>ul:first-child,
#write>ol:first-child {
  margin-top: 30px;
}

a {
  color: #4183C4;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  position: relative;
  margin-top: 1rem;
  margin-bottom: 1rem;
  font-weight: bold;
  line-height: 1.4;
  cursor: text;
}

h1:hover a.anchor,
h2:hover a.anchor,
h3:hover a.anchor,
h4:hover a.anchor,
h5:hover a.anchor,
h6:hover a.anchor {
  text-decoration: none;
}

h1 tt,
h1 code {
  font-size: inherit;
}

h2 tt,
h2 code {
  font-size: inherit;
}

h3 tt,
h3 code {
  font-size: inherit;
}

h4 tt,
h4 code {
  font-size: inherit;
}

h5 tt,
h5 code {
  font-size: inherit;
}

h6 tt,
h6 code {
  font-size: inherit;
}

h1 {
  font-size: 2.25em;
  line-height: 1.2;
  border-bottom: 1px solid #eee;
}

h2 {
  font-size: 1.75em;
  line-height: 1.225;
  border-bottom: 1px solid #eee;
}

/*@media print {
    .typora-export h1,
    .typora-export h2 {
        border-bottom: none;
        padding-bottom: initial;
    }

    .typora-export h1::after,
    .typora-export h2::after {
        content: "";
        display: block;
        height: 100px;
        margin-top: -96px;
        border-top: 1px solid #eee;
    }
}*/

h3 {
  font-size: 1.5em;
  line-height: 1.43;
}

h4 {
  font-size: 1.25em;
}

h5 {
  font-size: 1em;
}

h6 {
  font-size: 1em;
  color: #777;
}

p,
blockquote,
ul,
ol,
dl,
table {
  margin: 0.8em 0;
}

li>ol,
li>ul {
  margin: 0 0;
}

hr {
  height: 2px;
  padding: 0;
  margin: 16px 0;
  background-color: #e7e7e7;
  border: 0 none;
  overflow: hidden;
  box-sizing: content-box;
}

li p.first {
  display: inline-block;
}

ul,
ol {
  padding-left: 30px;
}

ul:first-child,
ol:first-child {
  margin-top: 0;
}

ul:last-child,
ol:last-child {
  margin-bottom: 0;
}

blockquote {
  border-left: 4px solid #dfe2e5;
  padding: 0 15px;
  color: #777777;
}

blockquote blockquote {
  padding-right: 0;
}

table {
  padding: 0;
  word-break: initial;
}

table tr {
  border: 1px solid #dfe2e5;
  margin: 0;
  padding: 0;
}

table tr:nth-child(2n),
thead {
  background-color: #f8f8f8;
}

table th {
  font-weight: bold;
  border: 1px solid #dfe2e5;
  border-bottom: 0;
  margin: 0;
  padding: 6px 13px;
}

table td {
  border: 1px solid #dfe2e5;
  margin: 0;
  padding: 6px 13px;
}

table th:first-child,
table td:first-child {
  margin-top: 0;
}

table th:last-child,
table td:last-child {
  margin-bottom: 0;
}

.CodeMirror-lines {
  padding-left: 4px;
}

.code-tooltip {
  box-shadow: 0 1px 1px 0 rgba(0, 28, 36, .3);
  border-top: 1px solid #eef2f2;
}

.md-fences,
code,
tt {
  border: 1px solid #e7eaed;
  background-color: #f8f8f8;
  border-radius: 3px;
  padding: 0;
  padding: 2px 4px 0px 4px;
  font-size: 0.9em;
}

code {
  background-color: #f3f4f4;
  padding: 0 2px 0 2px;
}

.md-fences {
  margin-bottom: 15px;
  margin-top: 15px;
  padding-top: 8px;
  padding-bottom: 6px;
}


.md-task-list-item>input {
  margin-left: -1.3em;
}

@media print {
  html {
    font-size: 13px;
  }

  pre {
    page-break-inside: avoid;
    word-wrap: break-word;
  }
}

.md-fences {
  background-color: #f8f8f8;
}

#write pre.md-meta-block {
  padding: 1rem;
  font-size: 85%;
  line-height: 1.45;
  background-color: #f7f7f7;
  border: 0;
  border-radius: 3px;
  color: #777777;
  margin-top: 0 !important;
}

.mathjax-block>.code-tooltip {
  bottom: .375rem;
}

.md-mathjax-midline {
  background: #fafafa;
}

#write>h3.md-focus:before {
  left: -1.5625rem;
  top: .375rem;
}

#write>h4.md-focus:before {
  left: -1.5625rem;
  top: .285714286rem;
}

#write>h5.md-focus:before {
  left: -1.5625rem;
  top: .285714286rem;
}

#write>h6.md-focus:before {
  left: -1.5625rem;
  top: .285714286rem;
}

.md-image>.md-meta {
  /*border: 1px solid #ddd;*/
  border-radius: 3px;
  padding: 2px 0px 0px 4px;
  font-size: 0.9em;
  color: inherit;
}

.md-tag {
  color: #a7a7a7;
  opacity: 1;
}

.md-toc {
  margin-top: 20px;
  padding-bottom: 20px;
}

.sidebar-tabs {
  border-bottom: none;
}

#typora-quick-open {
  border: 1px solid #ddd;
  background-color: #f8f8f8;
}

#typora-quick-open-item {
  background-color: #FAFAFA;
  border-color: #FEFEFE #e5e5e5 #e5e5e5 #eee;
  border-style: solid;
  border-width: 1px;
}

/** focus mode */
.on-focus-mode blockquote {
  border-left-color: rgba(85, 85, 85, 0.12);
}

header,
.context-menu,
.megamenu-content,
footer {
  font-family: "Segoe UI", "Arial", sans-serif;
}

.file-node-content:hover .file-node-icon,
.file-node-content:hover .file-node-open-state {
  visibility: visible;
}

.mac-seamless-mode #typora-sidebar {
  background-color: #fafafa;
  background-color: var(--side-bar-bg-color);
}

.md-lang {
  color: #b4654d;
}

/*.html-for-mac {
    --item-hover-bg-color: #E6F0FE;
}*/

#md-notification .btn {
  border: 0;
}

.dropdown-menu .divider {
  border-color: #e5e5e5;
  opacity: 0.4;
}

.ty-preferences .window-content {
  background-color: #fafafa;
}

.ty-preferences .nav-group-item.active {
  color: white;
  background: #999;
}

.menu-item-container a.menu-style-btn {
  background-color: #f5f8fa;
  background-image: linear-gradient(180deg, hsla(0, 0%, 100%, 0.8), hsla(0, 0%, 100%, 0));
}


@media print {
  @page {
    margin: 0 0 0 0;
  }

  body.typora-export {
    padding-left: 0;
    padding-right: 0;
  }

  #write {
    padding: 0;
  }
}
</style>
