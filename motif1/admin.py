from django.contrib import admin
from .models import Team, Contact, BlogPost, Comment, Faq

# Register your models here.


admin.site.register(Contact)





class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['user','id']
    readonly_fields  = ['id']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name','id_user' ]
    readonly_fields  =['id_user'] 


class FaqAdmin(admin.ModelAdmin):
    list_display = ['question','id' ]
    readonly_fields = ['id'] 

class CommentAdmin(admin.ModelAdmin):
    list_display = ['email','id' ]
    readonly_fields = ['id'] 

admin.site.register(Faq,FaqAdmin)
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Comment, CommentAdmin)