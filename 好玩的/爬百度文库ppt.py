#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Time   :2022/12/6 16:04
@Author :tisugou
@DESC   :
'''


import requests
import os
from lxml import etree


# 创建目录方法
def create_file(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

url = 'https://wenku.baidu.com/view/fdceea852aea81c758f5f61fb7360b4c2e3f2acb.html?fr=income2-doc-search&_wkts_=1678090422499&wkQuery=%E5%8E%86%E5%8F%B2%E5%B8%8C%E7%89%B9%E5%8B%92'

resp = requests.get(url)

# print(resp.text)
text = resp.text

html = etree.HTML(text)

img_list = html.xpath('//div[@class="mod flow-ppt-mod"]/div/div/img')

# 计数
cnt = 1

# 文件保存路径
file_path = './wendang/'
create_file(file_path)

# 获取图片
for i in img_list:
    try:
        img_url = i.xpath('./@src')[0]
    except:
        img_url = i.xpath('./@data-src')[0]

    # 文件名称
    file_name = f'{file_path}page_{cnt}.jpg'
    print(file_name, img_url)
    # 下载保存图片
    resp = requests.get(img_url)
    with open(file_name, 'wb') as f:
        f.write(resp.content)

    cnt += 1