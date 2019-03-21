from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")

soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section", "section chart-grid")

ul = section.div.ul
list_li = ul.find_all("li")
new_div = []

for i in range(len(list_li)):
    li = list_li[i]
    h3 = li.h3.a
    h4 = li.h4.a
    namesong = h3.string
    artis = h4.string
    
    dict_song = OrderedDict({
    "namesong": namesong,
    "artis": artis.lstrip().rstrip(),
    })
    new_div.append(dict_song)

for dict_song in new_div:
    name = dict_song["namesong"]
    art = dict_song["artis"]
    options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio' 
}  
    dl = YoutubeDL(options)
    dl.download([name])


# pyexcel.save_as(records=new_div,dest_file_name="topsong.xlsx")




