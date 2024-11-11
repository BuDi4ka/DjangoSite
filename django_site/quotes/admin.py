from django.contrib import admin
from quotes.models import Quote, Author, Tag

# Register your models here.
admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(Tag)
