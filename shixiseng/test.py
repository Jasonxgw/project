# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 19:54:46 2018

@author: Jun Gao
"""
import re
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import os

kv = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2 ',
    "Referer": "https://www.shixiseng.com"}
search_keyword = "数据"
replace_dict = {"\ue471": "0",
                "\uf530": "1",
                "\ue79d": "2",
                "\ue1ca": "3",
                "\uef99": "4",
                "\uf77e": "5",
                "\uf3d5": "6",
                "\uf8f2": "7",
                "\uf30e": "8",
                "\ue9a3": "9"}

result = np.array([['job_name', 'job_benefit', 'job_detail', 'salary', 'day_per_week', 'address']])
for page in np.arange(0, 5):
    url1 = "https://www.shixiseng.com/interns/c-110100_?k={}&p={}".format(search_keyword, page)
    r = requests.get(url1, headers=kv)
    if r.status_code == 200:
        print("第{}页索引页抓取成功".format(page))
    else:
        print("第{}页索引页抓取失败".format(page))
        break
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.prettify()
    url2_behind_list = re.findall(r'"intern_uuid": "(.*?)"', text)
    for index, i in enumerate(url2_behind_list):
        url2 = "https://www.shixiseng.com/intern/" + i
        r = requests.get(url2, headers=kv)
        if r.status_code == 200:
            print("第{}页-{}-{}抓取成功".format(page, index, i))
        else:
            print("第{}页-{}-{}抓取失败".format(page, index, i))
            break
        soup = BeautifulSoup(r.content, "html.parser")
        text = soup.prettify()
        for key, value in replace_dict.items():
            text = text.replace(key, value)

        job_name = re.findall(r'<div class="new_job_name" title="(.*?)">', text)[0].replace('\t', '').replace('\n',
                                                                                                              '').replace(
            ' ', '')
        job_benefit = re.findall(r'职位诱惑：(.*?)\n', text)[0].replace('\t', '').replace('\n', '').replace(' ', '')
        job_detail = re.findall(r'<div class="job_detail">([\s\S]*?)<div class="job_til">', text)[0].replace('\t',
                                                                                                             '').replace(
            '\n', '').replace(' ', '')
        job_detail = re.sub(r'<[\s\S]*?>', "", job_detail)
        salary = re.findall(r'(.*?)／天', text)[0].strip()
        day_per_week = re.findall(r'(.?)天／周', text)[0].strip()
        address = re.findall(r'<span class="com_position">([\s\S]*?)</span>', text)[0].strip()
        print("第{}页-{}-{}正在写入".format(page, index, i))
        data = [job_name, job_benefit, job_detail, salary, day_per_week, address]
        result = np.row_stack((result, data))

