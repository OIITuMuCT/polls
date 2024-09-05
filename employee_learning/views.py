from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import LearningCourse
from django.urls import reverse_lazy


class CourseList(ListView):
    model = LearningCourse
    template_name = 'employee_learning/course_list.html'
    # Извлекает список объектов из базы данных
    context_object_name = 'course_object_list'


class CourseDetail(DetailView):
    model = LearningCourse
    template_name = 'employee_learning/course_detail.html'
    # извлекает один объект из базы данных модели 
    context_object_name = 'course_object'



class CourseCreate(CreateView):
    model = LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('employee_learning:course_list')


class CourseUpdate(UpdateView):
    model = LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('employee_learning:course_list')


class CourseDelete(DeleteView):
    model = LearningCourse
    template_name = 'employee_learning/course_delete.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('employee_learning:course_list')
