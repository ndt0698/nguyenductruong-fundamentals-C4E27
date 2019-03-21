from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict


#1. Tạo một kết nối ( Create conection)
url = "https://dantri.com.vn/"
conn = urlopen(url)

#1.1 Download page
raw_data = conn.read()
html_content = raw_data.decode("utf-8")
with open("dantri.html", "wb") as f:
    f.write(raw_data)

# #2. tìm ROI (find ROI)
# soup =  BeautifulSoup(html_content,"html.parser")
# ul = soup.find("ul","ul1 ulnew")




# #3. phân giải ROI (extract ROI)

# li_list = ul.find_all("li")
# new_dict =[]

# for i in range(len(li_list)):

#     li = li_list[i]
#     h4 = li.h4
#     a = h4.a

#     title = a.string
#     link = url + a["href"]

#     dict_title = OrderedDict ({
#     "Title": title.lstrip().rstrip(),
#     "link": link,
#     } )
#     new_dict.append(dict_title)
    
   

# #4.Save data
# pyexcel.save_as(records=new_dict,dest_file_name="dantri.xlsx")