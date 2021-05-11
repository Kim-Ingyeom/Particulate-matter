import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://ewp.co.kr/kor/subpage/contents.asp?cn=K5VCI0HG&ln=NW3SBGVH&sb=9V62CFIE&tb=YXCJEDX&taborder',verify=False)
soup = BeautifulSoup(page.content,'html.parser')

table = soup.find_all('td')
ap = []
pm = []#미세먼지
upm = []#초 미세먼지
co = []#일산화 탄소
o3 = []#오존
for i in table[2:]:
    ap.append(i.text)
print(ap)
for i in ap:
    if ap.index(i)%7 == 1:
        pm.append(i)
    if ap.index(i)%7 == 2:
        upm.append(i)
    if ap.index(i)%7 == 4:
        co.append(i)
    if ap.index(i)%7 == 6:
        o3.append(i)
print('당진, 일산, 동해바이오, 울산, 호남')
print(pm)
print(upm)
print(co)
print(o3)





