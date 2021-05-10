import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://ewp.co.kr/kor/subpage/contents.asp?cn=K5VCI0HG&ln=NW3SBGVH&sb=9V62CFIE&tb=YXCJEDX&taborder',verify=False)
soup = BeautifulSoup(page.content,'html.parser')

table = soup.find_all('td')
ap = []
for i in table[2:]:
    ap.append(i.text)
print(ap)







