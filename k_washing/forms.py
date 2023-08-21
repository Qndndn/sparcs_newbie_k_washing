from django import forms
from k_washing.models import k_washing


class k_washingForm(forms.ModelForm):
    class Meta:
        model = k_washing
        fields = ['direction', 'floor']
    
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control mt-2", "rows": 20}),
        }
        labels = {
            'floor': '층수',
            'direction': '방향',
            'time': '세탁시간',
            'content': '하고 싶은 말',
        }
