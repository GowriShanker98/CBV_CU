"""ClassBased_CUDview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/list',views.School_ListView.as_view(),name="School List View"),
    path('student/list/',views.Student_ListView.as_view(),name="Student List View"),

    path('school/detail/<int:pk>',views.School_DetailView.as_view(),name="School Detail View"),

    path('school/create/',views.Create_School.as_view(),name="School Creation"),
    path('student/create/',views.Create_Student.as_view(),name="Student Creation"),

    path('school/update/<int:pk>',views.Update_School.as_view(),name="School Update View"),
    path('student/update/<int:pk>',views.Update_Student.as_view(),name="Student Update View"),

    path('school/delete/<int:pk>',views.Delete_School.as_view(),name="School Delete view"),
]
