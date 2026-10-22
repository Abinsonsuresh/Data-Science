
import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://nock-space.com/"


response = requests.get(url, timeout=10)
response.raise_for_status()

# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# print(soup)

print("Title:", soup.title.get_text(strip=True))


print("Headings:")
for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.get_text(strip=True))


# print("Links:")
# for link in soup.find_all("a", href=True):
#     print(link.get_text(strip=True), ":", link["href"])

# print(soup.get_text(" ", strip=True))

# OUTPUT
# Title: Nockspace - Innovative Digital Solutions
# Headings:
# NockSpace
# ABOUT
# NOCKSPACE
# What WeDo Best
# Web & Software
# Branding & Creative
# Digital Marketing & Automation
# Our Works
# What OurClients Say
# Let's BuildSomething Great
# Ready to transformyour digital presence?
