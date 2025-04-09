from django import forms

class UniversityForm(forms.Form):

    SUBJECT_CHOICES = (
        (1, 'Web Development'),
        (2, 'Systems Programming'),
        (3, 'Data Science'),
)

    name = forms.CharField()
    age = forms. IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    date_of_birth = forms.DateField()


