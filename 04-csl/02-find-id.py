import bs4

html_open = open("./04-csl./example.html")

html_bs4 = bs4.BeautifulSoup(html_open, "html.parser")

find_id = html_bs4.select('#author')
print(find_id)
one_tag = find_id[0]
print(f"The Text is: {one_tag.getText()}")