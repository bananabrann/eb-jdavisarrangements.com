from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select an audio file',
        help_text='Must be mp3 format'
    )