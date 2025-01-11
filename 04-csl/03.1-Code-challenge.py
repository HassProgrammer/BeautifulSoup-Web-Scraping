# code challenge: Scrape from second .mobile class while those name are same 
import bs4

html_file_open = open("./04-csl./example.html")
soup = bs4.BeautifulSoup(html_file_open, "html.parser")

select_class = soup.select(".mobile")
the_class_i_want = select_class[1]
print(the_class_i_want)
print(f"Your phone number: {the_class_i_want.getText()}")