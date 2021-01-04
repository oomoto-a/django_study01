from django import forms

CHOICE = {
    ('m','男'),
    ('f','女'),
    ('n','不明'),
}
class UserForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    sex = forms.ChoiceField(label='性別', widget=forms.RadioSelect, choices=CHOICE, initial=2)
    feature = forms.CharField(label='特徴', max_length=100)