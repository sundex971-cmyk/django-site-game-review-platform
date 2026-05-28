from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.
def contacts(request):
    return render(request, 'pages/contacts.html')

def login_view(request):
    return render(request, 'pages/login.html')

def register_view(request):
    
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(
        request,
        'pages/register.html',
        context={
            'form': form
        }
    )
