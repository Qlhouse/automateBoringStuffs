import time
import os
import numpy as np
from PIL import Image
import cv2
import requests
import queue
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://product.dangdang.com/1181643189.html'

# Scrape the product url, return a queue contains image urls
def getProductDetailImageUrls(url):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    
    driver.get(url)
    
    # Scroll down to end of the page
    # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # SCROLL_PAUSE_TIME = 0.5
    # 
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 
    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)
    # 
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    
    time.sleep(5)
    driver.refresh()
    
    try:
        imgUrlQueue = queue.Queue()
        # Parse product detail image address
        productDetailTag = driver.find_element_by_xpath('//*[@id="description"]/div[2]')
        soup = BeautifulSoup(productDetailTag.get_attribute('innerHTML'), 'html.parser')
        imgTag = soup.find('img')
        imgUrlQueue.put(imgTag['src'])
        while imgTag.next_sibling:
            imgTag = imgTag.next_sibling
            imgUrlQueue.put(imgTag['src'])
        
        return imgUrlQueue
        # while not imgUrlQueue.empty():
        #     print(imgUrlQueue.get())
    except:
        print("Sorry! 请重运行...")
    finally:
        # Close Firefox
        driver.quit()

# Download images in queue, concatenate them, write out 
imgUrlQueue = getProductDetailImageUrls(url)

# openCV version
def downloadImageAndStoredInList(imgUrlQueue):
    imgList = []
    while not imgUrlQueue.empty():
        imgUrl = imgUrlQueue.get()
        if imgUrl.endswith('.jpg'):
            resp = requests.get(imgUrl, stream=True).raw
            img = np.asarray(bytearray(resp.read()), dtype=np.uint8)
            imgList.append(cv2.imdecode(img, -1))

    return imgList

# concatenate imgs
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

imgList = downloadImageAndStoredInList(imgUrlQueue)

im_v_resize = vconcat_resize_min(imgList)
cv2.imwrite('opencv_vconcat_resize.jpg', im_v_resize)

print('Done...')

# pillow version 
# def downloadImageAndStoredInList(imgUrlQueue):
#     imgList = []
#     while not imgUrlQueue.empty():
#         imgUrl = imgUrlQueue.get()
#         if imgUrl.endswith('.jpg'):
#             img = Image.open(requests.get(imgUrl, stream=True).raw)
#             imgList.append(img)
# 
#     return imgList
#     
# imgList = downloadImageAndStoredInList(imgUrlQueue)
# min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgList])[0][1]
# imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgList ))
# imgs_comb = Image.fromarray( imgs_comb)
# imgs_comb.save( 'Trifecta_vertical.jpg' )
