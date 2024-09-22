# coding=gb2312
import re
import csv
f=open('sentences.csv','w')
csvwriter=csv.writer(f)
def sentsplit(name):
    try:
        with open(name,'r') as f:
            text=f.read()
        # ���ı����зָ�����˵�����
        lines = [line for line in text.splitlines() if line.strip()]
        # ���ı����ûس������ӳ�һ���ַ���
        text = ''.join(lines)
        sen=re.split(r'[������\n]',text)
        for sent in sen:
            csvwriter.writerow((sent,))
        print(name + 'done!')
            # print(sent+'��')
    except FileNotFoundError:
        print(name+'not found!continue...')

if __name__=='__main__':
    names=[]
    with open('urls.csv',mode='r')as f:
        csvreader=csv.reader(f)
        for row in csvreader:
            names.append('essays/'+row[0].rsplit('/',1)[1].replace('.html','.txt'))#��ȡ�ļ���
    for name in names:
        sentsplit(name)
    f.close()