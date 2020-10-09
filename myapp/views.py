from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from myapp.models import *
from django.urls import reverse,reverse_lazy

# Create your views here.
class School_ListView(ListView):
    model=School
    template_name="school_list.html"

class Student_ListView(ListView):
    model=Student
    #context_object_name="students"  --> Ifever, we are using the "objects_type" in html file at for-loop, 
    # we no need to mention the context_object_name

class School_DetailView(DetailView):
    model=School
    context_object_name="school_detail"

    def get_absolute_url(self):
        return reverse("detail_view", kwargs={'pk':self.pk})

class Create_School(CreateView):
    model=School
    template_name="school_form.html"
    fields=('name','principal','location')
    

class Create_Student(CreateView):
    model=Student
    fields=('name','age','school')

class Update_School(UpdateView):
    model=School
    template_name="school_form.html"
    fields=('name','principal','location')

class Update_Student(UpdateView):
    model=Student
    fields=('name','age','school')

class Delete_School(DeleteView):
    model=School
    template_name="school_delete.html"
    success_url=reverse_lazy('school_list')
    