from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):

    if request.user.is_anonymous:
        return redirect("/login")
    # context = {
    #     "variable1": "Harry is great",
    #     "variable2": "Rohan is great"
    # }
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')


def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'services.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Feedback Is Always Appreciated!')
    return render(request, 'contact.html')


def loginUser(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # checking if user has entered valid credentials
        user = authenticate(username=username, password=password)
        if user is not None:

            # A backend authenticated the credentials
            login(request, user)
            print(user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
