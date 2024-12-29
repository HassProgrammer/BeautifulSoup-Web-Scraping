from bs4 import BeautifulSoup

with open("./02-Learning-WsC-Web_scraping./03-index.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    course = soup.find_all("div", class_= "card")
    for courses in course:
        course_name = courses.find("h5").text
        course_price = courses.find("a").text

        print(f'{course_name}, {course_price}')


# With error handling
print("\n______________________________\n")

with open("./02-Learning-WsC-Web_scraping./03-index.html", "r") as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, "lxml")


courses = soup.find_all("div", class_="card")  

for course in courses:
    try:
        course_name = course.find("h5").text.strip()
        course_price = course.find("a").text.strip()

        print(f"{course_name}, {course_price}")
    except AttributeError:
        print("Error: Course information not found in this card.")
