from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        # 指定使用哪一个模型创建Meta类中的表单
        model = Comment
        # 通过fields字段可以显示的通知希望在表单中包含哪些字段
        fields = ('name', 'email', 'body')
