from bs4 import BeautifulSoup
from urllib.parse import unquote
import sys
from all_loader import *





def get_next(soup):
    stime=str(int(time.time()))
    try:
        # soup = BeautifulSoup(html, 'html.parser')
        next_page = 'https://www.amazon.com' + soup.find_all('li', 'a-last')[0].contents[0].attrs['href']
        next_page = next_page.split("qid=")[0]+"qid="+stime+ "&" +next_page.split("qid=")[1].split('&')[1]
        return next_page
    except Exception as e:
        print(e)
        return 0



def US_analysis(html,page,search_asin):
    # page=1
    print("当前页数是:%s"%page)
    soup=BeautifulSoup(html,'html.parser')
    tags=soup.find_all('h5','a-color-base s-line-clamp-4')
    print(len(tags))
    for tag in tags:
        sp=tag.parent.contents[1].text
        if sp=='Sponsored':
            sp='Sponsored'
        else:
            sp='非广告'
        url = tag.contents[1].attrs['href']
        url=unquote(url,'utf-8')
        asin=url.split('/dp/')[1].split('/')[0]
        # print(asin,sp)
        if asin==search_asin:
            print('当前页数是',page,'排名:',tags.index(tag),"广告:",sp)
            with open('test.html','w',encoding='utf-8') as f:
                f.write(html)
            sys.exit()
            return 'GG'
    next_page=get_next(soup)
    print('next>>',next_page)
    page+=1
    if next_page==0:
        print('全部抓取完成')
    else:
        html=loader(next_page)
        US_analysis(html,page,search_asin)