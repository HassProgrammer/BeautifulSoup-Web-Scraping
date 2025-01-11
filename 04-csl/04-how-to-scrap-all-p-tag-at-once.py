import bs4

html_file = open("./04-csl./example.html")
soup = bs4.BeautifulSoup(html_file, "html.parser")
select_all_p_tag = soup.select("p")
print(select_all_p_tag) 
for i in select_all_p_tag:
    print(i.getText())

# for i in range(10):
#     print(i)
#     for j in select_all_p_tag:
#         print(j.getText())

