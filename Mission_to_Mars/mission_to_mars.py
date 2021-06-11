#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit webiste
    url = "https://redplanetscience.com/"
    browser.visit(url)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Get the title
    title = soup.find('div', class_='content_title').text
    
    # Get paragraph text
    paragraph = soup.find('div', class_='article_teaser_body').text
    
    # Store into dictionary
    mars_data = {
        "title": title,
        "paragraph": paragraph,
        "feat_img": feat_img(browser),
        "facts": facts(),
        "image_store": mars_img(browser)
    }
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


# In[ ]:





# In[3]:


# Store image
def feat_img(browser):
    url="https://spaceimages-mars.com/"
    browser.visit(url)

# Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
# Get the image
    raw_img = soup.find('img', class_='headerimage fade-in').get("src")
    feat_img = url + raw_img
    return feat_img


# In[4]:


def facts():
    df=pd.read_html("https://galaxyfacts-mars.com/")[1]
    df.columns=["Mars Facts", "Measurement"]
    return df.to_html()


# In[5]:


#facts()


# In[6]:


def mars_img(browser):
    browser.visit("https://marshemispheres.com/")
    image_store=[]
    for i in range(4):
        temp={}
        browser.find_by_css("a.product-item img")[i].click()
        raw_url=browser.find_by_text("Sample").first
        temp["url"]=raw_url["href"]
        temp["title"]=browser.find_by_css("h2.title").text
        image_store.append(temp)
        browser.back()
    return image_store


# In[ ]:


#scrape_info()


# In[ ]:





# In[ ]:





# In[ ]:




