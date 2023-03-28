from django.contrib import admin
from .models import Post , About , Comment , Contact ,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created','author' ,'publish')
    list_filter = ("status",)
    list_filter = ("publish",)
   
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','created')
    list_filter = ("name",)
class CommentAdmin(admin.ModelAdmin): 
      list_display = ('name', 'comment','post','created')
      list_filter = ("post",)  
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag)