from bs4 import BeautifulSoup
import requests

#Our target find few days ago jobs
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=')

# status_code is for find status code
# print(html_text.status_code)

#if we want to find text
# print(html_text.text)

soup = BeautifulSoup(html_text, "lxml") 
jobs = soup.find("span", class_="sim-posted")
print(jobs)