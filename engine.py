# -*- coding:utf-8 -*-


__author__ = "Hongwing"

"""
百度云资源搜索
"""

from HTMLParser import HTMLParser 
from bs4 import BeautifulSoup
#import bs4.builder.htmlparser
#import bs4.builder._lxml
#import bs4.builder._html5lib
import xml
import requests
import sys
import urllib
import urllib2
import cookielib
reload(sys)
sys.setdefaultencoding('utf-8')


 
class MyHTMLParser(HTMLParser):  
    def __init__(self):   
        HTMLParser.__init__(self)   
        self.links = []
        self.linkContents = []
        self.source = {}   
        self.div_text = False
        self.item = 0;


    def handle_starttag(self, tag, attrs):   
        #print "Encountered the beginning of a %s tag" % tag   
        if tag == "a":   
            if len(attrs) == 0:   
                pass   
            else:   
            	if attrs.__contains__(('class', 'cse-search-result_content_item_top_a')):
            		for (variable, value) in attrs:
            			if variable == "href":
          					self.links.append(value)

        if tag == "div" and attrs.__contains__(('class', 'cse-search-result_content_item_mid')):
        	self.div_text = True


    def handle_endtag(self, tag):
    	if tag == "div" :
    		self.div_text = False

    def handle_data(self, data):
    	if self.div_text:
    		string = data;
    		self.linkContents.append(string);
    		#print self.links;
    		#self.source[self.links[self.item+=1]]= data;
    		#self.item += 1;
    		#self.linkContents.append(data)
    		#for i in range(len(data)):
    		#	self.linkContents.append(data[i])


class BDClound(object):
	"""docstring for BDClound"""
	def __init__(self):
		self.url = "http://www.wangpansou.cn/s.php?";
		self.getData = {}
		self.header = {}   
		self.html = ""
		self.key = ""     
		#elf.cookies = cookielib.CookieJar();
        #self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies));
    

	def PanSearch(self, key):
		self.header = urllib.urlencode({
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
			'Connection':'keep-alive',
			'Cookie':'uuid=ehabpzfr; _ga=GA1.2.209853326.1469412181; _gat=1; Hm_lvt_311044e7f31d9fd867541074b4ba8cfd=1469412182; Hm_lpvt_311044e7f31d9fd867541074b4ba8cfd=1469412182; BAIDU_SSP_lcr=https://www.baidu.com/link?url=o8B163U-wBwCu3-ggVLXwkdv_5vJ9HI5OgE3UXcBt9L0jlFZX1WxTGERsA-jD0Ya&wd=&eqid=c9c4ca9c0031ce59000000025795735c',
			'Host':'www.wangpansou.cn',
			'Referer':'http://www.wangpansou.cn/',
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
			});
		self.getData = urllib.urlencode({
			"wp": "0",
			"op": "gn",
			"ty": "gn",
			"q": key,
			"q": key
			});		
		# request = urllib2.Request(self.url+self.getData, None, self.header);
		# result = self.opener.open(request);
		# result = urllib2.urlopen(request);
		html = requests.get(self.url+self.getData);
		self.html = html;
		self.key = key;
		print html
		#print html.text
		with open("/Users/lister/PythonProjects/result.html", "w") as fp:
			fp.write(html.text)
		print "==> Done"

	def HTMLProcess(self):
		hp = MyHTMLParser();
		hp.feed(self.html.text)
		hp.close()
		print len(hp.links)
		print len(hp.linkContents)
		#print hp.source[hp.links[1]]
		#print hp.source.keys()
		for i in range(len(hp.links)):
			print "=============================================================="
			print "资源名称: " + hp.linkContents[i]
			print (self.key + ' 资源链接==》%d  ' % (i+1)) + hp.links[i]
		#soup = BeautifulSoup(self.html, 'html.parser')
		#src_url = soup.find_all('a', {'class': 'cse-search-result_content_item_top_a'})
		#src_info = soup.find_all('div', {'class':'cse-search-result_content_item_mid'})
		#print (src_url)
		   
    

if __name__ == '__main__':
	bdy = BDClound();
	print "================Baidu 云盘 搜索神器 Hongwing==============="
    #print "======                  开始搜索                     ======"
	key = raw_input("==========输入你的关键字: ");
	bdy.PanSearch(key);
	bdy.HTMLProcess();