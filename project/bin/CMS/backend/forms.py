from django import forms


class FormBody(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={"class": "input_top"}))
    name_id = forms.CharField(widget=forms.Textarea(attrs={"class": "input_center"}))
    all_body = forms.CharField(widget=forms.Textarea(attrs={"class": "input_body"}))
