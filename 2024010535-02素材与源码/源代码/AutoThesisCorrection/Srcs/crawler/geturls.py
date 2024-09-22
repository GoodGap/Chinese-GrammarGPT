import requests
from lxml import etree
import csv
# async def get_urls(url):
#     f=open('urls.txt',mode='w')
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             content=await resp.text()
#
def getcalalog(url):
    resp = requests.get(url).text
    # resp=BeautifulSoup(resp,"html")
    # print(resp)
    parser = etree.HTMLParser(encoding='gb2312')
    tree = etree.XML(resp, parser=parser)
    urls = tree.xpath('//*[@id="nav"]//li/a/@href')
    return urls
    # print(urls)
def geturls(url):
    resp=requests.get(url).text
    # resp=BeautifulSoup(resp,"html")
    # print(resp)
    parser=etree.HTMLParser(encoding='gb2312')
    tree=etree.XML(resp,parser=parser)
    urls=tree.xpath('//*[@id="column"]//dd/a/@href')
    # print(urls)
    return urls
# geturls('https://www.lunwendata.com/thesis/List_11.html')
# getcalalog('https://www.lunwendata.com/thesis/List_11.html')
# async def main():
#     pass
if __name__=='__main__':
    f=open('urls.csv','w')
    csvwriter=csv.writer(f)
    catalogs=getcalalog('https://www.lunwendata.com/thesis/List_11.html')
    catalogs=['https://www.lunwendata.com'+i for i in catalogs]
    for catalog in catalogs:
        urls=geturls(catalog)
        for url in urls:
            csvwriter.writerow((url.strip(),))
    f.close()
