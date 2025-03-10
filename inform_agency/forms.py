from django import forms
from app.models import Newspaper

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'content', 'published_date', 'topic', 'publishers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
