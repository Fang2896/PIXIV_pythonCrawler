import requests, csv
import numpy as np
from bs4 import BeautifulSoup
import re, os, requests
from url import url
from file import file
from multiprocessing import Pool

month = 5
year = 2020

if __name__=='__main__':

    # 测试file.py 文件功能
    path = "F:\H_img"
    folder_name = str(year) + "-" + str(month)
    os.chdir(path)
    os.mkdir(folder_name)
    os.chdir(path + "\\" + folder_name)
    
    p = Pool(8)
    
    # 测试 url.py 文件功能
    total_info = url().get_info(year, month)
    print(len(total_info[1]))
    pre_url = total_info[4]
    ori_url = url().ori_url(pre_url)
    # print(ori_url)
    # 测试成功！

    print(total_info)
    
    
    rank = 1
    for url in ori_url:
        p.apply_async(file().download, args=(url, rank, total_info[1][rank-1]))
        rank += 1
    p.close()
    p.join()

# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#     "referer":"https://www.pixiv.net/ranking.php"
# }

# baseurl='https://www.pixiv.net/ranking.php?mode=monthly&content=illust&date=20200501'


# html=requests.get(baseurl, headers=headers)
# soup = BeautifulSoup(html.content, 'lxml')

# all_infos = soup.find_all(class_="ranking-item")

# l_urls = []
# l_ranks = []
# l_pids = []
# l_titles = []
# l_authors = []

# rank = 1
# for info in all_infos:
#     url = info.find("img").get('data-src')
#     pid = re.search('\d{7,9}', url).group()
#     l_pids.append(pid)
#     l_urls.append(url)
#     l_titles.append(info.get("data-title"))
#     l_authors.append(info.get("data-user-name"))
#     l_ranks.append(rank)
#     rank += 1

# total_info = np.transpose(np.array([l_ranks, l_titles, l_authors, l_pids,l_urls]))
# print(total_info)