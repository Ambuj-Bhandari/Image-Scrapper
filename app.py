# -*- coding: utf-8 -*-
"""
@author: Krish Naik
"""
# Importing the necessary Libraries
from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request,jsonify
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=chrome_options)

# import request
app = Flask(__name__) # initialising the flask app with the name 'app'

#response = 'Welcome!'


@app.route('/')  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayImages(list_images):
    list_images=os.listdir('static')
    print(list_images)
    
    try:
        if(len(list_images)>0):
            return render_template('showImage.html',user_images=list_images)
        else:
            return "Images are not present"
    except Exception as e:
        print("No images found",e)
        return "Please try with a different search keyword"
    
@app.route('/searchImages',methods=['Get','POST'])
def searchImage():
   
    if request.method=="POST":
        search_term=request.form['keyword'] # assigning the value of the input keyword to the variable keyword
        
    else:
        print("Please enter something")
    
    
    list_of_images=os.listdir('static') ## Delete the old images before search
    for image in list_of_images:
        try:
            os.remove("./static/"+image)
        except Exception as e:
            print('error in deleting:  ',e)
    
    image_name=search_term.split()
    image_name="+".join(image_name)
    
    url = ("https://www.google.com/search?q="+image_name+"&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568")
    # Launch the browser and open the given url in the webdriver.
    driver.get(url)
    # Scroll down the body of the web page and load the images.
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
    # Find the images.
    imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'Q4LuWd')]")
    # Access and store the scr list of image url's.
    lst_images= []
    for img in imgResults:
        lst_images.append(img.get_attribute('src'))
    # Retrieve and download the images.
    for i in range(10):    
        urllib.request.urlretrieve(str(lst_images[i]),"static/{}{}.jpg".format(image_name,i))
    
    return displayImages(lst_images) # redirect the control to the show images method
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000) # port to run on local machine
   #app.run(debug=True) # to run on cloud
