from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication


class SimpleAuthentication(BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get('Username', '')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        return (user, None)
