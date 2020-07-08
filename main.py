import os
from url import url
from file import file
from multiprocessing import Pool

year = '2019'
month = '06'
path = "F:\\H_img"


if __name__=='__main__':

    folder_name = str(year) + "-" + str(month)
    os.chdir(path)
    os.mkdir(folder_name)
    os.chdir(path + "\\" + folder_name)
    
    p = Pool(8)
    
    total_info = url().get_info(year, month)
    print(len(total_info[1]))
    pre_url = total_info[4]
    ori_url = url().ori_url(pre_url)
    
    rank = 1
    for url in ori_url:
        p.apply_async(file().download, args=(url, rank, total_info[1][rank-1]))
        rank += 1
    p.close()
    p.join()