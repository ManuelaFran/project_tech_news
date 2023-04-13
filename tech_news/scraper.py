from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    header = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, header=header, timeout=3)
        if response.status_code == 200:
            return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news = selector.css("h2.entry-title a::attr(href)").getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").re_first(r"\d+")
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css("div.meta-category span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    URL = 'https://blog.betrybe.com/'
    news = []
    n = 0

    while n < amount:
        html_content = fetch(URL)
        for new in scrape_updates(html_content):
            if n == amount:
                break
            new_details = fetch(new)
            news.append(scrape_news(new_details))
            n += 1
        URL = scrape_next_page_link(html_content)

    create_news(news)

    return news
