from training.models import Book
from django.contrib import admin

# Make the Book app modifiable in the admin
admin.site.register(Book)
