from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager


class Role(models.TextChoices):
    ADMIN = 'admin', 'Администратор'
    USER = 'user', 'Пользователь'


class User(AbstractBaseUser):
    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'image']

    # также для работы модели пользователя должен быть переопределен менеджер объектов
    objects = UserManager()

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=9, choices=Role.choices, default=Role.USER)
    image = models.ImageField(upload_to='user_avatars/', null=True, blank=True)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    #  методы is_admin и is_user в данном случае являются аналогами проверки прав доступа
    #  (permissions) для конкретного пользователя
    @property
    def is_admin(self):
        return self.role == Role.ADMIN

    @property
    def is_user(self):
        return self.role == Role.USER

    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
