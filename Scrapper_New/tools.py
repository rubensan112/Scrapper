import urllib2
from lxml import cssselect, etree
import re
import json
import sys
from yapf.yapflib.yapf_api import FormatCode
import autopep8
import unicodedata
import collections
import urllib
import httplib

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data



def split_and_load(url):
    try :
        response = urllib2.urlopen(url)
        webContent = response.read()
        return webContent
    except:
        sys.exit("No url entry")
def split_and_load1(self):
    if self["load_type"] == "get":
        try :
            response = urllib2.urlopen(self)
            webContent = response.read()
            return webContent
        except:
            sys.exit("No url entry")
    if self["load_type"] == "post":
        try:
            params = urllib.urlencode(self["params"]) #Pasa de las keys, a un string encodeado para 'raw'
            headers = self["headers"]
            match = (re.search("https://(.+)", self["page"], re.S)).group(1)
            conn = httplib.HTTPConnection("bugs.python.org")
            conn.request("POST", "", params, headers)
            response = conn.getresponse()
            data = response.read()
            return data
        except:
            sys.exit("No url entry")





def extract(tag,regex,type,link,webContent):
    if type == "text":
        try:
            select = cssselect.CSSSelector(tag)
            root = etree.HTML(webContent)
            result = select(root)
            result2 = result[0].text
            if regex == "":
                match2 = result2
                return match2
            else:
                try:
                    match = re.search(regex, result2, re.S)  # importante activar s flag
                    try:
                        match2 = match.group(0)
                        return match2
                    except:
                        print("No groups found")
                except:
                    print("No regex entry")


        except:
            print('No tags found')
    if type == "attribute":
        select = cssselect.CSSSelector(tag)
        root = etree.HTML(webContent)
        result = select(root)
        link1=re.search('(.+?.com)',link,re.S)
        host=link1.group(0)
        result2 = (host +result[0].attrib["href"])
        return result2
def create_dict(nombre, link=None):
    f = open('event.json', 'w')  # w sobreescribir
    dict1=json.dumps(nombre)
    f.write(dict1)
    f.close

def create_dict1(nombre, link=None):
    f = open('event.json', 'w')  # w sobreescribir
    dict1=json.dumps(nombre)
    dict2=dict1.strip()
    f.write(dict2)
    f.close
'''
Esto son pruebas para enteneder como funciona todo

{ _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
    for key, value in dict.iteritems()}

def _byteify1(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return (data + "fin")
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify1(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify1(key, ignore_dicts=True): _byteify1(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def _byteify2(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, bool):
        return str(data)
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify2(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify2(key, ignore_dicts=True): _byteify2(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form Falta el return data

'''