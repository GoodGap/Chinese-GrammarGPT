from corrector.raw import LLMCorrector
llmcorrector=LLMCorrector()
while True:
    print('输入:\n')
    m=input()
    response=llmcorrector.GEC_Correction(m)
    print('结果：',response,'\n')
# [(1,2,'你们','我们'),()]cpn