import bs4 

html_open = open("./04-csl./example.html")

html_bs4 = bs4.BeautifulSoup(html_open, "html.parser")
# print(type(html_bs4))
div_tag = html_bs4.select("div")
print(div_tag)
# Printing first div
print(div_tag[0])