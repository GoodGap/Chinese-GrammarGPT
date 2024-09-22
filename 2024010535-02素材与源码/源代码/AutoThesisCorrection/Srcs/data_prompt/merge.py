import pandas as pd
df1=pd.read_csv('/home/grammar/Paper_Corrector/model/dataset.csv',low_memory=False)
# for i in df1:
#     print(i)
# print(df1.keys)
df2=pd.read_csv('/home/grammar/Paper_Corrector/model/resp.csv')
print(df2)
# for i in df2:
    # print(i)
df=pd.merge(df2,df1,on=u"病句".encode('utf-8'),how='left')
df.to_csv('test.csv', encoding="utf_8_sig")