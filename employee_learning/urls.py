from django.urls import path, reverse
from .views import CourseList, CourseDetail, CourseCreate, CourseUpdate,  CourseDelete 

app_name='employee_learning'

urlpatterns = [
    #  path('kebab-case/' , PascalCase.as_view() ,  name="'snake_case')
    path('course-list/', CourseList.as_view(), name='course_list'),
    path('course-detail/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    path('course-create/', CourseCreate.as_view(), name='course_create'),
    path('course-update/<int:pk>/', CourseUpdate.as_view(), name='course_update'),
    path('course-delete/<int:pk>/', CourseDelete.as_view(), name='course_delete'),
]
