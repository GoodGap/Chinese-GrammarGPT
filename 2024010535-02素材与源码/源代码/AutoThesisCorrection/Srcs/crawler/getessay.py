import aiohttp
import asyncio
import aiofiles
import csv
from lxml import etree
parser=etree.XMLParser(encoding='gb2312')
async def getessay(url):
    name='essays/'+url.rsplit('/',1)[1].replace('.html','.txt')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.text(encoding='gb2312')
            tree=etree.XML(content,parser=parser)
            content=tree.xpath('//*[@id="content"]/p/text()')
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
            tasks.append(getessay(row[0]))
        await asyncio.wait(tasks)
    pass
if __name__=='__main__':
    asyncio.run(main())