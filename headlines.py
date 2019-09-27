import sys
import feedparser
import pandas as pd
from datetime import datetime
from dateutil.parser import parse

def main():
    # url = "http://feeds.reuters.com/Reuters/worldNews"
    # url = "http://feeds.reuters.com/Reuters/PoliticsNews"
    #url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    #url = "http://www.marketwatch.com/rss/topstories"
    #url = "http://feeds.marketwatch.com/marketwatch/bulletins"
    #url = "https://www.economist.com/china/rss.xml"
    #url = "https://www.economist.com/international/rss.xml"

    #pd.options.display.width = 0
    pd.set_option('display.max_colwidth', -1)

    sources = [
        {
            'code'    : 'ECON',
            'url'       : "https://www.economist.com/finance-and-economics/rss.xml"
        },
        {
            'code'    : 'MWATCH',
            'url'       : "http://www.marketwatch.com/rss/realtimeheadlines"
        },
        {
            'code'    : 'REUTERS',
            'url'     : "http://feeds.reuters.com/reuters/companyNews"
        },
        {
            'code'    : 'REUTERS',
            'url'     : "http://feeds.reuters.com/reuters/businessNews"
        },
        {
            'code'    : 'REUTERS',
            'url'     : "http://feeds.reuters.com/reuters/topstories"
        },
        {
            'code'    : 'NOLA',
            'url'     : "https://www.theadvocate.com/search/?q=&t=article&l=35&d=&d1=&d2=&s=start_time&sd=desc&c%5b%20%5d=new_orleans/news*,baton_rouge/news/politics/legislature,baton_rouge/news/politics,new_orleans/opinion*,baton_rouge/opinion/stephanie_grace,baton_rouge/opinion/jeff_sadow,ba%20ton_rouge/opinion/mark_ballard,new_orleans/sports*,baton_rouge/sports/lsu&nk=%23tncen&f=rss"
        },
        {
            'code'    : 'NOLA',
            'url'     : "https://www.theadvocate.com/search/?q=&t=article&l=35&d=&d1=&d2=&s=start_time&sd=desc&c%5b%5d=new_orleans/news/business&nk=%20%23tncen&f=rss"
        },
        {
            'code'    : 'NOLA',
            'url'     : "https://www.theadvocate.com/search/?q=&t=article&l=35&d=&d1=&d2=&s=start_time&sd=desc&c%5b%5d=new_orleans/sports/saints&nk=%23tncen&f=rss"
        },
        {
            'code'    : 'TECHCRUNCH',
            'url'     : "http://feeds.feedburner.com/TechCrunch/"
        },
        {
            'code'    : 'RT',
            'url'     : "https://www.rt.com/rss/business/"
        },
        {
            'code'    : 'RT',
            'url'     : "https://www.rt.com/rss/news/"
        },
        {
            'code'    : 'RT',
            'url'     : "https://www.rt.com/rss/usa/"
        },
        {
            'code'    : 'RT',
            'url'     : "https://www.rt.com/rss/uk/"
        },
        {
            'code'    : 'ALPHA',
            'url'     : "https://seekingalpha.com/feed.xml"
        },
        {
            'code'    : 'MOTLEY',
            'url'     : "http://www.fool.ca/feed/"
        },
        {
            'code'    : 'CNBC',
            'url'     : "http://www.cnbc.com/id/20409666/device/rss/rss.html?x=1"
        },
        {
            'code'    : 'BBC',
            'url'     : "http://feeds.bbci.co.uk/news/rss.xml"
        },
        {
            'code'    : 'BBC',
            'url'     : "http://feeds.bbci.co.uk/news/world/rss.xml"
        },
        {
            'code'    : 'BBC',
            'url'     : "hhttp://feeds.bbci.co.uk/news/business/rss.xml"
        },
        {
            'code'    : 'BBC',
            'url'     : "http://feeds.bbci.co.uk/news/technology/rss.xml"
        },
        {
            'code'    : 'DOD',
            'url'     : "https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?max=10&ContentType=1&Site=945"
        },
        {
            'code'    : 'FINTIMES',
            'url'     : "https://www.ft.com/global-economy?format=rss"
        },
        {
            'code'    : 'SKIFT',
            'url'     : "https://skift.com/feed/"
        },
        {
            'code'    : 'HACKER',
            'url'     : "https://hnrss.org/frontpage"
        },
        {
            'code'    : 'NYTIMES',
            'url'     : "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
        },
        {
            'code'    : 'NYTIMES',
            'url'     : "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
        },
        {
            'code'    : 'NYTIMES',
            'url'     : "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
        },
        {
            'code'    : 'NYTIMES',
            'url'     : "https://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml"
        },
        {
            'code'    : 'NYTIMES',
            'url'     : "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml"
        },
        {
            'code'    : 'NYTIMES',
            'url'     : "https://rss.nytimes.com/services/xml/rss/nyt/US.xml"
        },
        {
            'code'    : 'PYMNTS',
            'url'     : "https://www.pymnts.com/feed/"
        },
        {
            'code'    : 'FINEXTRA',
            'url'     : "https://www.finextra.com/rss/headlines.aspx/?x=1"
        },
        {
            'code'    : 'WSJ',
            'url'     : "https://feeds.a.dj.com/rss/RSSWorldNews.xml"
        },
        {
            'code'    : 'WSJ',
            'url'     : "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml"
        },
        {
            'code'    : 'WSJ',
            'url'     : "https://feeds.a.dj.com/rss/RSSMarketsMain.xml"
        },
        {
            'code'    : 'WSJ',
            'url'     : "https://feeds.a.dj.com/rss/RSSWSJD.xml"
        }
    ]




    framelist = []
    for source in sources:
        code = source['code']
        url = source['url']
        NewsFeed = feedparser.parse(url)
        numEntries = len(NewsFeed.entries)

        for entry in NewsFeed.entries:
            #date = datetime.strptime(entry.published, '%d-%m-%Y')
            date = entry.published
            row = { 'headline' : entry.title,
                        'link' : entry.link, 'date' : date, 'source' : code,
            }
            #print(row)
            framelist.append(row)

    frame = pd.DataFrame(framelist)
    frame['date'] = pd.to_datetime(frame['date'])
    #print(type(frame['date']))


    sortFrame = frame.sort_values(by='date', ascending=False)

    # set the order of the columns
    sortFrame = sortFrame[['date', 'source', 'headline', 'link']]

    # determine the headline with most characters
    #maxHeadline = len(sortFrame['headline'].max())

    pageSize = 15
    rowCount = 0
    for index, row in sortFrame.iterrows():
        if(rowCount == pageSize):
            rowCount = 0
            command = input(":")
        else:
            date     = row['date'].strftime("%Y-%m-%d %H:%M").ljust(10)
            headline = row['headline'].ljust(130)
            source   = row['source'].ljust(15)
            print(date, ' ', source, ' ', headline, ' ', row['link'])
            rowCount = rowCount + 1

if __name__ == "__main__":
    main()
