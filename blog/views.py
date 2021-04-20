from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.shortcuts import redirect
from .models import  Category,Post,Contact,Comment
from .forms import FormContact
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator


# Create your views here.
def post_list(request,category_slug=None):
    category   = None
    categories = Category.objects.all()
    posts      = Post.objects.all()
    #================================================== start pagination 
    paginator = Paginator(posts, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #================================================== end pagination 
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        posts    = posts.filter(category=category)
    return render(request, 'post_list.html', {'categories':categories,
                                              'category':category,
                                              'posts':posts,'page_obj':page_obj
                                              })
#=======================================================================================
def post_detail(request,id):
    posts    = get_object_or_404(Post,id=id)
    posts.post_views = posts.post_views + 1
    posts.save() 
    comments = posts.comments.all()

    return render(request,'post_detail.html',{'posts':posts,'comments':comments })

#========================================================================================
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = request.POST.get('postid')
        post = get_object_or_404(Post,id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()
        return JsonResponse({'result':result})

#================================================================
def contact(request):
    form = FormContact()
    if request.is_ajax():
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg':'success'
            })
    return render(request,'contact.html',{'form':form})

#=================================================
def save_comment(request):
    if request.method =='POST':
        comment = request.POST['comment']
        postsid = request.POST['postsid']
        post    = Post.objects.get(pk=postsid)
        user    = request.user
        Comment.objects.create(
            post = post,
            body = comment,
            user = user
        )

    return JsonResponse({'bool':True})
