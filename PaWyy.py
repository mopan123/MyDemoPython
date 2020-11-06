# @Time    : 2020/9/16 15:22
# @Author  : mopan
# @File    : PaWyy.py
# @Software: PyCharm

import requests
from lxml import etree
def music():
    url = 'https://music.163.com/discover/toplist?id=3778678'

    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)
    #print(response)
    html=etree.HTML(response.text)
    id_list=html.xpath('//a[contains(@href,"/song?")]')
    #print(id_list)
    for data in id_list:
        url_base = 'https://music.163.com/song/media/outer/url?id='  #获取音乐路径
        href=data.xpath('./@href')[0]
        music_id=href.split("=")[1]
        music_name=data.xpath('./text()')[0]
        music_url=url_base+music_id
        music=requests.get(url=music_url,headers=headers)
        with open('F:\\Desktop' % music_name,'wb') as file:
           file.write(music.content)
        print('<%s>下载成功' % music_name)


music()