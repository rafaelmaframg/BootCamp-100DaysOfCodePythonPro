from bs4 import BeautifulSoup
import requests

with open('website.html') as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
all_anchors = soup.find_all(name="a")  #find for <a> tags
for tag in all_anchors:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section = soup.find(name='h3', class_="heading")
print(section.getText())

company_url = soup.select_one(selector="p a") #selector css
company_url = soup.select_one(selector="#name") #selector by id
print(company_url)

headings = soup.select(selector=".heading") #all items for class
print(headings)


response = requests.get("https://news.ycombinator.com/newest")

yc_web = response.text
article_text = []
article_links = []
soup = BeautifulSoup(yc_web, "html.parser")
a_tags = soup.find_all(name="span", class_="titleline")
for each in a_tags:
    article_text.append(each.a.getText())
    article_links.append(each.a.get("href"))

article_upvotes = [x.getText().split()[0] for x in soup.find_all(name="span", class_="score")]
index = article_upvotes.index(max(article_upvotes))
print(article_text[index])
print(article_links[index])
print(article_upvotes[index])