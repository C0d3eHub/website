from django.shortcuts import render, redirect,get_object_or_404
from .models import (
    NewsAlert, PrincipalDesk, AboutInstituteContent, 
    AdminStaff, TechStaff, HeaderContent,SliderImage,ElectricPowerSupply,KeyPerformanceIndicatorContent
)
from .forms import (
    NewsAlertForm, PrincipalDeskForm, 
    AboutInstituteForm, HeaderContentForm,SliderImageForm,KeyPerformanceIndicatorForm
)
from django.core.mail import send_mail
from django.contrib import messages
from .utils import get_header_content
from django.utils import timezone
from .forms import TraineeDetailsForm
from .models import TraineeDetails
from django.contrib.auth.decorators import user_passes_test
import pandas as pd
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


# Header content view
def header_content_view(request):
    header_content = HeaderContent.objects.first()
    if request.method == 'POST':
        form = HeaderContentForm(request.POST, request.FILES, instance=header_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Header content updated successfully.')
            return redirect('header_content')
    else:
        form = HeaderContentForm(instance=header_content)

    context = {
        'form': form,
        'header_content': header_content
    }
    return render(request, 'admin/header_content.html', context)

# Index view: Fetch latest news and principal desk posts
def index(request):
    news_alerts = NewsAlert.objects.all().order_by('-published_date')[:5]
    principal_desk_posts = PrincipalDesk.objects.all().order_by('-published_date')[:5]
    images = SliderImage.objects.all()  # Fetch all slider images
    
    # Fetch header content
    header_content = get_header_content()
    page_title = "Govt ITI Krishangarh"    

    # Pass 'images' to the template context
    return render(request, 'index.html', {
        'news_alerts': news_alerts,
        'principal_desk_posts': principal_desk_posts,
        'header_content': header_content,
        'images': images,  # Add images to the context
        'page_title': page_title,
    })



# Contact page view
from .models import ContactForm  # Import the model
def contact(request):
    header_content = get_header_content()  # Ensure header content is fetched
    page_title = "Contact Us"

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact form data to the database
        contact_entry = ContactForm(name=name, email=email, message=message)
        contact_entry.save()

        # Send email logic
        try:
            send_mail(
                subject='Contact Form Submission',
                message=message,
                from_email=email,
                recipient_list=['shekhar.sharma36@gmail.com'],  # Change this to your email
                fail_silently=False,
            )
            messages.success(request, 'Email sent successfully. Reloading this page in 10 seconds.')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return redirect('contact')  # This should match the URL name for your contact page

    return render(request, 'contact.html', {'header_content': header_content, 'page_title': page_title})

# News list view
def news_list(request):
    news_alerts = NewsAlert.objects.all().order_by('-published_date')
    header_content = get_header_content()
    return render(request, 'news_list.html', {
        'news_alerts': news_alerts,
        'header_content': header_content,
    })

# Principal desk list view
def principal_desk_list(request):
    principal_desk_posts = PrincipalDesk.objects.all().order_by('-published_date')
    header_content = get_header_content()
    return render(request, 'principal_desk_list.html', {
        'principal_desk_posts': principal_desk_posts,
        'header_content': header_content,
    })

# View for creating a new news alert
def create_news_alert(request):
    if request.method == 'POST':
        form = NewsAlertForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'News alert created successfully.')
            return redirect('news_list')
    else:
        form = NewsAlertForm()
    header_content = get_header_content()
    return render(request, 'create_news_alert.html', {'form': form, 'header_content': header_content})






# Admission page
def admission(request):
    header_content = get_header_content()
    page_title = "Admissoin" 
    
    return render(request, 'admission.html', {'header_content': header_content, 'page_title':page_title})

# Electric Power Supply page
def electric_power_supply(request):
    header_content = get_header_content()
    page_title = "Electric Power Supply"
    power_supplies = ElectricPowerSupply.objects.all()  # Fetch all electric power supply entries
    return render(request, 'electric_power_supply.html', {
        'header_content': header_content,
        'page_title': page_title,
        'power_supplies': power_supplies,  # Add the power supply data to context
    })




