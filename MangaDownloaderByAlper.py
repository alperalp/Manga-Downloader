from art import *
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
import urllib.request

from selenium import webdriver

tprint("Manga Downloader by Alper")

browser = input("Select your browser(Chrome/c,Firefox/f) :")

if browser == "f":
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.headless = True
    options.add_argument('log-level=3')
    driver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")
elif browser == "c":
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('log-level=3')  
    
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

    

main_pageUrl = input("Give main page of manga from !MANGEMELON! :")
driver.get(main_pageUrl)

main_page = driver.page_source

manga_name = main_pageUrl.split("manga/")[1]

soup = BeautifulSoup(main_page, 'html.parser')

chapter_name = []
chapter_rawlink = []
chapter_link = []
chapters = soup.findAll("a",{"class":"uk-link-text ccc"})



for chapter in chapters:
    chapter_name.append(chapter["data-slug"])
    chapter_rawlink.append(chapter["href"])
chapter_name.reverse()
chapter_rawlink.reverse()

for link in chapter_rawlink:
    chapter_link.append(f"https://mangamelon.com{link}")



gap = input(f"There are {len(chapters)} parts. Whic parts do you want to download(1-{len(chapters)}): ")

gap = gap.split("-")
gap[0] = str(int(gap[0])-1)
gap[1] = str(int(gap[1])-1)


sec_chap = []
for link in chapter_link:
    if(chapter_link.index(link) >= int(gap[0]) and chapter_link.index(link) <= int(gap[1])):
        sec_chap.append(link)

print(os.getcwd())

main_directory = manga_name
  
    
main_dir = os.getcwd()

main_path = os.path.join(main_dir, main_directory) 
 
os.mkdir(main_path)

for link in sec_chap:
    directory = chapter_name[chapter_link.index(link)]
   
    parent_dir = f"{os.getcwd()}\{manga_name}"

    path = os.path.join(parent_dir, directory) 


    os.mkdir(path)
    driver.get(link)
    link_page = driver.page_source
    soup = BeautifulSoup(link_page,'html.parser')
    images = soup.findAll("img",{"class":"uk-width-1-1 uk-width-2-3@m uk-width-3-5@l vpage"})
    img_link = []              
    for img in images:
        
            urllib.request.urlretrieve(img["data-src"],(f'{parent_dir}\{chapter_name[chapter_link.index(link)]}\{images.index(img)}.jpg'))
            print(img["data-src"])
driver.close()