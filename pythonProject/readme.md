# Python 설치
    https://www.python.org/downloads/ 에서 [Download Python 3.11.0] 버튼을 눌러 설치

<br>

# Pycharm 설치
	1. https://www.jetbrains.com/ko-kr/pycharm/download/other.html 에서 2022.1.4 이하의 해당 운영체제의 community 버전을 설치
	2. File > Settings > Tool > Terminal > Shell path: C:\WINDOWS\system32\cmd.exe  :  cmd로 쉘 변경

<br>

# Django 설치
	방법1 : File > Settings > Project:pythonProject > Python Interpreter > + [클릭]하여 Django 검색하여 설치
    방법2 : 하단 패널의 [Python Packages] 패널을 활용하여 Django 를 검색하여 설치
    방법3 : Terminal 에서 pip install Django 를 파이썬인스톨패키지관리자를 이용하여 설치

<br>

# Django 관리자 프로젝트 생성 및 시작
    1. 프로젝트 생성 : django-admin startproject 프로젝트명 .
        django-admin startproject do_it_django_prj
    2. 프로젝트 서버 구동 : python manage.py runserver
    3. python manage.py 로 시작하는 명령은 현재 디렉토리에 manage.py이 있어야 함

<br>

# Django 데이터베이스 설정 및 시작
    1. 데이터베이스 관리자 계정 설정 : python manage.py migrate
    2. 기본 db인 sqlite3가 아닌 경우의 DB 시스템을 진행하는 경우 __init__.py에 별도의 설정을 하고, python manage.py migrate 함
    3. 데이터베이스 사용자 추가 : python manage.py createsuperuser
    4. 데이터베이스 사용자의 아이디, 비밀번호 등을 입력하여 사용자를 추가
    5. python manage.py runserver 로 서버 다시 구동
    6. 브라우저에서 http://127.0.0.1:8000/admin 을 입력

# MariaDB 설치
    1. https://mariadb.org/download 에 접속하여 프로그램 다운로드 받아 설치

    2. 설치 시 설정된 root 비밀번호를 꼭 기억하고, 사용자 추가시는 HeidisSQL을 실행하여 추가 및 설정

    3. HeidisSQL의 왼쪽 접속자 카테고리에서 마우스 오른쪽 버튼 [새로 생성(O)] -> 데이터 베이스(T)

<br>    

# 새 앱 생성
    1. python manage.py startapp 앱명
```cmd
        python manage.py startapp blog
        python manage.py startapp single_pages
```

    2. settings.py 에서 INSTALLED_APPS 의 항목에 새로 생성한 앱(blog, single_pages)을 추가
```python
        INSTALLED_APPS = [
            # ..... 생략 
            'django.contrib.staticfiles',
            'blog',
            'single_pages',
        ]
        # ..... 생략
```

<br>

# 모델 만들기
    1. https://docs.djangoproject.com/en/4.1/ 의 model 카테고리를 찾아 참고하여 모델을 만듦

    2. 해당 프로젝트(blog)에 models.py 를 열고, 필요한 테이블명(클래스명)과 데이터 필드(컬럼명)와 데이터 타입, 크기를 지정
```python
        from django.db import models
        class Post(models.Model):
            title = models.CharField(max_length=30)
            content = models.TextField()
            created_at = models.DateTimeField(auto_now=True, null=True)
            # 기본키 설정
            def __str__(self):
                return f'[{self.pk}]{self.title}'
```

    3. python manage.py makemigrations 명령으로 모델을 생성
        해당 앱(blog)의 models.py 에 등록되어 있는 클래스이름(Post)으로 model이 생성
```cmd
        python manage.py makemigrations
```

    4. 해당 앱(blog)의 admin.py 에 내용을 기재하여 admin에서 접속이 가능하도록 함
```python
        from django.contrib import admin
        from .models import Post
        admin.site.register(Post)
```

    5. python manage.py runserver 입력 후 브라우저에서 http://127.0.0.1:8000/admin 을 입력
