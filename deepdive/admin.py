from django.contrib import admin

from .models import Post,PostItem,AnalyzingPeople,ExternalLink
# Register your models here.

admin.site.register(Post)
admin.site.register(PostItem)
admin.site.register(AnalyzingPeople)
admin.site.register(ExternalLink)