from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from django.utils import timezone
from .managers import UsersManager
from core.models import CreateModel

class User(AbstractBaseUser, PermissionsMixin, CreateModel):
    full_name = models.CharField(_('Full name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    mobile_phone = models.CharField(_('mobile phone'), max_length=11, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = jmodels.jDateTimeField(_("last login"), default=timezone.now())

    objects = UsersManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name', 'mobile_phone')
    
    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True
    
    @property
    def is_admin(self):
        return self.is_staff
    


class RecycleUser(User):
    class Meta:
        proxy = True