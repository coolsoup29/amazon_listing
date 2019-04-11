from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait       #WebDriverWait注意大小写
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from setting import *
import random as R

user_agent = [
           "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
           "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
           "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
           "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
           "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
           "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
           "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
           "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
           "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
       ]


# 注意修改　54 行的等待元素规则
def selenium_loader(url):

    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # 无头模式
    chrome_options.add_argument('--disable-gpu')
    prefs = {"profile.managed_default_content_settings.images": 2} #使用无图模式  #
    # chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument('--proxy-server=http://%s'%IP_html)  # 使用代理IP

    chrome_options.add_argument('--user-agent=%s' % R.choice(user_agent))



    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(CHROM_PATH,options=chrome_options,desired_capabilities=capa)  # 关键!记得添加
    wait = WebDriverWait(driver, 20)
    driver.get(url)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='s-result-list sg-row']")))  # 这里可选择多个selector
    html=driver.page_source
    return html


def loader(url):
    req=requests.get(url,headers=headers_img)
    req.encoding='utf-8'
    html=req.text
    return html