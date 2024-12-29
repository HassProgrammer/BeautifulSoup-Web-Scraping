from bs4 import BeautifulSoup
with open("./02-Learning-WsC-Web_scraping./03-index.html", "r") as html_file:
    content = html_file.read() 
    soup = BeautifulSoup(content, "lxml")
    courses = soup.find_all("div", class_ = "card")

    for course in courses:
        course_name = course.find("h5").text.split()[-1]
        course_price = course.find("a").text.split()[-1]
    
        print(f'{course_name}, {course_price}')