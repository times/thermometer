from django.contrib import admin
from comments.models import Comment, User

class CommentAdmin(admin.ModelAdmin):
  list_display = ('pub_date','comment',)
  search_fields = ('comment',)
  list_per_page = 50
  list_max_show_all = 1000

class UserAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)
  list_per_page = 50
  list_max_show_all = 1000

admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)