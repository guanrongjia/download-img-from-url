# -*- coding: utf-8 -*-
import urllib2
import os
from bs4 import BeautifulSoup


def downloadImg(uri):
    req = urllib2.urlopen(uri)
    html_doc = req.read()
    soup = BeautifulSoup(html_doc)
    div_html = soup.find_all("img")
    img_src_list = []

    for one_img_attr in div_html:
        data_original = one_img_attr.attrs.get('data-original')
        if data_original:
            img_src_list.append(data_original)

    for index, img_src in enumerate(img_src_list):
        try:
            ext = os.path.splitext(img_src)[-1]
            data = urllib2.urlopen(img_src).read()
            file_name = str(index) + ext
            file_path = os.path.join(r'C:\Users\namibox\Desktop\tmp', file_name)
            image = open(file_path, 'wb')
            image.write(data)
            image.close()
            print index

        except Exception, e:
            print "**** ERROR ****"
            print index, img_src