```cmd
        python manage.py runserver
```

    6. 브라우저에서 해당 페이지(http://127.0.0.1:8000/admin)의 화면 중에 새로 추가된 모델(Post)에 데이터 추가
    ※ python manage.py runserver를 한 뒤에 결과를 확인해보면 가끔 no such table 에러가 뜨는 경우 
```cmd
        python manage.py migrate --run-syncdb
```

<br>

# 뷰 만들기
    1. settings.py의 내용을 편집
```python
        # .... 생략
        # 타임존을 변경
        TIME_ZONE = 'Asia/Seoul'
        # .... 생략
        USE_TZ = False
```

    2. 메인 프로젝트(앱 do_it_django_prj)의 urls.py 를 편집

```python
        from django.contrib import admin
        from django.urls import path, include
        urlpatterns = [
            path('blog/', include('blog.urls')),
            path('admin/', admin.site.urls),
        ]
```

    3. 해당 앱(blog)의 views.py를 편집

```python
        from django.shortcuts import render

        # Create your views here.
        def index(request):
            return render(
                request,
                'blog/index.html',
        )
```

<br>

# 템플릿 작성하기
    1. 해당 앱(blog)에 templates/blog/index.html 디렉토리 및 파일 작성
```html
        <!-- 메인 앱 -> D:\dev\pythonProject\do_it_django_prj -->
        <!-- single_pages -> D:\dev\pythonProject\single_pages -->
        <!-- blog -> D:\dev\pythonProject\blog -->
        <!-- D:\dev\pythonProject\blog\templates\blog\index.html -->
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <title>Blog</title>
        </head>
        <body>
            <h1>Blog</h1>
        </body>
        </html>
```

<br>

# 데이터베이스 데이터 매핑 하기
    1. 새 앱(blog) 의 views.py 를 편집하여 렌더링(보여질)될 데이터를 지정

```python
        from django.shortcuts import render
        from .models import Post

        def index(request):
            posts = Post.objects.all().order_by('-pk')  # pk 값을 기준으로 역순 정렬하여 posts에 할당
            return render(
                request,
                'blog/index.html',
                {
                    'posts' : posts,        # 매핑변수 posts에 할당된 posts 데이터를 전달
                }
        )
```

<br>        
        
    2. 해당 앱(blog)에 templates/blog/index.html 디렉토리 및 파일 편집

```html
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <title>Blog</title>
        </head>
        <body>
            <h1>Blog</h1>
            <!--  -->
        {% for p in posts %}
            <hr>
            <h2>{{ p.title }}</h2>
            <h4>{{ p.create_at }}</h4>
            <p>{{ p.content }}</p>
        {% endfor %}
        </body>
        </html>
```

        ※ python 명령을 템플릿에서 구현시 '{%' 로 시작하여 '% }' 로 끝나며, 리스트에 내포된 테이블(model) 데이터를 그 사이에 출력

# 상세 페이지 만들기 및 매핑하기
    1. 새 앱(blog) 의 urls.py 를 편집
```python
        from django.urls import path
        from . import views
        
        urlpatterns = [
            # 작성예제
            path('<int:pk>/', views.single_post_page),
            path('', views.index),
        ]
```

<br>

    2. 새 앱(blog) 의 views.py 를 편집

```python
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
```

<br>

    3. 해당 앱(blog)에 templates/blog/single_post_page.html 파일 생성

```html
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <title>{{ post.title }} - Blog</title>
        </head>
        <body>
        <nav>
            <a href="/blog/">Blog</a>
        </nav>
        <h1>{{ post.title }}</h1>
        <h4>{{ post.create_at }}</h4>
        <p>{{ post.content }}</p>
        <h3>여기 댓글이 들어 올 수 있습니다.</h3>
        </body>
        </html>
```

<br>

    4. 해당 앱(blog)에 templates/blog/index.html 파일 편집
```html
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <title>Blog</title>
        </head>
        <body>
            <h1>Blog</h1>
            <!--  -->
        {% for p in posts %}
            <hr>
            <h2><a href="{{ p.get_absolute_url }}">{{ p.title }}</a></h2>
            <h4>{{ p.create_at }}</h4>
            <p>{{ p.content }}</p>
        {% endfor %}
        </body>
        </html>
```

<br>

        5. 해당 앱(blog)의 models.py 를 편집

```python
        from django.db import models
        
        class Post(models.Model):
            title = models.CharField(max_length=30)
            content = models.TextField()
            created_at = models.DateTimeField(auto_now=True, null=True)
        
            def __str__(self):
                return f'[{self.pk}]{self.title}'
        
            def get_absolute_url(self):
                return f'/blog/{self.pk}'
```

# FBV로 블로그 포스트 상세 페이지 만들기

        1. 메인 앱(do_it_django_prj)의 urls.py 편집
```python
        from django.contrib import admin
        from django.urls import path, include
        urlpatterns = [
            path('blog/', include('blog.urls')),
            path('admin/', admin.site.urls),
            path('', include('single_pages.urls')),
        ]
```

        2. 서브 앱(single_pages)의 urls.py 생성
```python
        from django.urls import path
        from . import views
        
        urlpatterns = [
            path('about_me/', views.about_me),
            path('', views.landing),
        ]
```

        3. 서브 앱(single_pages)의 views.py 편집
```python
        from django.shortcuts import render
        
        # Create your views here.
        def landing(request):
            return render(
                request,
                'single_pages/landing.html',
            )
        
        def about_me(request):
            return render(
                request,
                'single_pages/about_me.html',
            )
```
        4. single_pages\templates\single_pages\langding.html 작성
```html
        <!DOCTYPE html>
        <html lang="ko">
        <head>
        <meta charset="UTF-8">
        <title>나의 홈페이지</title>
        </head>
        <body>
            <nav>
                <a href="/blog/">Blog</a>
                <a href="/about_me">About Me</a>
            </nav>
            <h1>안녕하세요, 반갑습니다.</h1>
            <h2>[김기태 블로그]</h2>
        </body>
        </html>
```

        5. single_pages\templates\single_pages\about_me.html 작성
```html
        <!DOCTYPE html>
        <html lang="ko">
        <head>
        <meta charset="UTF-8">
        <title>내 소개</title>
        </head>
        <body>
          <nav>
            <a href="/blog/">Blog</a>
            <a href="/about_me">About Me</a>
          </nav>
          <h1>포트폴리오 페이지</h1>
          <h2>[김기태] 포트폴리오 페이지</h2>
          <h3>아직 공사중입니다.</h3>
        </body>
        </html>
```



