from gecllm import LLMCorrector
llmcorrector=LLMCorrector()
while True:
    m=input()
    response=llmcorrector.GEC_Correction(m)
    print('修正结果：',edits)
# [(1,2,'你们','我们'),()]