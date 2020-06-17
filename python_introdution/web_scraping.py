## Scrping the ConsumerReport products list using BeautifulSoup

## importing bs4, requests modules
import bs4
import requests

## initializing url
url = "https://www.consumerreports.org/cro/a-to-z-index/products/index.htm"

## getting the reponse from the page using get method of requests module
page = requests.get(url)

## storing the content of the page in a variable
html = page.content

## creating BeautifulSoup object
soup = bs4.BeautifulSoup(html, "xml")

## see the class or id of the tag which contains names ans links
div_class = "crux-body-copy"

## getting all the divs using find_all method
div_tags = soup.find_all("div", class_=div_class) ## finding divs whichs has mentioned class

## we will see all the tags with a tags which has name and link inside the div
for tag in div_tags:
    print(tag)