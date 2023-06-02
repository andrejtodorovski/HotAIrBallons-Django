from django import forms
from .models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"