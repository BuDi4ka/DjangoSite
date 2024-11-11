from django.core.management.base import BaseCommand
import pymongo
from ...models import Author, Quote


class Command(BaseCommand):
    help = 'Import data from MongoDB to PostgreSQL'

    def handle(self, *args, **kwargs):
        mongo_client = pymongo.MongoClient("mongodb+srv://dddd09399:qwerty123321@authors.lpuu5.mongodb.net/?retryWrites=true&w=majority&appName=Authors")
        mongo_db = mongo_client["scrapy_quotes"]

        authors_collection = mongo_db["authors"]
        quotes_collection = mongo_db["quotes"]

        # Import authors
        for author in authors_collection.find():
            Author.objects.create(
                id=str(author["_id"]),
                fullname=author.get("fullname"),
                born_date=author.get("born_date"),
                born_location=author.get("born_location"),
                description=author.get("description")
            )

        # Import quotes
        for quote in quotes_collection.find():
            author_id = str(quote.get("author"))  # Get the MongoDB _id of the author
            try:
                author = Author.objects.get(id=author_id)
                Quote.objects.create(
                    id=str(quote["_id"]),  # Store MongoDB _id as primary key
                    author=author,
                    quote=quote.get("quote"),
                    tags=quote.get("tags", []),  # Store tags, default to empty list
                )
            except Author.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Author with id {author_id} not found. Quote skipped.'))

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))