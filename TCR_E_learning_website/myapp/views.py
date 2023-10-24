from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages
from .models import CustomUser
from .models import Course, PurchasedCourse,CourseURL,UserCourseProgress
import secrets
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login, authenticate


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'templets/login.html'


def generate_token(length=32):
    return secrets.token_hex(length)


from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def login_signup_view(request):
    if request.method == 'POST':
        if 'login-submit' in request.POST:
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')  # Use 'username' instead of 'email'
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, email=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Login form is not valid')
                print(login_form.errors)
        elif 'signup-submit' in request.POST:
            signup_form = CustomUserCreationForm(request.POST, request.FILES)
            if signup_form.is_valid():
                user = signup_form.save()
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Signup form is not valid')
                print("Signup form is not valid")

    login_form = CustomAuthenticationForm()
    signup_form = CustomUserCreationForm()
    return render(request, 'login.html', {'login_form': login_form, 'signup_form': signup_form})





def page(request):
    return render(request, 'index.html')


def Learn(request):
    return render(request, 'LearnMore.html')


def cal(request):
    return render(request, 'db.html')

@login_required
def home(request):
    user =request.user
    username = user.name
    email = user.email
    profile_image = user.photo 
    context ={
        'email': email,
        }
    return render(request, 'home.html',{'profile_image': profile_image,'username': username})
 

from django.shortcuts import render
from .models import Course, PurchasedCourse

def courses_list(request):
    courses = Course.objects.all()
    # Get the current user (you'll need to adjust this based on your authentication setup)
    current_user = request.user  # Assuming you're using Django's built-in authentication
    # Create a set of purchased course IDs for the current user
    purchased_course_ids = set(
        PurchasedCourse.objects.filter(user=current_user).values_list('course_id', flat=True)
    )
    # Pass the courses and the set of purchased course IDs to the template
    return render(request, 'course_list.html', {'courses': courses, 'purchased_course_ids': purchased_course_ids})




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Course, PurchasedCourse

@login_required
def add_to_purchased(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        user = request.user  # This will give you the currently authenticated user
        purchased_course, created = PurchasedCourse.objects.get_or_create(user=user, course=course)

    return redirect('courses_list')


def purchased_courses(request):
    current_user = request.user
    purchased_course_ids = PurchasedCourse.objects.filter(user=current_user).values_list('course', flat=True)
    purchased_courses = Course.objects.filter(id__in=purchased_course_ids)

    return render(request, 'my_course.html', {'purchased_courses': purchased_courses})

def help(request):
    return render(request,'help.html')


def profile(request):
    current_user = request.user
    context ={
        'email': current_user.email,
        'photo': current_user.photo,
        'name': current_user.name,
        }
    return render(request,'profile.html',context)


from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import CustomUserChangeForm, CustomPasswordChangeForm

@login_required
def settings(request):
    user = request.user
    user_form = CustomUserChangeForm(instance=user)
    password_form = CustomPasswordChangeForm(user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        password_form = CustomPasswordChangeForm(user, request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Account settings updated successfully.')
        else:
            messages.error(request, 'Account settings update failed. Please correct the errors.')

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
        else:
            messages.error(request, 'Password change failed. Please correct the errors.')

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'settings.html', context)

def Dashboard(request):
    current_user = request.user
    purchased_course_ids = PurchasedCourse.objects.filter(user=current_user).values_list('course', flat=True)
    purchased_courses = Course.objects.filter(id__in=purchased_course_ids)
    progress = UserCourseProgress.objects.filter(user=current_user)
    return render(request,'dashboard.html',{'purchased_courses': purchased_courses,'progress':progress})



def main_course(request,course_id):
    if request.method == 'POST':
        user = request.user 
        urls = CourseURL.objects.filter(course_id=course_id)
        current_course = Course.objects.get(id=course_id)
    return render(request,'main_coursepage.html',{'urls':urls,'current_course':current_course})