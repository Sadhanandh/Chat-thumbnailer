from lxml.html import fromstring
import requests
import re
from urlparse import urljoin
from readability import Document

def postme(text):
    img = None
    urls = re.findall("https?://\S+",text,re.I)
    if len(urls)>0:
    	link = urls[0] # as of now im parsing just the first url
        req = requests.get(link)
        source = req.text
        htmltree = fromstring(source)
        elems = htmltree.cssselect("img") # this can be done by data = re.findall("img\s*=\s*(\S+)") and re.sub("'|\"","",data)
        for elem in elems[:1]:
            img = elem.attrib["src"]
            img = urljoin(link,img)
        if (img!=None):
            return "<span>%s</span><br /><img src=%s></img>"%(text,img)

    return text

def postreadability(text):
    img = "None"
    urls = re.findall("https?://\S+",text,re.I)
    if len(urls)>0:
    	link = urls[0] # as of now im parsing just the first url
        req = requests.get(link)
        source = req.text
        try:
			readable_article = Document(source).summary()
			htmltree = fromstring(readable_article.html)
        except Exception :
			return text

        elems = htmltree.cssselect("img") # this can be done by data = re.findall("img\s*=\s*(\S+)") and re.sub("'|\"","",data)
        for elem in elems[:1]:
            img = elem.attrib["src"]
            img = urljoin(link,img)
        if (img!=None):
            return "<span>%s</span><br /><img src=%s></img>"%(text,img)
    return text
