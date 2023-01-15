from django.contrib.auth.backends import BaseBackend
from .models import Utilisateur2

class CustomAuthBackend(BaseBackend):
    def authenticate(request, username=None, password=None, **kwargs):
        try:
            user = Utilisateur2.objects.get(Email=username)
            if user.Password == password :
                request.session['user'] = user.id
                print(request.session.get('user'))
                return user
        except Utilisateur2.DoesNotExist:
            return None


