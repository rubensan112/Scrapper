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
import copy
import tools
from cssselect import GenericTranslator, SelectorError
import StringIO
from lxml.etree import fromstring
"""
def split_and_load(param):
    if param["http_method"] == "get":
        try :
            response = urllib2.urlopen(param["url"])
            webContent = response.read()
            return webContent
        except:
            sys.exit("No url entry")
    if param["http_method"] == "post":
        try:
            params = urllib.urlencode(param["params"]) #Pasa de las keys, a un string encodeado para 'raw'
            try:
                headers = param["headers"]
                match = (re.search("https://(.+)", param["page"], re.S)).group(1)
                conn = httplib.HTTPConnection("bugs.python.org")
                conn.request("POST", "", params, headers)
                response = conn.getresponse()
                data = response.read()
                return data
            except:
                sys.exit("No url entry")
        except:
            sys.exit("No params")
"""
def del_step(config, steps):
    position_in_list = [i for i in range(len(steps)) if steps[i]["guid"] == config["guid"]]
    config["feed"]["steps"].pop(position_in_list[0])
    return config




class Start(object):
    def __init__(self,config,browser):
        self.feed = config
        self.iter = 0
    def execute(self,step):
        self.iter += 1
        return "Nothing"

class LoadPage(object):
    def __init__(self,config,browser):
        self.iter = 0
        self.config = config
        self.browser = browser

    def execute(self,step):

        def split_and_load(param):
            if param["http_method"] == "get":
                try:
                    response = urllib2.urlopen(param["url"]) #En el curro utilizan urllib.request
                    webContent = response.read()
                    return webContent
                except:
                    sys.exit("No url entry")
            if param["http_method"] == "post":
                try:
                    params = urllib.urlencode(param["params"])  # Pasa de las keys, a un string encodeado para 'raw'
                    try:
                        headers = param["headers"]
                        match = (re.search("https://(.+)", param["page"], re.S)).group(1)
                        conn = httplib.HTTPConnection("bugs.python.org")
                        conn.request("POST", "", params, headers)
                        response = conn.getresponse()
                        data = response.read()
                        return data
                    except:
                        sys.exit("No url entry")
                except:
                    sys.exit("No params")

        print("-------------------Executing %s -------------------" % (step["name"]))

        param = step["param"]
        browser = split_and_load(param)
        return browser

class Loop(object):
    def __init__(self,config,browser):
        self.feed = config["feed"]
        self.feed_copy = copy.deepcopy(config["feed"])
        self.browser_copy = copy.deepcopy(browser)
        self.iter = 0
    def execute(self,step):
        param = step['param']

        print("-------------------Executing %s -------------------" % (step["name"]))
        if self.iter == 0:
            next_guid = step['next_guids']
            browser_copy = self.browser_copy
            feed_copy = self.feed_copy
        #if param['path']:

        result = [browser_copy, feed_copy, next_guid]

        return result

class End(object):
    def __init__(self,config,browser):
        self.feed = config
    def execute(self,step):
        return "Nothing"








class Extract(object):
    def __init__(self, config, browser):
        self.iter = 0
        self.config = config
        self.browser = browser
    def execute(self, step):
        param = step['param']
        try:
            expression = GenericTranslator().css_to_xpath(param['path'])
        except SelectorError:
            print('Invalid selector')
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO.StringIO(self.browser), parser)
        #result = [e.get('href', 'None')for e in tree.xpath(expression)]
        if param['path_extract_type'] == "plain_text":
            result = [node.text for node in tree.xpath(expression)]
        if param['path_extract_type'] == "attribute":
            result = [node.get('param.path_extract_ref') for node in tree.xpath(expression)]
        result = tools._byteify(result[0])
        print(result)
        return result

class iter(object):
    def __init__(self,config,var):
        self.iter = 0
        self.config = config
        self.var = var

    def execute(self,config,browser):

        return browser



