from tech_news.database import search_news
from datetime import date as d


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": 'i'}})
    return [
        (new["title"], new["url"])
        for new in news
    ]


# Requisito 8
def search_by_date(date):
    try:
        news = search_news(
            {"timestamp": d.fromisoformat(date).strftime("%d/%m/%Y")}
        )
        return [
            (new["title"], new["url"])
            for new in news
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": 'i'}})
    return [
        (new["title"], new["url"])
        for new in news
    ]
