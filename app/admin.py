from django.contrib import admin
from .models import Complain,Comment,Status,CommentByTeacher

admin.site.register(Complain)
admin.site.register(Comment)
admin.site.register(CommentByTeacher)
admin.site.register(Status)
