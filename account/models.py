from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Модель профиль пользователя
    attr:
        user,
        date-of_birth,
        photo
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True
    )
    def __str__(self) -> str:
        return f'Profile of {self.user.username}'


# class AbstractUser(User):
#     pass