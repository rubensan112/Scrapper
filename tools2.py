import urllib2
from lxml import cssselect, etree
import re
import json
import sys

def loopload(tag,webContent,link,max_iter=100):
    linklist=[]
    select = cssselect.CSSSelector(tag)
    root = etree.HTML(webContent)
    result = select(root)
    link1 = re.search('(.+?.com)', link, re.S)
    host = link1.group(0)
    for k in result:
        linklist.append((host + k.attrib["href"]))
    return linklist