# Key Performance Indicator page
def key_performance_indicator_view(request):
    header_content = get_header_content()  # Fetch your header content
    kpi_content = KeyPerformanceIndicatorContent.objects.first()  # Fetch the first KPI content
    page_title = "Key Performance Indicator"  # Set the page title

    context = {
        'header_content': header_content,
        'kpi_content': kpi_content, 
        'page_title': page_title,  # Add the page title to context
    }

    return render(request, 'key_performance_indicator.html', context)

#about Institute
def about_institute_view(request):
    
    header_content = get_header_content()  # Fetch your header content
    about_content = AboutInstituteContent.objects.first()  # Fetch the first KPI content
    page_title = "About Institute"  # Set the page title

    context = {
        'header_content': header_content,
        'about_content': about_content, 
        'page_title': page_title,  # Add the page title to context
    }

    return render(request, 'about_institute.html', context)
#profile in anout
from .models import Profile

def about_institute_view(request):
    header_content = get_header_content()  # Fetch your header content
    about_content = AboutInstituteContent.objects.first()  # Fetch the first KPI content
    profiles = Profile.objects.all()  # Fetch all profiles
    page_title = "About Institute"  # Set the page title

    context = {
        'header_content': header_content,
        'about_content': about_content,
        'profiles': profiles,
        'page_title': page_title,  # Add the page title to context
    }

    return render(request, 'about_institute.html', context)

# Institute Amenities page
def institute_amenities(request):
    header_content = get_header_content()
    page_title = "Institute Anenities"
    return render(request, 'institute_amenities.html', {'header_content': header_content, 'page_title':page_title})
#photo gallery




# Institute Infrastructure page
from django.shortcuts import render
from .models import InstituteInfrastructure

def institute_infrastructure(request):
    header_content = get_header_content()
    page_title = "Institute infrastructure"
    infrastructure_data = InstituteInfrastructure.objects.all()  # Fetch all records
    return render(request, 'institute_infrastructure.html', {'infrastructure_data': infrastructure_data,'header_content': header_content, 'page_title':page_title })


   
    
    return render(request, 'institute_infrastructure.html', {'header_content': header_content, 'page_title':page_title})

# Trades page
def trades(request):
    header_content = get_header_content()
    page_title = "Trades"
    return render(request, 'trades.html', {'header_content': header_content,'page_title':page_title})

# Admission Criteria page

from django.shortcuts import render
from .models import AdmissionCriteria

def admission_criteria(request):
    # Fetch the content for the admission criteria
    criteria = AdmissionCriteria.objects.first()  # Assuming there's only one record
    header_content = get_header_content()  # Get the header content
    page_title = "Admission Criteria"  # Set the page title
    
    # Render the template with the fetched data
    return render(request, 'admission_criteria.html', {
        'criteria': criteria,
        'header_content': header_content,
        'page_title': page_title
    })
# Trades NCVT page
from .models import NCVTTrade

def trades_ncvt(request):
    # Fetch filter value from the request
    filter_value = request.GET.get('affiliated_to', 'all')  # Default to 'all'

    # If a filter is applied, filter the trades based on the selected 'affiliated_to' value
    if filter_value == 'all':
        trades = NCVTTrade.objects.all()
    else:
        trades = NCVTTrade.objects.filter(affiliated_to=filter_value)

    header_content = get_header_content()
    page_title = "NCVT Trades"

    return render(request, 'trades_ncvt.html', {
        'trades': trades,
        'header_content': header_content,
        'page_title': page_title,
        'filter_value': filter_value
    })
# Overall Results page
def overall_results(request):
    header_content = get_header_content()
    page_title = "Over all Result"
    return render(request, 'overall_results.html', {'header_content': header_content,'page_title':page_title})

# Trade-wise Results page
def trade_wise_result(request):
    header_content = get_header_content()
    page_title = "Trade wise Result"
    return render(request, 'trade_wise_result.html', {'header_content': header_content,'page_title':page_title})

