# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:51:15 2020

@author: krish.naik
"""

from bs4 import BeautifulSoup as bs
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)


class ScrapperImage:
    
    ## Create  Image URl
    def createImageUrl(searchterm):
        searchterm=searchterm.split()
        searchterm="+".join(searchterm)
        web_url="https://www.google.com/search?q=" + searchterm + "&source=lnms&tbm=isch"
        return web_url
    
   # get Raw HTML
    def scrap_html_data(url):
        driver.get(url)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
        imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")

        #request=urllib.request.Request(url,headers=header)
        #response = urllib.request.urlopen(request)
        #responseData = response.read()
        #html = bs(responseData, 'html.parser')
        return imgResults
    
    # contains the link for Large original images, type of  image
    
    def downloadImagesFromURL(imageUrlList,image_name):
        ###print images
        src = []
        for img in imageUrlList:
            src.append(img.get_attribute('src'))
            
        return src
    
    def delete_downloaded_images(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/"+self.image)
            except Exception as e:
                print('error in deleting:  ',e)
        return 0
    
   
    
    
    
    