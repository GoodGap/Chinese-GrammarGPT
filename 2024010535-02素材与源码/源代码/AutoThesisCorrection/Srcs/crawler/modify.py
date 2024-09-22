# coding=gb2312
import csv
import re
f=open('sentence_modified.csv','w')
pattern = re.compile(r'(?<![a-zA-Z])\s+(?![a-zA-Z])')
pattern0 = re.compile('[\u4e00-\u9fff]')
writer=csv.writer(f)
with open('sentences.csv','r') as w:
    reader=csv.reader(w)
    for row in reader:
        row[0]=row[0].strip()
        r=re.split(pattern,row[0])
        # print(r)
        for r0 in r:
            if(len(r0)>25 and re.search(pattern0, r0)!=None):
                writer.writerow((r0.strip(),))
    f.close()
w.close()
# # #
# pattern = re.compile(r'(?<![a-zA-Z])\s+(?![a-zA-Z])')
# r=re.split(pattern,"this is an sentence 这是一句中文句子。 你好！hello another 英文 sentence here." )
# print(r)
# import re
#
# def is_english_sentence(sentence):
#
#     return re.match(pattern, sentence) != None
# print(is_english_sentence("hello 你好"))
# import re
#
# pattern = re.compile('[\u4e00-\u9fff]')
#
# def has_chinese(sentence):
#     return re.search(pattern, sentence)
# sentence="(20)lt's once in a blue moon that you get a chance like that."
# if not has_chinese(sentence):
#     print(has_chinese(sentence))