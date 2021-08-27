from django.db import models
from django.contrib.auth.models import User

# edit email field in User model
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False


class Message(models.Model):
    """Model for create a messages"""

    text = models.TextField(max_length=99)
    owner = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return 'Message: %s' % self.id