# Session-wise Results page
def session_wise_result(request):
    page_title = "Session wise result"
    header_content = get_header_content()
    return render(request, 'session_wise_result.html', {'header_content': header_content,'page_title':page_title})

# Trade Infrastructure page
from django.shortcuts import render
from .models import InstituteInfrastructure

def trade_infrastructure(request):
    trade_filter = request.GET.get('trade', 'all')  # Default to 'all' if no filter is applied
    header_content = get_header_content()
    page_title = "Trade Infrastructure"
    if trade_filter == 'all':
        # Fetch all data
        infrastructures = InstituteInfrastructure.objects.all()
    else:
        # Filter by selected trade (COPA or MMV)
        infrastructures = InstituteInfrastructure.objects.filter(trade=trade_filter)

    # Pass data to the template
    return render(request, 'trade_infrastructure.html', {
        'infrastructures': infrastructures,
        'trade_filter': trade_filter,
        'header_content': header_content,'page_title':page_title
    })
# Placement page

from django.shortcuts import render
from .models import Placement

def placement(request):
    header_content = get_header_content()
    page_title = "Placement"
    
    # Fetching all placement data
    placements = Placement.objects.all()
    
    return render(request, 'placement.html', {
        'header_content': header_content,
        'page_title': page_title,
        'placements': placements
    })


# Extra-curricular Activities page
# views.py
from django.shortcuts import render
from .models import ECA

def eca(request):
    header_content = get_header_content()
    page_title = "Extra Curricular Activities"
    activities = ECA.objects.all()
    
    return render(request, 'eca.html', {
        'header_content': header_content,
        'page_title': page_title,
        'activities': activities
    })


# Administrative Staff page: Fetch and display all staff members
def adminstaff(request):
    staff_members = AdminStaff.objects.all()
    header_content = get_header_content()
    page_title = "Admin Staff"  
    return render(request, 'adminstaff.html', {
        'staff_members': staff_members,
        'header_content': header_content,
         'page_title': page_title, 
    })

# Technical Staff page
def techstaff(request):
    tech_staff_list = TechStaff.objects.all()
    header_content = get_header_content()
    return render(request, 'techstaff.html', {
        'tech_staff_list': tech_staff_list,
        'header_content': header_content,
    })

# RTI page
# views.py
from django.shortcuts import render
from .models import RTI

def rti(request):
    # Fetch all RTI records from the database
    rti_data = RTI.objects.all()
    
    # Pass the data to the template
    header_content = get_header_content()
    return render(request, 'rti.html', {
        'header_content': header_content,
        'rti_data': rti_data,
    })


# Apprenticeship Training Scheme (ATS) page
# views.py
from django.shortcuts import render
from .models import ApprenticeshipSection

def ats(request):
    # Fetch the section data from the database
    sections = ApprenticeshipSection.objects.all()  # Get all sections
    header_content = get_header_content()
    return render(request, 'ats.html', {
        'header_content': header_content,
        'sections': sections,
    })


# Craftsman Training Scheme (CTS) page
from django.shortcuts import render
from .models import CTSContent

def cts(request):
    header_content = get_header_content()
    content = CTSContent.objects.all()  # Fetch all the CTS content
    page_title = "Craftsman Training Scheme"
    
    return render(request, 'cts.html', {
        'header_content': header_content,
        'content': content,
        'page_title': page_title,
    })


# IMC page
# views.py
# views.py
from django.shortcuts import render
from .models import CommitteeMember, Achievement

def imc(request):
    header_content = get_header_content()
    committee_members = CommitteeMember.objects.all()  # Fetch all committee members
    achievement = Achievement.objects.first()  # Fetch the first achievement
    return render(request, 'imc.html', {
        'header_content': header_content,
        'committee_members': committee_members,
        'achievement': achievement
    })



# HPKVN page
from django.shortcuts import render
from .models import HPKVNTrainingProgram, HPKVNEnrollmentProcess, HPKVNPlacement, HPKVNTrainee

