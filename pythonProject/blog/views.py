from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')  # pk 값을 기준으로 역순 정렬하여 posts에 할당
    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,        # 매핑변수 posts에 할당된 posts 데이터를 전달
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )