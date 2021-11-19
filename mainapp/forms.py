from django.forms import ModelForm, fields
from .models import Navigation


class NavigationForm(ModelForm):
    class Meta:
        model = Navigation
        fields = "__all__"

