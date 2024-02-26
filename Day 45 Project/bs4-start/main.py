from bs4 import BeautifulSoup
# import lxml
import requests

# with open ("/home/ubuntu/100-days-of-Python/Day 45 Project/bs4-start/website.html") as file:
#     contents = file.read()
    

# soups = BeautifulSoup(contents, "html.parser")
# # print(soups.title) # prints the title tag
# # print(soups.title.string) # prints the title tag without the tag
# # print(soups.a) # prints the first anchor tag
# # print(soups.p) # prints the first paragraph tag
# # print(soups) # prints the entire html
# # print(soups.prettify()) # prettify() method is used to print the html in a more readable format

# all_anchor_tags = soups.find_all(name="a") # find_all() method is used to find all the anchor tags

# # for tag in all_anchor_tags:
# #     print(tag.getText()) # prints the text inside the anchor tags
# #     print(tag.get("href")) # prints the href attribute of the anchor tags
    
# headings = soups.find_all(name="h1", id="name") # find_all() method is used to find all the h1 tags with id="name"
# # print(headings)

# section_heading  = soups.find(name="h3", class_="heading") # find() method is used to find the first h3 tag with class="heading"
# print(section_heading)

# company_url = soups.select_one(selector="p a") # select_one() method is used to find the first anchor tag inside a paragraph tag
# print(company_url)

# name = soups.select_one(selector="#name") # select_one() method is used to find the first tag with id="name"
# print(name)


response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)
