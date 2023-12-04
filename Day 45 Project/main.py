from bs4 import BeautifulSoup
import requests
# import lxml


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
BeautifulSoup(yc_web_page, "html.parser")
article = soup.find(name="a", class_="storylink")
article_text = []
article_link = []
for article_tag in article:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get("href")
    article_link.append(link)
    


article_upvote = [int(score.getText()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_text[largest_index])
print(article_link[largest_index])


# print(article_texts)
# print(article_links)
# print(article_upvotes)


















# with open("website.html") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())   
#     # print(tag.get("href"))
    
# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(class_is_heading)

# h3_tag = soup.find(name="h3", class_="heading")
# print(h3_tag.getText())

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)
