from django import forms

class FeedBackForm(forms.Form):
    email = forms.EmailField(label="Enter Your email address")
    name = forms.CharField(max_length=100, label="Enter Your name")
    feedback = forms.CharField(label="Your Feedback", widget= forms.Textarea )


    def __init__(self, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'