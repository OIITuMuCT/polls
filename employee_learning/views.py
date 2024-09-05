from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import LearningCourse
from django.urls import reverse_lazy
import datetime


class CourseList(ListView):
    # model = LearningCourse
    # queryset = LearningCourse.objects.order_by('title')
    queryset = LearningCourse.objects.filter(level='B')
    template_name = 'employee_learning/course_list.html'
    # Извлекает список объектов из базы данных
    context_object_name = 'course_object_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context


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


class Index(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.data.today()
        return context