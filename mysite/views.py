from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout(request):
    logout(request)
    return redirect('/')

def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method == "GET":
        userform = UserCreationForm()

    return render(request, "registration/signup.html", {
        "userform": userform,
}) 		