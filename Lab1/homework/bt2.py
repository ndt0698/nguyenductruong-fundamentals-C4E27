from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict


url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.cnn"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")
soup = BeautifulSoup(html_content,"html.parser")
tables = soup.find("table",id="tableContent")

tr_list = tables.find_all("tr")

new_dict = []

for tr in tr_list:
    td_list = tr.find_all("td")
    dict_cf = {}
    for j in range(len(td_list)):
         if td_list[j].string != None:
            if j ==0:
                dict_cf["danh muc"]=td_list[j].string.strip()
            elif j ==1:
                dict_cf["quy 4 nam 2016"]=td_list[j].string.strip()
            elif j ==2:
                dict_cf["quy 1 nam 2017"]=td_list[j].string.strip()
            elif j ==3:
                dict_cf["quy 2 nam 2017"]=td_list[j].string.strip()
            elif j ==4:
                dict_cf["quy 3 nam 2017"]=td_list[j].string.strip()
    if dict_cf != {}:
        new_dict.append(dict_cf)
pyexcel.save_as(records=new_dict, dest_file_name="baocao.xlsx")