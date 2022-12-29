from django.contrib import admin

from .models import Post,PostItem
# Register your models here.

admin.site.register(Post)
admin.site.register(PostItem)