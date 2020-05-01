from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

# 输入浏览器的信息，用户代理
# headers = {'use-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
# url = Request("https://www.zhipin.com/shenzhen/", headers=headers)
# html = urlopen(url, timeout=150)

html = urlopen("https://www.zhipin.com/shenzhen/?sid=sem_pz_bdpc_dasou_title")
bsobj = BeautifulSoup(html)
for link in bsobj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
