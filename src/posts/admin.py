from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"] # displays 

    list_filter = ["timestamp"] # allows you to filter the content
    search_fields = ['title', 'content'] # allows you to search posts
    prepopulated_fields = {'slug': ['title']}

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(PostAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)