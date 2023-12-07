import re
import requests
from bs4 import BeautifulSoup

url = "http://localhost:3333/"
response = requests.get(url)
raw_html = response.text

parsed_html = BeautifulSoup(raw_html, "html.parser", from_encoding='utf-8')
title_html = parsed_html.title.text
top_jobs_heading = parsed_html.select_one("#intro > div > div > article > h2")
top_jobs_heading_text = top_jobs_heading.text
article = top_jobs_heading.parent

print(raw_html)
print(parsed_html)
print(title_html)
print(top_jobs_heading_text)
print(article)

for p in article.select("p"):
    print(re.sub(r"\s{1,}", " ", p.text).strip())

