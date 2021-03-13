"""
Author : Raju Datla
App: To scrap BBC news websites
functions: get_bbc_news to get title, small description and content
"""

# Imports
import requests
from bs4 import BeautifulSoup
import json

# vars
news = {}

# # news = []
# #
# #
# # class BBC:
# #     def __init__(self, url: str):
# #         article = requests.get(url)
# #         self.soup = bs(article.content, "html.parser")
# #         #        self.body = self.get_body()
# #         #        self.title = self.get_title()
# #         self.stories = self.soup.find_all('div', {'class': 'gs-c-promo'})
# #         self.url = url
# #
# #     def get_news(self, stories):
# #         for idx, story in enumerate(stories[0:10]):
# #             news_article = {}
# #             headline = story.find('h3')
# #             # article title
# #             news_article['title'] = headline.text
# #             # article link
# #             link = story.find('a')
# #             if link:
# #                 news_article['link'] = self.url + link['href']
# #             # article summary
# #             summary = story.find('p')
# #             if summary:
# #                 news_article['summary'] = summary.text
# #             # article content
# #             news_article['body'] = self.get_details(link)
# #
# #     def get_details(self, article_url):
# #         article = requests.get(article_url)
# #         article_soup = bs(article.content, 'html.parser')
# #         body = article_soup.find(property="articleBody")
# #         return [p.text for p in body.find_all("p")]
#
#
# '''
#     def get_body(self) -> list:
#         body = self.soup.find(property="articleBody")
#         return [p.text for p in body.find_all("p")]
#
#     def get_title(self) -> str:
#         return self.soup.find(class_="story-body__h1").text
#
# '''
# #parsed = BBC('https://www.bbc.co.uk/news/world')
#
# #print(BBC.get_news('https://www.bbc.co.uk/news/world'))




# Constants
BBC_URL = "http://feeds.bbci.co.uk/news/rss.xml"


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_headlines(bbc_url, no_of_articles=10):
    # request and parse html
    soup = get_soup(bbc_url)
    # isolate the rest of the headlines (articles)
    articles = soup.find_all('item')
    # extract headlines and url from links on main page & print
    i = 0
    for item in range(no_of_articles):  # to get only 10 articles
        news_local = {}
        # Article URL
        articleurl = articles[item].guid.text
        news_local['url'] = articleurl
        # Article Title / Headline
        articleheadline = articles[item].title.text
        news_local['headline'] = articleheadline
        news['article' + str(i)] = news_local
        # Article Body / Content

        i += 1
    return json.dumps(news)


# partial url example ( /news/1072279 )
def get_article_text(article_url):
    soup = get_soup(article_url)
    story = soup.find_all('p')  # soup.article#soup.find_all('p')
    return story
    # range_start is set to 12 to ignore all the pre-amble / social media ads.
    # range_start = 12
    # for p_tag in range(len(story)):
    #     if p_tag < range_start:
    #         pass
    #     else:
    #         return story[p_tag].text

# Local testing
urls = get_headlines(no_of_articles=10, bbc_url=BBC_URL)
# for item in news.items():
print(news)
