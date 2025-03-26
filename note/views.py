from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
# Create your views here.

@login_required
def main(request):
    # user = request.user
    # post = Note.objects.all(user=user)
    # post = Note.objects.filter(user=user)
    return render(request,'landing.html', )

@login_required
def detail(request, post_id):
    post = get_object_or_404(Note, pk=post_id)
    return render(request, 'detail.html', {'post': post})


# @login_required
def create_note(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        content = request.POST.get("content")
        Note.objects.create(title=title, content=content, user=user)
        return redirect ("Home page")
    return render(request, "detail.html")


@login_required
def delete_note(request, post_id):
    post = get_object_or_404(Note, id=post_id)
    post.delete()
    return redirect("Home page")

@login_required
def edit_note(request, post_id):
    post = get_object_or_404 (Note, id=post_id)
    if request.method =="POST":
        post.title = request.POST["title"]
        post.content =request.POST["content"]
        post.save()
        return redirect("Home page")
    return render (request, "detail.html" ,{"note": post})


def create_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create(username=username, email=email)
            user.set_password(password1)
            user.save()
            return redirect('Home page')
    return render(request, 'signup.html')


@login_required
def home(request):
    user = request.user
    notes  = Note.objects.filter(user=user)
    return render(request, 'index.html', {"notes": notes})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # if not username and not password:
        #     return render(request, 'login.html', {'error': 'Both fields are required.'})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home page')  
        return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

# Create your views here.
