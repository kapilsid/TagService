from bs4 import BeautifulSoup

from urllib.request import Request, urlopen

req = Request('https://www.google.com/search?q=American+Hospital+Supply&oq=American+Hospital+Supply', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})

html = urlopen(req).read()


soup = BeautifulSoup(html, "html.parser", from_encoding="utf8")

#divs = soup.find_all('div', attrs={'class': 'kp-blk knowledge-panel'})

#divs = soup.find_all("div", class=lambda value: value and value.startswith("kp-blk"))

#print(soup.div)

divs = soup.select("div[class*=knowledge-panel]")
print(divs)

f = open("demofile2.html", "w", encoding="utf8")
f.write(str(soup.prettify()))
f.close()


html = divs[0].select("div[class*=kno-fb-ctx]")

#for div in html:
#    print(div.text)

#img = html[0].find("div[class*=img-kc-m]")r = 
other = []
for div in html:
    if len(div.select('img[title]')) > 0:
        img =  div.select('img[title]')[0]
        logo = img['title']
    
    if 'kno-ecr-pt' in  div['class']:
        comp = div.text
    if 'wwUB2c' in  div['class']:
        ctype = div.text        
    if 'hb8SAc' in  div['class']:
        desc = div.text  
    
    if 'zloOqf' in  div['class']:
        other.append(div.text)     


# for div in html:
#     print(div['class'])
#     print(div.text)
# print(logo)
# print(comp)
# print(ctype)
# print(desc)
# print(other)


# element = so
# up.select('div.kp-blk')

# print(element)

# for div in soup.find_all('div', {'class':'knowledge-panel'}):
#     print(div)