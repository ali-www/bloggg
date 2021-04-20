from django.contrib import admin
from  .models import Post,Category,Contact,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Comment)