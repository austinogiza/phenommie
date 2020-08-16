from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={

        "placeholder": 'Leave a comment',
        'class': 'form-textarea'
    }))
