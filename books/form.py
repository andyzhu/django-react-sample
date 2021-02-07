from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'description', 'image']
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 300:
            raise forms.ValidationError('The description is too long')
        return description
