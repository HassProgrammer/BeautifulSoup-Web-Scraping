from bs4 import BeautifulSoup

with open("./02-Learning-WsC-Web_scraping./03-index.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    find_all_h5_tags = soup.find_all('h5')
    print(find_all_h5_tags)