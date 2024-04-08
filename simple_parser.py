#!/usr/bin/env python.3.11.5

import re
from urllib.request import urlopen
import csv

url = 'https://www.djintelligence.com/pages/mobilebeatprint.asp'
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('iso-8859-1')

td = re.findall("<td.*?>(.+?)</td>", html)
new_td = td[3:]
lst = []
for i in range(len(new_td)):
    if (len(new_td[i]) == 0):
        continue
    td_value = re.findall("<font[^>]*>(.*?)</font>", new_td[i])
    lst.append(td_value[0])
    
if (len(lst)) > 0:
    out = [lst[k:k+3] for k in range(0, len(lst), 3)]

    for i in range(len(out)):
        out[i][0] = re.findall("<b>(.*)</b>", out[i][0])[0]

    with open('./test.csv', 'w', newline="\n") as myfile:
        wr = csv.writer(myfile)
        wr.writerows(out)
else:
    print(html)
    




