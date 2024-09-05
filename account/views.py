from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, \
                    UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

from django.views.generic import TemplateView
# from social_core.backends.oauth import BaseOAuth2

def user_login(request):
    # Если метод запроса Пост
    if request.method == 'POST':
        # создаем пустую форму
        form = LoginForm(request.POST)
        # Проверяем валидность формы
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
    

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html', 
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, 
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile update'\
                'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                instance=request.user.profile)
    return render(request, 
                  'account/edit.html',
                {'user_form': user_form,
                 'profile_form': profile_form})
    


def function_view_test(request):
    return HttpResponse('<h1>Hello world! Function-based ViewTest</h1>')


class ClassViewTest(TemplateView):
    template_name = 'account/test.html'
    
    



# class GitHubOAuth2(BaseOAuth2):
#     """GitHub OAuth authentication backend"""
#     name = 'github'
#     AUTHORIZATION_URL = 'https://github.com/login/oauth/authorize'
#     ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
#     ACCESS_TOKEN_METHOD = 'POST'
#     SCOPE_SEPARATOR = ','
#     EXTRA_DATA = [
#         ('id', 'id'),
#         ('expires', 'expires')
#     ]

#     def get_user_details(self, response):
#         """Return user details from GitHub account"""
#         return {'username': response.get('login'),
#                 'email': response.get('email') or '',
#                 'first_name': response.get('name')}

#     def user_data(self, access_token, *args, **kwargs):
#         """Loads user data from service"""
#         url = 'https://api.github.com/user?' + urlencode({
#             'access_token': access_token
#         })
#         return self.get_json(url)