from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

# print(contents)
soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# To get the href links
for tag in all_anchor_tags:
    print(tag.getText())

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)