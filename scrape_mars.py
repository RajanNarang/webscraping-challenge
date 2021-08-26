from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
def news_scrape(browser):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit("https://redplanetscience.com/")
    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find(class_="content_title").text
    news_p = soup.find(class_="article_teaser_body").text
    return news_title, news_p

def image_scrape(browser):
    browser.visit("https://spaceimages-mars.com/")
    browser.find_by_tag("button")[1].click()
    html = browser.html
    space_image_soup = bs(html, 'html.parser')
    image_link = space_image_soup.find('img', class_ = 'fancybox-image').get('src')
    featured_image_url = "https://spaceimages-mars.com/" + image_link
    return featured_image_url

def facts_scrape(browser):
    mars_df = pd.read_html('https://galaxyfacts-mars.com')[0]
    mars_df.set_index(0)
    return mars_df.to_html()

def mars_scrape(browser):
    browser.visit('https://marshemispheres.com/')
    hemisphere_image_urls = []
    counter = 0
    while counter < len(images):
        my_dict = {"title" : None , "img_url" : None}
        browser.find_by_css("img.thumb")[counter].click()
        title = browser.find_by_css("h2.title").text
        img_url = browser.links.find_by_text("Sample").first["href"]
        my_dict['title'] = title
        my_dict['img_url'] = img_url
    
        hemisphere_image_urls.append(my_dict)
    
        counter = counter + 1
        browser.back()
    return hemisphere_image_urls



