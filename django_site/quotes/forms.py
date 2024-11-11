from django import forms
from .models import Author, Tag, Quote
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Fullname'}),
            'born_date': forms.DateInput(attrs={'type': 'date'}),
            'born_location': forms.TextInput(attrs={'placeholder': 'Born Location'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
        }

    def clean_fullname(self):
        fullname = self.cleaned_data.get("fullname")
        if Author.objects.filter(fullname=fullname).exists():
            raise ValidationError("An author with this name already exists.")
        return fullname

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tag name'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Tag.objects.filter(name=name).exists():
            raise ValidationError("A tag with this name already exists.")
        return name

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'quote', 'tags']

        widgets = {
            'author': forms.Select(attrs={'placeholder': 'Author'}),
            'quote': forms.Textarea(attrs={'placeholder': 'Quote'}),
            'tags': forms.SelectMultiple(attrs={'placeholder': 'Select tags', 'class': 'form-control'}),
        }

