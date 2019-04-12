from django import forms
from subject.models import subjects

class Add_subject(forms.ModelForm):

    class Meta:
        model = subjects
        fields = "__all__"

