
import feedparser
news_feed = feedparser.parse('https://www.cert.ssi.gouv.fr/alerte/feed/')
print(news_feed.feed.keys())
print("Feed Title:", news_feed.feed.title) 
print("Feed Subtitle:", news_feed.feed.subtitle)
print("Feed Link:", news_feed.feed.link, "\n")
print(news_feed.entries[0].keys())

for entry in news_feed.entries:
    print(f"{entry.title} --> {entry.link}")
    for i in range(0, len(news_feed.entries)):
    if i == (len(news_feed.entries)-1):
        print("Alert: {} \nLink: {}".format(news_feed.entries[0]['title'], news_feed.entries[0]['id']))