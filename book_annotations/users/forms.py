from django.contrib.auth.forms import UserCreationForm as _UserCreationForm
from django.conf import settings
from users.models import User


class UserCreationForm(_UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
