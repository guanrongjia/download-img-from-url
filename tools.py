# -*- coding: utf-8 -*-
import urllib2
import os
import re
import sys
import time
import json
import traceback
from bs4 import BeautifulSoup

##################### 1、check URL #########################
def check_url(source_url):
    url_result = False
    source_url = source_url.strip()
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if len(regex.findall(source_url)):
        url_result = True

    return url_result


##################### 2、filter image urls #########################
def filterImageUrls(source_url):
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    dirname = os.path.dirname(dirname)
    dirname = os.path.join(dirname, u'image-download')
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    print "*" * 50
    print u'the location to save images：%s' % dirname
    req = urllib2.urlopen(source_url)
    html_doc = req.read()
    soup = BeautifulSoup(html_doc)
    div_html = soup.find_all("img")
    img_objs = []

    for one_img_attr in div_html:
        # we user data-original here ,for the image is lazy loading.
        # the value of key data-original is where the real url lives
        img_src = one_img_attr.attrs.get('data-original') or one_img_attr.attrs.get('src')
        img_name = one_img_attr.attrs.get('alt') or one_img_attr.attrs.get('title') or ''
        if img_src:
            img_objs.append({'img_src': img_src, 'img_name': img_name})


    return dirname, img_objs


##################### 3、download image #########################
def downloadImages(dirname, img_objs):
    timestamp = str(int(time.time()))
    for index, img_obj in enumerate(img_objs):
        try:
            img_src = img_obj.get('img_src')
            img_src = img_src.replace('-228x228.jpg', '-600x600.jpg')
            img_name = img_obj.get('img_name')
            data = urllib2.urlopen(img_src, timeout=25).read()
            ext = os.path.splitext(img_src)[-1]
            ext = ext.split('!')[0]
            ext = ext.split('@')[0]
            file_name = (img_name or timestamp + '_' + str(index)) + ext
            file_path = os.path.join(dirname, file_name)
            image = open(file_path, 'wb')
            image.write(data)
            image.close()
            print 'image index: %s is downloaded' % index

        except Exception, e:
            print "******************** ERROR ********************"
            print index, json.dumps(img_obj, ensure_ascii=False)
            print "****************"
            print(traceback.format_exc())

    return 'picture download finished!<br/> "%s" pictures are downloaded' % len(img_objs)


