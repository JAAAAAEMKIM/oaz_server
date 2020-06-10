from django.contrib import admin
from boards.models import Post, Comment, LikePost, LikeComment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    model = Post

class CommentAdmin(admin.ModelAdmin):
    model = Comment

class LikePostAdmin(admin.ModelAdmin):
    model = LikePost

class LikeCommentAdmin(admin.ModelAdmin):
    model = LikeComment


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(LikePost, LikePostAdmin)
# admin.site.register(LikeComment, LikeCommentAdmin)