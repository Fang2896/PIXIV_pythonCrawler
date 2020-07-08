import os, re, csv
import numpy as np
import codecs
import requests

class file:
    def __init__(self):
        pass
    
    # download函数为下载指定图片, 保存到 以"year-mouth'命名的文件夹里。
    # 图片命名为 "name-pid.jpg"
    def download(self, url, rank, title):
        headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        }
        pid = re.search('\d{8}', url).group()
        headers["referer"] = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + pid
        
        img = requests.get(url, headers=headers).content

        with open('{}#{}-{}.jpg'.format(str(rank), title,pid), "wb") as f:
            f.write(img)
            print("Download sucecess: {}".format(rank))



    # 废弃。存储到csv文件乱码问题未解决
    # =============================================================== #
    # 将爬取到的图片信息保存到其对应月份的文件夹
    # def sav_csv(self, total_info):
    #     line_head = ['rank', 'title', 'author', 'pid', 'url']
    #     line_info = np.array(total_info).transpose()
    #     print(type(line_info))
    #     line_info = line_info.tolist()
    #     print(type(line_info))

    #     with open("info.csv", "w", encoding="utf-8", newline='') as fp:
    #         writer = csv.writer(fp)
    #         writer.writerow(line_head)
    #         writer.writerows(line_info)
    # =============================================================== #