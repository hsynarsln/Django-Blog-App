from django.contrib.auth.forms import UserCreationForm

from .models import User


#! UserCreationForm --> otomatik olarak validation'lar geliyor.
class UserForm(UserCreationForm):
    class Meta():
        model = User
        # fields = '__all__'
        fields = ('username', 'email', 'password1', 'password2',
                  'portfolio', 'profile_pic', 'first_name', 'last_name')
        # exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', )
