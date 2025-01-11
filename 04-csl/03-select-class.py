import bs4

html_file = open("./04-csl./example.html")

soup = bs4.BeautifulSoup(html_file, "html.parser")

html_class_select = soup.select(".mobile")
print(html_class_select)
one_class = html_class_select[0]
print(f"The phone number is: {one_class.getText()} from .mobile class.")