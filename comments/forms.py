from django import forms
from tinymce.widgets import TinyMCE
from .models import Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CommentForm(forms.ModelForm):
    comment_wiki = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Comment
        fields = ['comment_wiki']

    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id', None)
        self.name = kwargs.pop('name', None)
        super(CommentForm, self).__init__(*args, **kwargs)
