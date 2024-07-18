from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])



#print(article_texts)
#print(article_links)
#print(article_upvote)
























#with open("website.html", encoding="utf-8") as file:
#    contents = file.read()

#soup = BeautifulSoup(contents, "html.parser")

#anchor_tags = soup.findAll(name="a")

#for tag in anchor_tags:
#    pass

#section_heading = soup.find(name="h3", class_="heading")

#print(section_heading.get("class"))

#company_url = soup.select_one(selector="#name")
#print(company_url)

#headings = soup.select(".heading")
#print(headings)

