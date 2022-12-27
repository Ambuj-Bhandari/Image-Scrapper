# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:24:49 2020

@author: krish.naik
"""

from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    
    keyword=""
    fileLoc=""
    image_name=""
    header=""
     
    def downloadImages( keyWord):
        imgScrapper = ScrapperImage
        url = imgScrapper.createImageUrl(keyWord)
        imageURLList = imgScrapper.scrap_html_data(url)
        
        #imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord)
        
        return masterListOfImages    
   
    
    