# coding=gb2312
import re
import csv
f=open('sentences.csv','w')
csvwriter=csv.writer(f)
def sentsplit(name):
    try:
        with open(name,'r') as f:
            text=f.read()
        # 将文本按行分割，并过滤掉空行
        lines = [line for line in text.splitlines() if line.strip()]
        # 将文本行用回车符连接成一个字符串
        text = ''.join(lines)
        sen=re.split(r'[。！？\n]',text)
        for sent in sen:
            csvwriter.writerow((sent,))
        print(name + 'done!')
            # print(sent+'。')
    except FileNotFoundError:
        print(name+'not found!continue...')

if __name__=='__main__':
    names=[]
    with open('urls.csv',mode='r')as f:
        csvreader=csv.reader(f)
        for row in csvreader:
            names.append('essays/'+row[0].rsplit('/',1)[1].replace('.html','.txt'))#获取文件名
    for name in names:
        sentsplit(name)
    f.close()