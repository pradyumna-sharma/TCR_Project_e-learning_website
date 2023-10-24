"""TCR_E_learning_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login_signup', views.login_signup_view, name='login_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home', views.home, name='home'),
    path('Learn', views.Learn, name='Learn'),
    path('calendar/', views.cal, name='cal'),
    path('help/', views.help, name='help'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('courses/', views.courses_list, name='courses_list'),
    path('my-purchases/', views.purchased_courses, name='my-purchases'),
    path('add_to_purchased/<int:course_id>/', views.add_to_purchased, name='add_to_purchased'),
    path('main_coursepage/<int:course_id>/', views.main_course, name='main_coursepage'),
    path('', views.page,name='page')
]
