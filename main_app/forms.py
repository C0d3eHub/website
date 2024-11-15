from django import forms
from .models import TraineeDetails, NewsAlert , PrincipalDesk, AboutInstituteContent,HeaderContent,SliderImage, KeyPerformanceIndicatorContent

class NewsAlertForm(forms.ModelForm):
    class Meta:
        model = NewsAlert
        fields = ['title', 'content', 'attachment']  # Include attachment field
class PrincipalDeskForm(forms.ModelForm):
    class Meta:
        model = PrincipalDesk
        fields = ['title', 'content']


from django import forms




class HeaderContentForm(forms.ModelForm):
    class Meta:
        model = HeaderContent
        fields = '__all__'
class SliderImageForm(forms.ModelForm):
    class Meta:
        model = SliderImage
        fields = ['image', 'caption']
from django import forms
from .models import KeyPerformanceIndicatorContent

class KeyPerformanceIndicatorForm(forms.ModelForm):
    class Meta:
        model = KeyPerformanceIndicatorContent
        fields = ['header', 'description', 'updated_at']  # Include 'updated_at' to allow manual updates
class AboutInstituteForm(forms.ModelForm):
    class Meta:
        model = AboutInstituteContent
        fields = ['header', 'description', 'updated_at']  # Include 'updated_at' to allow manual updates



class TraineeDetailsForm(forms.ModelForm):
    class Meta:
        model = TraineeDetails
        fields = ['name', 'fathername', 'mothername', 'address', 'phoneno', 'aadharcard', 'trade', 'session', 'result', 'photo', 'remarks']
        widgets = {
            'trade': forms.Select(choices=TraineeDetails.TRADE_CHOICES),
            'result': forms.Select(choices=TraineeDetails.RESULT_CHOICES),
            'session': forms.Select(choices=TraineeDetails.SESSION_CHOICES),
        }
        
from django import forms
from .models import GalleryImage

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'image']
from django import forms
from .models import OJTContent

class OJTContentForm(forms.ModelForm):
    class Meta:
        model = OJTContent
        fields = ['link_1_text', 'div_1_content', 'link_2_text', 'div_2_content', 'link_3_text', 'div_3_content']
        widgets = {
            'link_1_text': forms.TextInput(attrs={'placeholder': 'Link 1 Text'}),
            'div_1_content': forms.Textarea(attrs={'placeholder': 'Content for Div 1'}),
            'link_2_text': forms.TextInput(attrs={'placeholder': 'Link 2 Text'}),
            'div_2_content': forms.Textarea(attrs={'placeholder': 'Content for Div 2'}),
            'link_3_text': forms.TextInput(attrs={'placeholder': 'Link 3 Text'}),
            'div_3_content': forms.Textarea(attrs={'placeholder': 'Content for Div 3'}),
            
        }
