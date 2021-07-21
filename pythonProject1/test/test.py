from bs4 import BeautifulSoup
import requests
url = "http://siamchart.com/stock/"

res = requests.get(url)
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')

a = soup.find('div',id="table_data")
courses = soup.find_all('table',class_="tbl")
course_list = []

for course in courses:
    # Create a new variable --> obj to store
    # only course name getting rid of unwanted tags
    obj = course.string

    # Append each course into a course_list variable
    course_list.append(obj)
    print(course_list)