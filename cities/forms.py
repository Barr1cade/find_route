from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города'
    }))
    station = forms.CharField(label='Вокзал', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название вокзала'
    }))
    platform = forms.CharField(label='Путь номер', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название платформы'
    }))

    class Meta:
        model = City
        fields = ('name', 'station', 'platform',)
