import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"    
  
def loadRSS():
    resp = requests.get(RSS_FEED_URL) 
    return resp.content

def parseXML(rss):
    
    root = ET.fromstring(rss)  
    newsitems = []
    for item in root.findall('./channel/item'): 
        news = {} 
  
        # iterate child elements of item 
        for child in item: 
  
            # special checking for namespace object content:media 
            if child.tag == '{http://search.yahoo.com/mrss/}content': 
                news['media'] = child.attrib['url'] 
            else: 
                news[child.tag] = child.text.encode('utf8') 
        newsitems.append(news) 
  
    # return news items list 
    return newsitems 

def topStories(): 
    ''' 
    main function to generate and return news items 
    '''
    # load rss feed 
    rss = loadRSS() 
  
    # parse XML 
    newsitems = parseXML(rss) 
    return newsitems 