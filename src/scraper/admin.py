from django.contrib import admin

# Register your models here.
from .models import Article, UserProfile

admin.site.register(Article)
admin.site.register(UserProfile)
