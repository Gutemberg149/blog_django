from .models import Post
from django.views.generic import ListView
from .forms import PostForm
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse

class BlogAllList(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


def product_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    return render(request, 'pages/product_detail.html', {'post': post}) 


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:BlogAllList')
    else:
        form = PostForm()
    return render(request, 'pages/post_create.html', {'form': form})



def delete_post(request,slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blogs:BlogAllList')


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:product_detail', slug=post.slug)
            
    else:
        form = PostForm(instance=post)
            

    return render(request, 'pages/edit_post.html', {'form':form, "post":post})
