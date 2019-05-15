from bs4 import BeautifulSoup

import urllib
from urllib.request import Request, urlopen



def searchEntity(name):
    """Searches the name entity in google search     
    Extract the knowledge panel if present from Google Search Page

    Args:
        name: Name or entity to be search 

    Returns:
        Logo, Company Name, description, and other details   

    """ 
    name = urllib.parse.quote_plus(name)
    url = "https://www.google.com/search?q={}&oq={}".format(name,name)
    #print(url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})

    html = urlopen(req).read().decode('utf-8', 'ignore')
    #print(html)
    soup = BeautifulSoup(html, "html.parser")
    
    #divs = soup.select('div[class*="knowledge-panel"]')
    

    divs = soup.find_all('div',class_="knowledge-panel")

    if(len(divs) > 0):
        
        html = divs[0].select("div[class*=kno-fb-ctx]")
        other = []
        ctype = ""
        desc= ""
        comp = ""
        logo = ""
        for div in html:
            if len(div.select('img[src]')) > 0:
                img =  div.select('img[src]')[0]
                logo = img['src']
            
            if 'kno-ecr-pt' in  div['class']:
                comp = div.text.replace(">","")
            if 'wwUB2c' in  div['class']:
                ctype = div.text.replace(">","")        
            if 'hb8SAc' in  div['class']:
                desc = div.text.replace(">","")  
            
            if 'zloOqf' in  div['class']:
                d = div.text.replace(">","")
                other.append(d)     

        return {'logo':logo,'comp':comp,'type':ctype,'desc':desc,'other':other}
