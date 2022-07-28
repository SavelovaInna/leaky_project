from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class MyAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        query = f'SELECT id FROM auth_user WHERE username = "{username}" AND password="{password}"'
        query = f'SELECT id FROM auth_user WHERE username = %s AND password=%s'
        try:
            return User.objects.raw(query, username, password)[0]
        except Exception as e:
            return

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
