import pycorrector
from pycorrector.macbert.macbert_corrector import MacBertCorrector


class ErrorCorrect:
    def __init__(self, model_path="shibing624_macbert4csc-base-chinese/"):
        self.m = MacBertCorrector(model_path)

    def correct(self, input_prompt):
        correct_sent, err = self.m.macbert_correct(input_prompt)
        # print("query:{} => {}, err:{}".format(input_prompt, correct_sent, err))
        return correct_sent


if __name__ == "__main__":
    error_sentences = [
        '你找到你最喜的工作，我也很高心。',
        '真麻烦你了,希望你们好好的跳无。',
        '少先队员因该为老人让坐。',
        '机七学习是人工智能领遇最能体现智能的一个分知。',
        '一只小鱼船浮在平净的河面上。',
        '我的家乡是有明的渔米之乡。',
    ]
    ec = ErrorCorrect()
    result = ec.correct("\n".join(error_sentences))
    print(result)
    # exit()
    # for each in error_sentences:
    #     print(each, " --> ", ec.correct(each))
