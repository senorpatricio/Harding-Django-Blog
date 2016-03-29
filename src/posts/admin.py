from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"] # displays 
    # list_display_links = ['timestamp'] # allows you to change which info has the link
    list_filter = ["timestamp"] # allows you to filter the content
    search_fields = ['title', 'content'] # allows you to search posts 
    # list_editable = ['title'] # allows you to edit the info in the admin
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)