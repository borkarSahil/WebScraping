from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# Gives all anchor tags header navigation link also
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.text)

# Only article tags
# For 1
# article_tags = soup.find(name="span", class_ = "titleline")
# print(article_tags.getText())


# For all
article_tags = soup.find_all(name="span", class_ = "titleline")
# print(article_tags)

article_text = []
article_link = []

for tag in article_tags:
    # Text
    text = tag.getText()
    # print(text)
    article_text.append(text)

    # Links
    link = tag.find(name="a").get("href")
    # print(link)
    article_link.append(link)

# Upvotes
article_upvotes = [ int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_ = "score")]

# print("Text", article_text)
# print("Link", article_link)
# print(article_upvotes)


largest_number = max(article_upvotes)
# print( largest_number )
largest_index = article_upvotes.index(largest_number)
# print(largest_index)

print(article_text[largest_index])
print(article_link[largest_index])