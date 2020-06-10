from django.contrib import admin
from qnas.models import Qna, QnaComment, LikeQna, LikeQnaComment

# Register your models here.
class QnaAdmin(admin.ModelAdmin):
    model = Qna

class QnaCommentAdmin(admin.ModelAdmin):
    model = QnaComment

class LikePostAdmin(admin.ModelAdmin):
    model = LikeQna

class LikeQnaCommentAdmin(admin.ModelAdmin):
    model = LikeQnaComment


admin.site.register(Qna, QnaAdmin)
admin.site.register(QnaComment, QnaCommentAdmin)
admin.site.register(LikeQna, LikePostAdmin)
admin.site.register(LikeQnaComment, LikeQnaCommentAdmin)