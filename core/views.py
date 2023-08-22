from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging
from .models import VisualData
logger = logging.getLogger(__name__)

from django.http import JsonResponse
from .models import VisualData  # Import your model

def chart1_data(request):
    data = VisualData.objects.values('likelihood', 'region')  # Replace 'count' with the actual column name you want to use for counting
    return JsonResponse(list(data), safe=False)

def chart2_data(request):
    data = VisualData.objects.values('relevance', 'country')  # Replace 'count' with the actual column name you want to use for counting
    return JsonResponse(list(data), safe=False)

def chart3_data(request):
    data = VisualData.objects.values('topic', 'intensity')  # Replace 'count' with the actual column name you want to use for counting
    return JsonResponse(list(data), safe=False)


# def index(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         if email:  # Check if the email field is not empty
#             # Here you can save the email to the database or perform any other actions you need
#             subscription = EmailSubscription(email=email)
#             subscription.save()
#             return redirect('/')
#     else:
#         return render(request, 'index.html')

def dashboard(request):
    # Fetching specific columns for different charts
    chart1_data = VisualData.objects.values('likelihood', 'region')
    chart2_data = VisualData.objects.values('relevance', 'country')
    chart3_data = VisualData.objects.values('topic', 'intensity')

    context = {
        "chart1_data": chart1_data,
        "chart2_data": chart2_data,
        "chart3_data": chart3_data,
    }

    return render(request, 'dashboard.html', context)


def signup(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        pass1= request.POST['password']
        pass2= request.POST['password2']

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=name).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif len(pass1) < 8:
                messages.info(request, 'Password too short')
                return redirect('signup')
            elif not name.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=name, email=email, password=pass1)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:   
        return render(request, 'signin.html')

def billing(request):
    return render(request, 'billing.html')

def documentation(request):
    return render(request, 'documentation.html')

def icons(request):
    return render(request, 'icons.html')

def map(request):
    return render(request, 'map.html')

def notifications(request):
    return render(request, 'notifications.html')

def profile(request):
    return render(request, 'profile.html')

def rtl(request):
    return render(request, 'rtl.html')

def tables(request):
    return render(request, 'tables.html')

def template(request):
    return render(request, 'template.html')

def typography(request):
    return render(request, 'typography.html')

def virtualreality(request):
    return render(request, 'virtualreality.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('signup')