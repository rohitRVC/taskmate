from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user account created, login to get started!"))
            return redirect("register")
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})