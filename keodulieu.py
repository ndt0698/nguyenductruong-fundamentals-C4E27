from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url ="https://ahacafe.vn/#location"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")
with open("aha.html","wb") as f:
    f.write(raw_data)

soup = BeautifulSoup(html_content,"html.parser")
ul = soup.find("ul","ul1 ulnew")

aha_list = ul.find_all("li")
new_ahacafe = []

for i in range(len(li_list)):
    li= li_list[i]
    