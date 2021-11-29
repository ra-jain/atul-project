from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an Email address")
        if not username:
            raise ValueError("Users must have a username")
        if not first_name:
            raise ValueError("Users must have a First Name")
        if not last_name:
            raise ValueError("Users must have a Last Name")
        # if not phone_number:
        #     raise ValueError("Users must have a Phone number")
        
        user =  self.model(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
                # phone_number=phone_number
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name,
            # phone_number = phone_number
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # general user
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(max_length=60, unique=True)
    # phone_number = models.CharField(verbose_name = 'phone',name = 'Phone No.', max_length=15, null = True)
    # autogenerate
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    # refer this again for admin verification for new users
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # refer for admin
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
