from bs4 import BeautifulSoup
# import lxml


with open('website.html') as file:
  contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title) # returns title tag
print(soup.title.string)  # returns the string in title tag

print(soup)     # entire html soup
print(soup.prettify())    # prettify the html
