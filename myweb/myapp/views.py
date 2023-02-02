from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Client, Post
from django.contrib.auth.decorators import login_required
import re




# Create your views here.

@login_required(login_url='signin/')
def index(request):
        user_client = Client.objects.get(user=request.user)
        all_client = Client.objects.exclude(user=request.user)
        post_lists = Post.objects.filter(user=request.user.username)
        return render(request, 'index.html', {'all_client': all_client, 'user_client': user_client
                                          , 'post_lists': post_lists})

# def preupload(request):
#     return render(request, 'upload.html')

@login_required(login_url='signin')
def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image')
        title = request.POST['title']
        passage = request.POST['passage']
        Post.objects.create(user=user, image=image, title=title, passage=passage)
        return redirect('/')



@login_required(login_url='signin')
def client(request, id_user):
    preuser = Client.objects.get(user=request.user)
    user_client = Client.objects.get(id_user=id_user)
    user_posts = Post.objects.filter(user=user_client.user.username)


    context = {
        'user_client': user_client,
        'user_posts': user_posts,
        'preuser': preuser,
    }
    return render(request, 'client.html', context)



@login_required(login_url='signin')
def settings(request):
    user_client = Client.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image') == None:
            user_client.location = request.POST['location']
            user_client.save()
        if request.FILES.get('image') != None:
            user_client.img = request.FILES.get('image')
            user_client.location = request.POST['location']
            user_client.save()
    return render(request, 'settings.html', {'user_client': user_client})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if username and password and password2 and email:
            my_emali = re.findall(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{2,3}$', email)
            if not my_emali:
                error_message = '邮箱格式出错'
                return render(request, 'signup.html', {'error_message': error_message})
            if password == password2:
                if User.objects.filter(email=email).exists():
                    error_message = '该邮箱已存在'
                    return render(request, 'signup.html', {'error_message': error_message})
                elif User.objects.filter(username=username).exists():
                    error_message = '用户名已存在'
                    return render(request, 'signup.html', {'error_message': error_message})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()


                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)


                    user_model = User.objects.get(username=username)
                    new_client = Client.objects.create(user=user_model, id_user=user_model.id)
                    new_client.save()
                    return redirect('settings')
            else:
                error_message = '密码前后不一致'
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = '请输入所有信息'
            return render(request, 'signup.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            error_message = '用户名或密码错误'
            return render(request, 'signin.html', {'error_message': error_message})

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def preedit(request, pk):
    post_now = Post.objects.get(id=pk)
    context = {
        'post_now':post_now,
    }
    return render(request, 'edit.html', context)


@login_required(login_url='signin')
def edit(request, pk):
    post_now = Post.objects.get(id=pk)
    post_now.title = request.POST['title']
    post_now.passage = request.POST['passage']
    if request.FILES.get('image') != None:
        post_now.image = request.FILES.get('image')
        post_now.save()
    else:
        post_now.save()
    return redirect('/')

@login_required(login_url='signin')
def delete(request, pk):
    post_now = Post.objects.get(id=pk)
    post_now.delete()
    return redirect('/')

@login_required(login_url='signin')
def search(request):
    title = request.POST['title']
    post_list = Post.objects.filter(title=title)
    if post_list:
        return render(request, 'post.html', {'post_list': post_list})
    else:
        return redirect('/')