# View for HPKVN Main Page
def hpkvn(request):
    # Fetch data for all sections
    header_content = get_header_content()
    training_programs = HPKVNTrainingProgram.objects.all()
    enrollment_process = HPKVNEnrollmentProcess.objects.all()
    placements = HPKVNPlacement.objects.all()
    trainees = HPKVNTrainee.objects.all()

    return render(request, 'hpkvn.html', {
        'training_programs': training_programs,
        'enrollment_process': enrollment_process,
        'placements': placements,
        'trainees': trainees,
        'header_content':header_content,
    })



# On Job Training (OJT) page
from django.shortcuts import render
from .models import OJTContent
from .models import OJTTrainee
def ojt(request):
    header_content = get_header_content()  # Assuming you have a header function
    ojt_content = OJTContent.objects.first()  # You can fetch the content to display
    trainees = OJTTrainee.objects.all()
    
    return render(request, 'ojt.html', {
        'header_content': header_content,
        'ojt_content': ojt_content,
        'trainees': trainees
    })

#imagesbackground Upload for slider


def upload_slider_image(request):
    if request.method == 'POST':
        form = SliderImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_slider_image')  # Redirect after successful upload
    else:
        form = SliderImageForm()

    # Handle delete request (if needed)
    if request.method == 'POST' and 'delete_image' in request.POST:
        image_id = request.POST.get('image_id')
        image = get_object_or_404(SliderImage, id=image_id)
        image.delete()
        return redirect('upload_slider_image')

    images = SliderImage.objects.all()  # Retrieve all uploaded images
    return render(request, 'admin/upload_slider_image.html', {'form': form, 'images': images})

# industry_collaboration
# views.py
from django.shortcuts import render
from .models import IndustryCollaboration

def industry_collaboration(request):
    # Fetch the filter value from GET request
    mou_signed_filter = request.GET.get('mou_signed', 'all')
    
    # Apply filter if any, otherwise fetch all records
    if mou_signed_filter == 'Yes':
        collaborations = IndustryCollaboration.objects.filter(mou_signed='Yes')
    elif mou_signed_filter == 'No':
        collaborations = IndustryCollaboration.objects.filter(mou_signed='No')
    else:
        collaborations = IndustryCollaboration.objects.all()

    header_content = get_header_content()  # Assuming you use header content
    page_title = "Industry Collaboration"
    
    return render(request, 'industry.collaboration.html', {
        'header_content': header_content,
        'page_title': page_title,
        'collaborations': collaborations,
        'mou_signed_filter': mou_signed_filter,  # Pass the filter value
    })


# Inspection page view
# views.py
from django.shortcuts import render
from .models import Inspection

def inspection(request):
    inspections = Inspection.objects.all()  # Fetch all inspection records
    header_content = get_header_content()
    page_title = "Inspection"  # Set the relevant page title
    return render(request, 'inspection.html', {
        'header_content': header_content,
        'page_title': page_title,
        'inspections': inspections,
    })

#trainees
def trainee_view(request):
    header_content = get_header_content()
    page_title = "Trainees"
    return render(request, 'trainees.html',{'header_content': header_content, 'page_title':page_title})

from django.contrib import admin
#database
@user_passes_test(lambda u: u.is_superuser)
def upload_trainee_details(request):
    if request.method == 'POST':
        form = TraineeDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect after saving
    else:
        form = TraineeDetailsForm()

    return render(request, 'upload_trainee.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def bulk_upload_trainees(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        try:
            data = pd.read_excel(file)  # Ensure pandas and openpyxl are installed
            for _, row in data.iterrows():
                TraineeDetails.objects.create(
                    sn=row['sn'],
                    name=row['name'],
                    fathername=row['fathername'],
                    mothername=row['mothername'],
                    address=row['address'],
                    phoneno=row['phoneno'],
                    aadharcard=row['aadharcard'],
                    trade=row['trade'],
                    session=row['session'],
                    result=row['result'],
                    remarks=row['remarks']
                )
            messages.success(request, 'Trainee details uploaded successfully!')
        except Exception as e:
            messages.error(request, f'Error uploading data: {str(e)}')
        return redirect('admin:bulk_upload_trainees')  # Change to the correct redirect

    return render(request, 'admin/bulk_upload.html')  # Ensure the template path is correct


from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import GalleryImageForm
from .utils import get_header_content  # Import the helper function if it's in a separate utils file

def gallery_view(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Photos"
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images, 'header_content': header_content,'page_title':page_title})


