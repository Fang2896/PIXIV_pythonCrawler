'''
参考url
缩略图：
https://i.pximg.net/c/240x480/img-master/img/2019/02/24/00/00/27/73355010_p0_master1200.jpg
原图：
https://i.pximg.net/img-master/img/2019/02/24/00/00/27/73355010_p0_master1200.jpg
容易看出，缩略图和原图的url差别仅仅是多了"/c/240x480"
考虑采用正则匹配来通过缩略图来获取原图。以避免登录  '''

import requests, re
from bs4 import BeautifulSoup


class url:
    def __init__(self):
        self.l_pids = []
        self.l_urls = []
        self.l_ranks = []
        self.l_titles = []
        self.l_authors = []
        self.rank = 1
        self.headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "referer":"https://www.pixiv.net/ranking.php"
        }
    # 获取xx年xx月的前50排行榜信息。包括[rank, title, author, pid, url]
    def get_info(self, year, month):
        
        baseurl='https://www.pixiv.net/ranking.php?mode=monthly&content=illust&date={}{}01'.format(str(year), str(month).zfill(2))

        html=requests.get(baseurl, headers=self.headers)

        # with open("test.html", "w", encoding="utf-8") as fp:
        #     fp.write(html.text)

        soup = BeautifulSoup(html.content, 'lxml')

        all_infos = soup.find_all(class_="ranking-item")

        for info in all_infos:
            url = info.find("img").get('data-src')
            pid = re.search('\d{8}', url).group()
            self.l_pids.append(pid)
            self.l_urls.append(url)
            self.l_titles.append(info.get("data-title"))
            self.l_authors.append(info.get("data-user-name"))
            self.l_ranks.append(self.rank)
            self.rank += 1
        total_info = [self.l_ranks, self.l_titles, self.l_authors, self.l_pids, self.l_urls]

        print("Get All URL Sucecess.\n")

        return total_info


    # change_url函数将缩略图网址用字符串替换方法得到原网址
    def ori_url(self, llist):
        orilist = []    # 原图网址
        for i in llist:
            tem = re.search("/c/\d{0,3}x\d{0,3}/img-master/", i).group()
            i = i.replace(tem, "/img-master/")
            orilist.append(i)
        print("Change URL Sucess.\n")
        return orilist