from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Fieldset
from crispy_forms.bootstrap import FormActions
from models import Article

class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Edit Article' if self.instance.pk else 'Create Article',
                Field('title', css_class="span2"),
                Field('text', css_class="span4"),
            ),
            FormActions(
                Submit('submit', 'Save', css_class="btn-primary")
            )
        )    

    class Meta:
        model = Article