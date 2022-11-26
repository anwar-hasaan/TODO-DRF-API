from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from uuid import uuid4
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, fullname, picture=None, password=None, password2=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email=email),
                        fullname=fullname, picture=picture)
        user.uid = str(uuid4())
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, picture=None, password=None, password2=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.create_user(
            email=self.normalize_email(email=email), fullname=fullname,
            password=password, picture=picture)
        user.uid = str(uuid4())
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    uid = models.UUIDField(unique=True, null=True, blank=True, editable=True)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    fullname = models.CharField(verbose_name='full name', max_length=50)
    picture = models.ImageField(verbose_name='profile picture', upload_to='profile_pic/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    # def save(self, *args, **kwargs):
    #     self.uid = str(uuid4())
    #     return super().save(self, *args, **kwargs)

STATUS = (
    ('pending', 'pending'),
    ('complete', 'complete'),
    ('overdue', 'overdue')
)
class Todo(models.Model):
    uid = models.UUIDField(unique=True, default=uuid4, editable=True)
    user_id = models.CharField(max_length=5)
    dev_ref = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=15)
    due_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task