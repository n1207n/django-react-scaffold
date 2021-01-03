import re

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class UserManager(BaseUserManager):
    """
    Based on Django's original UserManager.
    """

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The given email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, SoftDeletableModel, TimeStampedModel):
    """
    Customized User model based on Django's original User.
    """

    username = models.CharField(_('username'), max_length=30,
                                help_text=_('30 characters or fewer. Letters, numbers and '
                                '@/./+/-/_ characters'),
                                validators=[
                                    validators.RegexValidator(
                                        re.compile(r'^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
                                ], blank=True, default='')
    email = models.EmailField(_('email'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_('Designates whether this user should be treated as '
                                    'active. Unselect this instead of deleting user.'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_username()

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def email_user(self, subject, message, from_email=None, **kwargs):  # pragma: no cover
        """Sends an email to this User [upstream AbstractUser method]."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Account(TimeStampedModel, SoftDeletableModel):
    """
    Represent User account
    """
    user = models.ForeignKey(
        'account.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='accounts',
        verbose_name=_('account')
    )
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_('Designates whether this user should be treated as '
                                    'active. Unselect this instead of deleting account.'))

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def __str__(self):
        return self.get_username()
