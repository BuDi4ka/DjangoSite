import os
import sys
import django
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_site.settings")
django.setup()

from pymongo import MongoClient
from quotes.models import Quote, Tag, Author

client = MongoClient('mongodb://localhost:27017')
db = client['authors_quotes']

mongo_authors = db.author.find()

for author in mongo_authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description'],
    )

mongo_quotes = db.quote.find()

for quote in mongo_quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.author.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a,
        )
        for tag in tags:
            q.tags.add(tag)
