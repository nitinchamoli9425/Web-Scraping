from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql

url = 'https://www.semalytix.com/team/'

#open the connection and downloads the webpage
download = urlopen(url)

html = download.read()
download.close()

page_soup = BeautifulSoup(html,"html.parser")
Team_Members = page_soup.findAll("div",{"class":"team-member"})

'''
#creating a CSV file
filename = "EmployeeDetails.csv"
f = open(filename,"w")
headers = "Employee Name, Employee Role\n"
f.write(headers)
'''

login_info = open('Login.txt')
login_info = login_info.read()
login_info = login_info.split()
#conn = mysql.connector.connect(host=login_info[0], user=login_info[1], passwd=login_info[2], db=login_info[3])
#conn = pymysql.connect("localhost", "root", "Paderborn@9425", "sakila")
#cursor = conn.connect()

conn = pymysql.connect(host=login_info[0], user=login_info[1], passwd=login_info[2], db=login_info[3])
cur = conn.cursor()

#roll_back = "delete from employee"
#cur.execute(roll_back)

for i in range(0,len(Team_Members)):

    EmployeeName = Team_Members[i].figcaption.h5.string
    EmployeeRole = Team_Members[i].figcaption.span.string


    query = "INSERT INTO employee (employee_name, employee_role) VALUES (%s,%s)"
    val = (EmployeeName, EmployeeRole)
    cur.execute(query, val)
    conn.commit()

fet = "select * from employee"
cur.execute(fet)
row = cur.fetchall()
print(row)

cur.close()
conn.close()

'''
host = login_info[0]
user = login_info[1]
passwd = login_info[2]
db = login_info[3]
'''






