
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserModel

# Create your views here.


def join_now(request):
    if request.method == "POST":
        
        form = UserForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)

            f = UserModel(
                firstname=cd['firstname'],
                lastname=cd['lastname'],
                r_name=cd['r_name'],
                r_number=cd['r_number'],
                r_address=cd['r_address'],
                phone=cd['phone'],
                email=cd['email'],
            )

            f.save()

            return redirect("/home?login=true")
        
    else:
        form = UserForm()
    return render(request, "join_now.html",  {"form": form})


def home(request):
    return render(request, "home.html")


def send_to_home(request):
    return redirect(home)


