from bs4 import BeautifulSoup
# import lxml


with open('website.html') as file:
  contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title) # returns title tag
print(soup.title.string)  # returns the string in title tag

print(soup)     # entire html soup
print(soup.prettify())    # prettify the html


all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

# find() gets first h1 with id name
h1_heading = soup.find(name="h1", id="name")
h3_heading = soup.find(name="h3", class_="heading")
print(h1_heading, h3_heading)

# select() selects all 
# select_one() gets first one
company_url = soup.select_one(selector="p a")
print(company_url)
name = soup.select_one(selector="#name")
print(name)