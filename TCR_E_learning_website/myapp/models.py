from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, tokens, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, tokens=tokens)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tokens, password):
        user = self.create_user(email, name, tokens, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    tokens = models.TextField(max_length=64)
    photo = models.ImageField(upload_to='static/user_photos', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tokens']



class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    course_photo = models.ImageField(upload_to='static/course_photos/') 

class PurchasedCourse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)


from django.db import models

class CourseURL(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)  
    def __str__(self):
        return self.url

class UserCourseProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    urls_completed = models.PositiveIntegerField(default=0) 
    def __str__(self):
        return f"{self.user.name} - {self.course.course_name}"

    
    
    
