import aiohttp
import asyncio
import aiofiles
from lxml import etree
import csv
import requests
# parser=etree.XMLParser(encoding='utf-8')
# resp=requests.get('https://www.lunwendata.com/thesis/2023/161406.html').text
# print(resp)
# content = resp.text
parser=etree.HTMLParser(encoding='gb2312')
async def transessay(name):

    async with aiofiles.open(name,'r') as f0:
            content = await f0.read()
            tree=etree.XML(content,parser=parser)
            content = tree.xpath('//*[@id="content"]//text()')
            content = ''.join(content)
    f0.close()
    async with aiofiles.open(name,mode='w',encoding='gb2312',errors='ignore') as f:
        try:
            await f.write(content)
        except UnicodeDecodeError:
            pass
    print(name+'done!')

async def main():
    tasks=[]
    with open('urls.csv',mode='r')as f:
        csvreader=csv.reader(f)
        for row in csvreader:
            name='essays/'+row[0].rsplit('/',1)[1].replace('.html','.txt')
            tasks.append(transessay(name))
        await asyncio.wait(tasks)
    pass
if __name__=='__main__':
    asyncio.run(main())