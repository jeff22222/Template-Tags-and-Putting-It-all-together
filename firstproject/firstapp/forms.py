from django import forms
from firstapp.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','author','message']
        widgets={
            'title': forms.TextInput(attrs={'placeholder':'Enter the title of your post','class':'form-control'}),
            'author': forms.TextInput(attrs={'placeholder':'What is your name?','class':'form-control'}),
            'message': forms.Textarea(attrs={'placeholder':'What are you posting about','class':'form-control'}), 
        }