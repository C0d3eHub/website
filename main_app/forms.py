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
        fields = '__all__'  # This will automatically include all fields, including 'right_logo'
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



from django import forms
from .models import TraineeDetails

class TraineeDetailsForm(forms.ModelForm):
    class Meta:
        model = TraineeDetails
        fields = [
            'name', 
            'fathername', 
            'mothername', 
            'gender',  
            'address', 
            'phoneno', 
            'aadharcard', 
            'trade', 
            'session', 
            'result', 
            'photo',             
            'highest_qualification', 
            'marks_10th', 
            'marks_12th', 
            'hobbies', 
            'work_experience',
            'remarks',
        ]
        widgets = {
            'trade': forms.Select(choices=TraineeDetails.TRADE_CHOICES),
            'result': forms.Select(choices=TraineeDetails.RESULT_CHOICES),
            'session': forms.Select(choices=TraineeDetails.SESSION_CHOICES),
            'gender': forms.Select(choices=TraineeDetails.GENDER_CHOICES), 
            'remarks': forms.Textarea(attrs={'rows': 3}),
            'hobbies': forms.Textarea(attrs={'rows': 3}),
            'work_experience': forms.Textarea(attrs={'rows': 3}),
        }

    # You could optionally include a custom method to display the ID (if needed):
    def clean_trainee_id(self):
        return self.instance.trainee_id  # Ensure that the trainee_id is not editable

        
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
        #formformarks



#grienvence
from django import forms
from .models import Grievance

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your grievance'}),
        }
#chairman
# forms.py
from django import forms
from .models import Chairman

class ChairmanForm(forms.ModelForm):
    class Meta:
        model = Chairman
        fields = ['name', 'position', 'message', 'image']


#online test
from django import forms
from .models import TradeForOnlineTest, TopicForOnlineTest

class TestSelectionForm(forms.Form):
    trade = forms.ModelChoiceField(queryset=TradeForOnlineTest.objects.all(), label="Select Trade")
    topic = forms.ModelChoiceField(queryset=TopicForOnlineTest.objects.all(), label="Select Topic")
    num_questions = forms.ChoiceField(choices=[(5, '5'), (10, '10'), (25, '25'), (50, '50')], label="Number of Questions")
#tender
