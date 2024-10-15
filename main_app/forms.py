from django import forms
from .models import NewsAlert , PrincipalDesk, AboutInstitute,HeaderContent,SliderImage


class NewsAlertForm(forms.ModelForm):
    class Meta:
        model = NewsAlert
        fields = ['title', 'content', 'attachment']  # Include attachment field
class PrincipalDeskForm(forms.ModelForm):
    class Meta:
        model = PrincipalDesk
        fields = ['title', 'content']


class AboutInstituteForm(forms.ModelForm):
    class Meta:
        model = AboutInstitute
        fields = ['title', 'description']  # Include the fields you want

        # Optionally, you can add custom widgets here to apply CSS classes
        widgets = {
            'title': forms.TextInput(attrs={'class': 'about-institute-title'}),
            'description': forms.Textarea(attrs={'class': 'about-institute-description'}),
        }
class HeaderContentForm(forms.ModelForm):
    class Meta:
        model = HeaderContent
        fields = '__all__'
class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage
        fields = ['image', 'caption']