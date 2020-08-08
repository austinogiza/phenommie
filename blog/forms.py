from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={

        "placeholder": 'Leave a comment',
        'class': 'form-textarea'
    }))
