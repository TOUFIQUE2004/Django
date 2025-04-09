from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UniversityForm

def index(request):
    form = UniversityForm()  # Initialize form outside the if-else block
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('admin:index')  # Redirect to admin dashboard
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'index.html', {'form': form})
