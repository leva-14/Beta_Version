from django.shortcuts import render , redirect, get_object_or_404
from datetime import datetime
from .forms import PostForm
from .models import Post




def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, '../templates/posts/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            return redirect ('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, '../templates/posts/Create_Post.html', {'form': form})

def index(request):
    posts = Post.objects.all()
    return render(request, "../templates/posts/Main.html", {"posts": posts})


if __name__ == '__main__':
    DEBUG = True