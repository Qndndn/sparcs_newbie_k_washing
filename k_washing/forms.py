from django import forms
from k_washing.models import k_washing, k_washing_state


class k_washingForm(forms.ModelForm):
    class Meta:
        model = k_washing
        fields = ['floor','direction']
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control mt-2", "rows": 20}),
        }
        labels = {
            'floor': '층수',
            'direction': '방향',
            'time': '세탁시간',
            'content': '하고 싶은 말',
        }

class k_washing_stateForm(forms.ModelForm):
    class Meta:
        model = k_washing_state
        fields = [ 'floor_1', 'direction_1', 'time_first', 'state', 'pk_1']
