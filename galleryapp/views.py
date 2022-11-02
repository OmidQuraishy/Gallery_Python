from email import message
import imp
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from galleryapp.forms import GalleryForm

from galleryapp.models import Gallery, Slider

# Create your views here.


@login_required(login_url='login')
def index(request):
    slider = Slider.objects.all()

    gallery = Gallery.objects.all().order_by('-created_at')[:3]

    all_gallery = Gallery.objects.all()
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = GalleryForm()

    context = {
        'form': form,
        'slider': slider,
        'gallery': gallery,
        'all_gallery': all_gallery
    }
    return render(request, 'home/index.html', context)


def user_singup(request):
    if request.method == 'POST':
        firstname = request.POST.get('fist_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request, "Password does not match")
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.warning(request, "نام موجود است")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, "Email already taken")
            return redirect('signup')
        else:
            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                password=password1,
            )
            user.save()
            messages.success(request, 'شما موفقانه ثبت نام شدید')
            return redirect('signup')
    return render(request, 'account/signup.html')


def login(request):

    if request.user.is_authenticated:
        return redirect("index")

    else:
        if request.method == "POST":

            user = request.POST.get('username')
            password = request.POST.get('pass')

            auth = authenticate(request,
                                username=user,
                                password=password
                                )
            if auth is not None:
                auth_login(request, auth)
                return redirect("index")

            else:
                messages.error(request, "نام و گذرواژه همخانی ندارد")

    return render(request, 'account/login.html')


def user_logout(request):
    logout(request)
    return redirect("login")
