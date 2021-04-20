from django.db import models
from django.urls import  reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True,blank=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug  = slugify(self.name)
        super(Category,self).save(*args,**kwargs) 

    def get_absolute_url(self):
        return reverse('blog:post_by_category', args=[self.slug])
#======================================================================================
class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category   = models.ForeignKey(Category,on_delete=models.CASCADE)
    title      = models.CharField(max_length=200)
    video      = models.FileField(upload_to='video/',blank=True,null=True)
    body       = models.TextField(db_index=True)
    status     = models.CharField(max_length=10, choices=options, default='published')
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts_author')
    likes      = models.ManyToManyField( User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    post_views = models.IntegerField(default=0,null=True,blank=True)
    date       = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-title',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
       return reverse('blog:post_detail',args=[self.id,])
#==========================================================================0
class Contact(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.EmailField()
    message = models.TextField()
    def __str__(self):
         return self.name 

#===============================================================================
class Comment(models.Model):

    post    = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments') 
    body    = models.TextField()
    user    = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
    date    = models.DateTimeField(auto_now_add=True)
    status  = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date',) 
    def __str__(self):
         return  self.body

               