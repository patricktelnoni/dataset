import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Chrome()
url = u"https://twitter.com/search?q=lockdown%20since%3A2020-03-02%20until%3A2020-03-03%20lang%3Aid%20exclude%3Alinks"

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

# html = browser.page_source
tweets = browser.find_element_by_css_selector('article')

# soup = BeautifulSoup(html,"html.parser")
# print(soup)
# tweets = soup.find_all("article")
# tweets = soup.findAll("div", {"data-testid": "tweet"})
# tweets = soup.find("div", attrs={"data-testid":True}).text
# print(tweets)
for tweet in tweets:
    print(tweet.text)

# file = "lockdown.csv"
# f = open(file, "w+")
# Headers = "tweet_user, tweet_text,  replies,  retweets\n"
# f.write(Headers)
# # q = "lockdown since:2020-03-02 until:2020-03-03 lang:id exclude:links"
# # url = "https://twitter.com/search?q={keyword}".format(keyword=q)
# url = "https://twitter.com/search?q=lockdown%20since%3A2020-03-02%20until%3A2020-03-03%20lang%3Aid%20exclude%3Alinks"
# print(url)
# html = urlopen(url)

# soup = BeautifulSoup(html,"html.parser")
# print(soup)
# tweets = soup.find_all("article")
# for tweet in tweets:
#     print(tweet)
#     try:
#         if tweet.find('div', {"class":"css-1dbjc4n"}):
#         # if tweet.find('div', {"class":"css-901oao"}):
#             tweet_text = tweet.find('div',{"class":'css-901oao'}).text.strip()
#             print(tweet_text)
#             # tweet_text = tweet.find('p',{"class":'tweet-text'}).text.encode('utf8').strip()            
            
#     except: AttributeError
# f.close()