def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'upload_image.html', {'form': form})





@staff_member_required  # Ensure only admin can access this
def bulk_upload_trainees(request):
    return render(request, 'admin/bulk_upload.html')
def trainee_list(request):
    header_content = get_header_content()
    trainees = TraineeDetails.objects.all()  # Retrieve all trainee records
    return render(request, 'trainees.html', {'trainees': trainees,'header_content': header_content})
# views.py
from django.shortcuts import render
from .models import Trade
from .models import Trade 
def trades_view(request):
    trades = Trade.objects.all()  # Fetch all trades from the database
    header_content = get_header_content()  # Get header content (adjust if necessary)
    
    # Return the response, passing both the trades and header_content to the template
    return render(request, 'trades.html', {'trades': trades, 'header_content': header_content})


from django.shortcuts import render
from .models import TraineeDetails

def overall_results(request):
    # Get all the possible values of the result column
    results = ['pass', 'fail', 'reappear', 'all']  # Added 'all' as an option
    header_content = get_header_content()

    # Default to show all trainees if no result is selected
    selected_result = request.GET.get('result', 'all')  # Default value is 'all'

    # If 'all' is selected, return all data
    if selected_result == 'all':
        trainees = TraineeDetails.objects.all()
    else:
        # Otherwise, filter based on selected result (case-sensitive)
        trainees = TraineeDetails.objects.filter(result__iexact=selected_result)  # Use `iexact` for case-insensitive matching

    context = {
        'results': results,
        'trainees': trainees,
        'selected_result': selected_result,
        'header_content': header_content
    }
    return render(request, 'overall_results.html', context,)

def trade_wise_result(request):
    # Get all the distinct trades from the TraineeDetails model
    trades = TraineeDetails.objects.values_list('trade', flat=True).distinct()  # Get unique trades
    trades = list(trades)  # Convert to a list for easier access in the template
    trades.insert(0, 'all')  # Add 'all' as an option at the beginning

    header_content = get_header_content()
    
    # Default to 'all' if no trade is selected
    selected_trade = request.GET.get('trade', 'all')  # Default value is 'all'

    # If 'all' is selected, return all data
    if selected_trade == 'all':
        trainees = TraineeDetails.objects.all()
    else:
        # Otherwise, filter based on selected trade
        trainees = TraineeDetails.objects.filter(trade=selected_trade)

    context = {
        'trades': trades,
        'trainees': trainees,
        'selected_trade': selected_trade,
        'header_content': header_content
    }

    return render(request, 'trade_wise_result.html', context)

from django.shortcuts import render
from .models import TraineeDetails, Trade
from .utils import get_header_content  # Import the function to get header content

def session_wise_result(request):
    # Get all the distinct values for session and trade
    sessions = TraineeDetails.objects.values_list('session', flat=True).distinct()
    trades = Trade.objects.all()

    selected_session = request.GET.get('session')
    selected_trade = request.GET.get('trade', 'all')

    if selected_session:
        # If a session is selected, filter trainees by session
        trainees = TraineeDetails.objects.filter(session=selected_session)
        if selected_trade != 'all':
            # If a trade is selected, further filter by trade
            trainees = trainees.filter(trade=selected_trade)
    else:
        trainees = TraineeDetails.objects.none()

    # Fetch the header content
    header_content = get_header_content()

    context = {
        'sessions': sessions,
        'trades': trades,
        'trainees': trainees,
        'selected_session': selected_session,
        'selected_trade': selected_trade,
        'header_content': header_content  # Pass header content to the template
    }
    return render(request, 'session_wise_result.html', context)
from django.shortcuts import render
from .models import InstituteAmenity

def institute_amenities(request):
    header_content = get_header_content()
    amenities = InstituteAmenity.objects.all()  # Fetch all records
    return render(request, 'institute_amenities.html', {'amenities': amenities,'header_content': header_content})
