from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from employee_learning.views import CourseDetail


app_name = "acc"
urlpatterns = [
    # previous login url
    # path('login/', views.user_login, name="login"),

    # login/logout urls
    # url-адреса входа и выхода
    path('test-function/', views.function_view_test),
    path('test-class/', views.ClassViewTest.as_view()),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    # path('course-detail/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    
    

    # # URL-адреса для смены пароля
    # path('password-change/',
    #      auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # # URL-адреса для сброса пароля
    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('password-reset/complete/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),

    
]
