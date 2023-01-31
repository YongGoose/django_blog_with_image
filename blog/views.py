from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
# Create your views here.
def main(request):
    return render(request, 'index.html')

def blog_views(request):
    blogs = BLog.objects.all()
    # return render(request, 'home.html', {'blogs':blogs})
    return render(request,'home.html', {'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(BLog, pk=id)
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = BLog()
    new_blog.title = request.POST['title']
    new_blog.author = request.POST['author']
    new_blog.image = request.FILES['image']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('blog_views')


def edit(request,id):
    blog = BLog.objects.get(id = id)
    return render(request, 'edit.html', {'blog':blog})

def update(request, id):
    if request.method == 'POST':
        update_blog = BLog.objects.get(id = id)
        update_blog.title = request.POST['title']
        update_blog.author = request.POST['author']
        update_blog.body = request.POST['body']
        update_blog.save()
        return redirect('detail', update_blog.id)
    else:
        blog = BLog.objects.get(id = id)
        return render(request, 'edit.html', {'blog':blog})

def delete(request, id):
    delete_blog = BLog.objects.get(id = id)
    delete_blog.delete()
    return redirect('blog_views')

def make_post(request):
    if request.method == 'POST':
        new_blog = BLog()
        new_blog.title = request.POST['title']
        new_blog.author = request.POST['author']
        new_blog.image = request.FILES.get('image')
        new_blog.body = request.POST['body']
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('blog_views')
    else:
        return render(request,'new.html')

# 이 두 함수의 차이점은 render의 경우 내가 가진 templates를 data를 넣어 보내고 싶을 때 이용하고, redirect는 내가 가진 templates뿐만 아니라 절대 url로 이동하고 싶을 때에도 이용할 수 있다는 거죠

def create_comment(request, blog_id):
    if request.method == "POST":
        comment = Comment()
        comment.blog = get_object_or_404(BLog, pk=blog_id)
        comment.author = request.POST['author']
        comment.content = request.POST['content']
        comment.create_at = timezone.datetime.now()
        comment.save()

        return redirect('detail', blog_id)

def delete_comment(request, blog_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    my_comment.delete()
    return redirect('detail', blog_id)