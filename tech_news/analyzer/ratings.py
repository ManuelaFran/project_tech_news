from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news = find_news()
    all_categories = [new["category"] for new in news]
    categories_counter = Counter(sorted(all_categories)).most_common(5)

    return [category[0] for category in categories_counter]
