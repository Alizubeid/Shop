from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment","score"]

    def __init__(self, *args, **kwargs):
        super(CommentForm,self).__init__(*args, **kwargs)
        self.fields["comment"].widget.attrs["placeholder"] = "comment"
        self.fields["score"].widget.attrs["placeholder"] = "score"
        