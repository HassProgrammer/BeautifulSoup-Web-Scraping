from bs4 import BeautifulSoup

with open('03-index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    print(soup.prettify())