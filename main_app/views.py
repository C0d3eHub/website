from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.http import JsonResponse
import pandas as pd


# Models
from .models import (
    NewsAlert, PrincipalDesk, AboutInstituteContent, AdminStaff, TechStaff,
    HeaderContent, SliderImage, ElectricPowerSupply, KeyPerformanceIndicatorContent,
    TraineeDetails, ContactForm, InstituteInfrastructure, IndustryCollaboration,
    OJTContent, OJTTrainee, HPKVNTrainingProgram, HPKVNEnrollmentProcess,
    HPKVNPlacement, HPKVNTrainee, CommitteeMember, Achievement, CTSContent,
    ApprenticeshipSection, RTI, ECA, Placement, NCVTTrade, AdmissionCriteria,
    Stream, Video, Meeting, Testimonial, Marks, Trade, GalleryImage, InstituteAmenity,
    Inspection,ReachUsContent,VisitorCounter,Grievance,Chairman
)

# Forms
from .forms import (
    NewsAlertForm, PrincipalDeskForm, AboutInstituteForm, HeaderContentForm,
    SliderImageForm, KeyPerformanceIndicatorForm, TraineeDetailsForm, GalleryImageForm,GrievanceForm,ChairmanForm
)

# Utilities
from .utils import get_header_content

#view for qpr
# views.py
from django.shortcuts import render

def qpr_view(request):
    return render(request, 'qpr.html')

# Header content view
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HeaderContent
from .forms import HeaderContentForm  # Make sure your form includes right_logo

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


def contact(request):
    header_content = get_header_content()  # Ensure header content is fetched
    page_title = "Contact Us"

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # Get phone number from POST data
        message = request.POST.get('message')

        # Save the contact form data to the database
        contact_entry = ContactForm(name=name, email=email, phone=phone, message=message)
        contact_entry.save()

        # Send email logic
        try:
            send_mail(
                subject='Contact Form Submission',
                message=f"Message: {message}\nPhone: {phone}",  # Include phone in email
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


def institute_infrastructure(request):
    header_content = get_header_content()
    page_title = "Institute infrastructure"
    infrastructure_data = InstituteInfrastructure.objects.all()  # Fetch all records
    return render(request, 'institute_infrastructure.html', {'infrastructure_data': infrastructure_data,'header_content': header_content, 'page_title':page_title })


   
    
    return render(request, 'institute_infrastructure.html', {'header_content': header_content, 'page_title':page_title})

# Trades page


# Admission Criteria page



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


# Trade-wise Results page



# Session-wise Results page


# Trade Infrastructure page


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
from django.shortcuts import render, get_object_or_404
from .models import AdminStaff

from django.shortcuts import render, get_object_or_404
from .models import AdminStaff
from .utils import get_header_content  # Assuming you have a function to get the header content

def adminstaff_detail(request, serial_number):
    # Get the header content and sitemap
    header_content = get_header_content()
    page_title = "Admin Staff Detail"
    

    # Fetch the specific staff member by serial_number
    staff = get_object_or_404(AdminStaff, serial_number=serial_number)

    # Get the next and previous staff members for navigation
    next_staff = AdminStaff.objects.filter(serial_number__gt=serial_number).order_by('serial_number').first()
    previous_staff = AdminStaff.objects.filter(serial_number__lt=serial_number).order_by('-serial_number').first()
    if not request.user.is_staff and staff.aadharcard2:
        # Mask all but the last 4 characters of the Aadhar card
        masked_aadhar = '*' * (len(staff.aadharcard2) - 4) + staff.aadharcard2[-4:]
    else:
        masked_aadhar = staff.aadharcard2
        
    return render(request, 'adminstaffdetail.html', {
        'staff': staff,
        'next_staff': next_staff,
        'previous_staff': previous_staff,
        'header_content': header_content,
        'page_title': page_title,
        'masked_aadhar': masked_aadhar,
        
    })


# Technical Staff page
def techstaff(request):
    tech_staff_list = TechStaff.objects.all()
    header_content = get_header_content()  # Assuming this function provides header data
    return render(request, 'techstaff.html', {
        'tech_staff_list': tech_staff_list,
        'header_content': header_content,
    })
def techstaff_detail(request, serial_number):
    header_content = get_header_content()
    page_title = "Tech Staff"  
    staff = get_object_or_404(TechStaff, serial_number=serial_number)

    # Get next and previous staff members
    next_staff = TechStaff.objects.filter(serial_number__gt=serial_number).order_by('serial_number').first()
    previous_staff = TechStaff.objects.filter(serial_number__lt=serial_number).order_by('-serial_number').first()

    # Mask Aadhar card for non-admin users
    if not request.user.is_staff and staff.aadharcard1:
        # Mask all but the last 4 characters of the Aadhar card
        masked_aadhar = '*' * (len(staff.aadharcard1) - 4) + staff.aadharcard1[-4:]
    else:
        masked_aadhar = staff.aadharcard1
        

    return render(request, 'techstaffdetail.html', {
        'staff': staff,
        'next_staff': next_staff,
        'previous_staff': previous_staff,
        'header_content': header_content,
        'page_title': page_title,
        'masked_aadhar': masked_aadhar,
    })

# RTI page



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



def ats(request):
    # Fetch the section data from the database
    sections = ApprenticeshipSection.objects.all()  # Get all sections
    header_content = get_header_content()
    return render(request, 'ats.html', {
        'header_content': header_content,
        'sections': sections,
    })


# Craftsman Training Scheme (CTS) page


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

#traineebulk
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import TraineeDetails

@user_passes_test(lambda u: u.is_superuser)
def bulk_upload_trainees(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        try:
            # Read the Excel file using pandas
            data = pd.read_excel(file)  # Ensure pandas and openpyxl are installed
            
            # Get the last trainee_id to generate the next one
            last_trainee = TraineeDetails.objects.last()
            next_id = 1
            if last_trainee:
                # Increment the last trainee_id if records already exist
                last_id = last_trainee.trainee_id
                next_id = int(last_id.split('-')[1]) + 1
            
            # Iterate over the rows of the Excel file
            for idx, row in data.iterrows():
                # Generate the trainee_id (e.g., TR-0001, TR-0002, etc.)
                trainee_id = f"TR-{str(next_id).zfill(4)}"
                
                # Create a new TraineeDetails instance with the provided data
                TraineeDetails.objects.create(
                    trainee_id=trainee_id,  # Use the generated trainee_id
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
                    remarks=row.get('remarks', ''),  # Default to empty string if 'remarks' is missing
                    highest_qualification=row.get('highest_qualification', ''),  # Handle the new field
                    marks_10th=row.get('marks_10th', None),  # Handle marks, default to None if not present
                    marks_12th=row.get('marks_12th', None),  # Handle marks, default to None if not present
                    hobbies=row.get('hobbies', ''),  # Handle hobbies, default to empty string
                    work_experience=row.get('work_experience', '')  # Handle work experience, default to empty string
                )

                # Increment the next_id for the next trainee
                next_id += 1
                
            messages.success(request, 'Trainee details uploaded successfully!')
        except Exception as e:
            # Handle exceptions and display an error message
            messages.error(request, f'Error uploading data: {str(e)}')

        return redirect('admin:bulk_upload_trainees')  # Redirect to the bulk upload page after successful upload

    return render(request, 'admin/bulk_upload.html')  # Ensure the template path is correct



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
#trainee_list viwe
from django.shortcuts import render
from .models import TraineeDetails

def trainee_list(request):
    header_content = get_header_content()  # Assuming this function exists to get header content

    # Get filter values from request
    selected_session = request.GET.get('session', '')
    selected_trade = request.GET.get('trade', '')

    # Get all unique sessions and trades for the filters
    sessions = TraineeDetails.objects.values_list('session', flat=True).distinct()
    trades = TraineeDetails.objects.values_list('trade', flat=True).distinct()

    # Retrieve trainees with optional filtering
    trainees = TraineeDetails.objects.all()

    if selected_session:
        trainees = trainees.filter(session=selected_session)
    
    if selected_trade:
        trainees = trainees.filter(trade=selected_trade)

    # Mask phone number logic
    for trainee in trainees:
        # Assuming 'gender' is part of the trainee model
        if hasattr(trainee, 'gender') and trainee.gender == 'Female':  
            trainee.phoneno_masked = f"*****{trainee.phoneno[-4:]}"  # Mask all but last 4 digits
        else:
            trainee.phoneno_masked = trainee.phoneno  # Show full number if not female

    # Pass filtered trainees, session options, and selected values to the template
    return render(request, 'trainees.html', {
        'trainees': trainees,
        'sessions': sessions,
        'trades': trades,
        'selected_session': selected_session,
        'selected_trade': selected_trade,
        'header_content': header_content
    })

# trade view

def trades(request):
    trades = Trade.objects.all()  # Fetch all trades from the database
    header_content = get_header_content()  # Get header content (adjust if necessary)
    page_title = "Institute Trades"
    
    # Return the response, passing both the trades and header_content to the template
    return render(request, 'trades.html', {'trades': trades, 'header_content': header_content,'page_title':page_title})
   


#overall result

def overall_results(request):
    # Get all the possible values of the result column
    results = ['pass', 'fail', 'reappear', 'all']  # Added 'all' as an option
    header_content = get_header_content()
    page_title = "Overall Result"
    

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
        'header_content': header_content,
        'page_title':page_title

    }
    return render(request, 'overall_results.html', context,)

def trade_wise_result(request):
    page_title = "Trade wise Result"
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
        'header_content': header_content,
        'page_title':page_title
    }

    return render(request, 'trade_wise_result.html', context)

#sessionwise result

def session_wise_result(request):
    # Get all the distinct values for session and trade
    page_title = "Session Wise Result" 
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
        'header_content': header_content , # Pass header content to the template
        'page_title':page_title
    }
    return render(request, 'session_wise_result.html', context)

#institute anenities

def institute_amenities(request):
    header_content = get_header_content()
    page_title = "Institute Anenities"
    amenities = InstituteAmenity.objects.all()  # Fetch all records
    return render(request, 'institute_amenities.html', {'amenities': amenities,'header_content': header_content, 'page_title':page_title })
    #return render(request, 'institute_amenities.html', {'header_content': header_content, 'page_title':page_title})

#reportcard


def report_card(request):
    # Get the selected session, month, and trade from the GET request
    page_title = "Report Card"
    selected_session = request.GET.get('session', None)
    selected_month = request.GET.get('month', None)
    selected_trade = request.GET.get('trade', None)

    # Fetch all marks
    marks = Marks.objects.select_related('trainee_sn')
    header_content = get_header_content()

    # Filter based on session
    if selected_session:
        marks = marks.filter(trainee_sn__session=selected_session)

    # Filter based on month
    if selected_month:
        marks = marks.filter(month=selected_month)

    # Filter based on trade
    if selected_trade:
        marks = marks.filter(trainee_sn__trade=selected_trade)

    # Remove duplicates manually (by combining trainee_sn and month)
    unique_marks = []
    seen = set()  # To keep track of already seen (trainee_sn, month) combinations

    for mark in marks:
        unique_key = (mark.trainee_sn.sn, mark.month)
        if unique_key not in seen:
            unique_marks.append(mark)
            seen.add(unique_key)

    # Get all unique sessions, months, and trades for the dropdowns
    sessions = Marks.objects.values_list('trainee_sn__session', flat=True).distinct()
    months = Marks.objects.values_list('month', flat=True).distinct()
    trades = Marks.objects.values_list('trainee_sn__trade', flat=True).distinct()

    return render(request, 'reportcard.html', {
        'marks': unique_marks,
        'selected_session': selected_session,
        'selected_month': selected_month,
        'selected_trade': selected_trade,
        'sessions': sessions,  # Pass available sessions to the template
        'months': months,      # Pass available months to the template
        'trades': trades,      # Pass available trades to the template
        'header_content': header_content,
    })





#add marks

from datetime import datetime
def add_marks(request):
    header_content = get_header_content()
    page_title = "Add Marks"
    if request.method == 'POST':
        # Get the selected month from the form
        selected_month = request.POST.get('month')

        # Loop through the form data and process only relevant entries
        for trainee in TraineeDetails.objects.all():
            sn = trainee.sn  # This is the trainee SN, used to identify each trainee
            
            # Retrieve data from the form for this trainee
            monthly_attendance = request.POST.get(f'monthly_attendance_{sn}', '').strip()
            trade_theory_marks = request.POST.get(f'trade_theory_marks_{sn}', '').strip()
            trade_practical_marks = request.POST.get(f'trade_practical_marks_{sn}', '').strip()
            es_marks = request.POST.get(f'es_marks_{sn}', '').strip()
            ws_marks = request.POST.get(f'ws_marks_{sn}', '').strip()
            total_marks = request.POST.get(f'total_marks_{sn}', '').strip()
            remarks = request.POST.get(f'remarks_{sn}', '').strip()

            # Check if any data was submitted for this trainee
            if any([monthly_attendance, trade_theory_marks, trade_practical_marks, es_marks, ws_marks, total_marks, remarks]):
                # Fetch the TraineeDetails instance corresponding to the trainee SN
                trainee_instance = TraineeDetails.objects.get(sn=sn)

                # Create and save the marks entry in the Marks table
                Marks.objects.create(
                    trainee_sn=trainee_instance,  # Use the instance here, not the sn
                    monthly_attendance=int(monthly_attendance) if monthly_attendance else 0,
                    trade_theory_marks=int(trade_theory_marks) if trade_theory_marks else 0,
                    trade_practical_marks=int(trade_practical_marks) if trade_practical_marks else 0,
                    es_marks=int(es_marks) if es_marks else 0,
                    ws_marks=int(ws_marks) if ws_marks else 0,
                    total_marks=int(total_marks) if total_marks else 0,
                    remarks=remarks,
                    month=selected_month
                )

        return redirect('success')  # Redirect to a success page or back to the form

    # Get the list of trainees for rendering the table
    trainees = TraineeDetails.objects.all()

    return render(request, 'add_marks.html', {'trainees': trainees, 'header_content': header_content, 'page_title': page_title})



def success(request):
    header_content = get_header_content()
    page_title = "Success"
    return render(request, 'success.html',{'header_content': header_content,'page_title':page_title})  # Assuming you have a 'success.html' template






#socialmedia

def social_media_page(request):
    header_content = get_header_content()
    page_title = "Social Media" 
    testimonials = Testimonial.objects.all()  # Fetch all testimonials from the database
    return render(request, "social_media.html", {"testimonials": testimonials,'header_content': header_content,'page_title':page_title})



# View to handle displaying and saving meetings
def meetings_view(request):
    header_content = get_header_content()
    page_title = "Meetings" 
    if request.method == 'POST':
        # Collect form data
        agenda = request.POST.get('agenda')
        date = request.POST.get('date')
        time = request.POST.get('time')
        minutes = request.POST.get('minutes')
        
        # Handling file upload (optional)
        attachment = request.FILES.get('attachment')
        if attachment:
            fs = FileSystemStorage()
            attachment_path = fs.save(attachment.name, attachment)
        else:
            attachment_path = None

        # Create and save a new meeting object
        meeting = Meeting(agenda=agenda, date=date, time=time, minutes=minutes, attachment=attachment_path)
        meeting.save()

        messages.success(request, "Meeting has been saved successfully!")

        # Redirect to the same page after saving
        return redirect('meetings')  # Assuming 'meetings' is the name of the URL for this page

    # Fetch all meetings to display in the table
    meetings = Meeting.objects.all()

    return render(request, 'meetings.html', {'meetings': meetings,'header_content': header_content,'page_title':page_title})





#video


def video_view(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Videos"
    videos = Video.objects.all()  # Fetch all videos from the database

    return render(request, 'video.html', {
        'videos': videos,
        'header_content': header_content,
        'page_title': page_title
    })





def detailtrade_view(request):
    header_content = get_header_content()  # Retrieve header content
    streams = Stream.objects.all()  # Fetch all streams from the database
    context = {
        'streams': streams,
        'header_content': header_content,
    }
    return render(request, 'detailtrade.html', context)

#reach us

 

def reach_us(request):
    # Fetch the first ReachUsContent instance (or create one if none exists)
    content = ReachUsContent.objects.first()
    header_content = get_header_content()  # Retrieve header content
    page_title = "Reach Us"
    if content is None:
        content = ReachUsContent.objects.create(
            location_url="https://www.google.com/maps/embed?pb=YOUR_DEFAULT_EMBED_URL", 
            description="You can find us at this location."
        )

    context = {
        'location_url': content.location_url,
        'description': content.description,
        'header_content': header_content,
        'page_title': page_title
    }
    return render(request, 'reach_us.html', context)

#counter

from django.http import JsonResponse
from django.utils.timezone import now
from django.contrib.sessions.models import Session
from .models import VisitorCounter
from django.http import JsonResponse
from django.utils.timezone import now
from .models import VisitorCounter

# In views.py
from .utils import get_client_ip

def update_visitor_count(request):
    counter, created = VisitorCounter.objects.get_or_create(id=1)

    # Get client IP address
    ip = get_client_ip(request)

    # Your existing logic for handling session, user, and IP
    session_key = request.session.session_key
    user = request.user if request.user.is_authenticated else None

    if ip and ip not in counter.visitor_ips:
        counter.visitor_ips[ip] = now().strftime("%Y-%m-%d %H:%M:%S")

    if session_key and session_key not in counter.visitor_sessions:
        counter.visitor_sessions[session_key] = now().strftime("%Y-%m-%d %H:%M:%S")

    if user and user.id not in counter.visitor_users:
        counter.visitor_users[user.id] = now().strftime("%Y-%m-%d %H:%M:%S")

    counter.count = len(counter.visitor_ips) + len(counter.visitor_sessions) + len(counter.visitor_users)
    counter.save()

    formatted_count = f"{counter.count:06d}"
    return JsonResponse({"count": formatted_count})



#reset counter 
from django.http import JsonResponse
from .models import VisitorCounter

def reset_visitor_count(request):
    if request.user.is_superuser:  # Ensure only admins can reset
        counter, created = VisitorCounter.objects.get_or_create(id=1)
        counter.count = 0
        counter.visitor_ips.clear()
        counter.visitor_sessions.clear()
        counter.visitor_users.clear()
        counter.save()
        return JsonResponse({"message": "Visitor counter has been reset to zero."})
    return JsonResponse({"error": "Permission denied."}, status=403)

#grievance


# Grievance submission and listing view
def grievance_list_create(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Grievance"
    # Handle form submission
    if request.method == 'POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grievance')  # Redirect to the same page after submission
    else:
        form = GrievanceForm()

    # Fetch all grievances
    grievances = Grievance.objects.all().order_by('-created_at')  # Newest first
    return render(request, 'grievance.html', {'form': form, 'grievances': grievances,'header_content': header_content,
        'page_title': page_title})

#chairmandesk



def chairman_desk(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Chairman Desk"
    chairman = Chairman.objects.first()  # Get the first Chairman object (assuming only one entry)
    
    # If no Chairman record exists, create a default one
    if not chairman:
        chairman = Chairman.objects.create(
            name='Dr. John Doe',
            position='Chairman',
            message='Welcome to our institute. As the Chairman, I am committed...',
            image='default.jpg'  # Place a default image or leave it blank
        )

    # Handle form submission
    if request.method == 'POST':
        form = ChairmanForm(request.POST, request.FILES, instance=chairman)
        if form.is_valid():
            form.save()
            return redirect('chairman_desk')  # Redirect to the same page after saving
    else:
        form = ChairmanForm(instance=chairman)

    return render(request, 'chairman_desk.html', {
        'chairman': chairman,
        'form': form,
        'header_content': header_content,
        'page_title': page_title
    })



#studymaterial
# views.py
from django.shortcuts import render
from .models import StudyMaterial

def study_material(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Chairman Desk"
    # Get all trades for the dropdown
    trades = StudyMaterial.objects.values_list('trade', flat=True).distinct()
    
    # Get selected trade from the dropdown (default: show all)
    selected_trade = request.GET.get('trade', None)
    if selected_trade:
        materials = StudyMaterial.objects.filter(trade=selected_trade)
    else:
        materials = StudyMaterial.objects.all()
    
    return render(request, 'study_material.html', {
        'materials': materials,
        'trades': trades,
        'selected_trade': selected_trade,
        'header_content': header_content,
        'page_title': page_title
    })


#online test

from .models import TradeForOnlineTest, TopicForOnlineTest
from .models import TradeForOnlineTest, TopicForOnlineTest
from .models import TradeForOnlineTest, TopicForOnlineTest, QuestionForOnlineTest
from .models import QuestionForOnlineTest
from .models import QuestionForOnlineTest
from django.http import HttpResponse

def select_test(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Select Test"
    
    trades = TradeForOnlineTest.objects.all()
    selected_trade_id = request.GET.get('trade_id', '')
    selected_topic_id = request.GET.get('topic_id', '')
    num_questions = request.GET.get('num_questions', 5)
    user_name = request.GET.get('user_name', '')  # New field
    iti_name = request.GET.get('iti_name', '')  # New field

    # Filter topics based on selected trade
    if selected_trade_id:
        topics = TopicForOnlineTest.objects.filter(trade_id=selected_trade_id)
    else:
        topics = TopicForOnlineTest.objects.none()  # Empty queryset if no trade selected

    # If all fields are filled, redirect to the start_test view
    if selected_trade_id and selected_topic_id and num_questions and user_name and iti_name:
        return redirect(
            'start_test',
            trade_id=selected_trade_id,
            topic_id=selected_topic_id,
            num_questions=num_questions,
            user_name=user_name,
            iti_name=iti_name
        )

    return render(request, 'select_test.html', {
        'trades': trades,
        'topics': topics,
        'selected_trade_id': selected_trade_id,
        'selected_topic_id': selected_topic_id,
        'num_questions': num_questions,
        'header_content': header_content,
        'page_title': page_title,
        'user_name': user_name,  # Pass user_name to the template
        'iti_name': iti_name  # Pass iti_name to the template
    })






from django.shortcuts import render
from .models import TradeForOnlineTest, TopicForOnlineTest, QuestionForOnlineTest
from django.shortcuts import get_object_or_404, redirect

def start_test(request, trade_id, topic_id, num_questions, user_name, iti_name):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Start Test"
    
    # Get the selected trade
    trade = get_object_or_404(TradeForOnlineTest, id=trade_id)
    
    # Fetch questions based on the topic selection
    if topic_id == "all":  # If "all" is selected, fetch questions across all topics for the trade
        questions = QuestionForOnlineTest.objects.filter(topic__trade=trade).order_by('?')[:int(num_questions)]
        topic = None  # No specific topic, since "all" is selected
    else:  # Specific topic is selected
        topic = get_object_or_404(TopicForOnlineTest, id=topic_id)
        questions = QuestionForOnlineTest.objects.filter(topic=topic).order_by('?')[:int(num_questions)]

    # Calculate the total number of questions actually loaded
    total_loaded_questions = questions.count()

    # Calculate time remaining based on the number of questions loaded
    # 2 minutes per question
    time_per_question = 2  # minutes
    total_time_in_minutes = total_loaded_questions * time_per_question
    total_time_in_seconds = total_time_in_minutes * 60  # Convert minutes to seconds

    # Prepare the topic_id value for the template
    topic_id_context = topic.id if topic else "all"

    return render(request, 'start_test.html', {
        'trade': trade,
        'topic': topic,
        'questions': questions,
        'num_questions': num_questions,  # Number requested by the user
        'total_loaded_questions': total_loaded_questions,  # Actual loaded questions for this test
        'header_content': header_content,
        'page_title': page_title,
        'topic_id': topic_id_context,  # Include topic_id in the context
        'total_time_in_seconds': total_time_in_seconds,  # Pass the calculated time in seconds
        'user_name': user_name,  # Pass user_name to the template
        'iti_name': iti_name  # Pass iti_name to the template
    })


#submit


from django.shortcuts import render
from .models import QuestionForOnlineTest, TopicForOnlineTest, TradeForOnlineTest
from django.http import HttpResponse
from random import sample

from django.shortcuts import render, get_object_or_404
from .models import QuestionForOnlineTest, TopicForOnlineTest, TradeForOnlineTest
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import TradeForOnlineTest, TopicForOnlineTest, QuestionForOnlineTest

def submit_test(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Test Results"
    
    if request.method == 'POST':
        # Initialize variables
        score = 0
        total_questions = 0
        attempted_questions = 0
        correct_answers_count = 0
        correct_answers = []
        user_answers = {}

        # Get POST data
        selected_topic_id = request.POST.get('topic_id')
        num_questions = int(request.POST.get('num_questions'))
        trade_id = request.POST.get('trade_id')

        # Fetch questions based on "All Topics" or a specific topic
        if selected_topic_id == "all":
            # Fetch all topics for the trade
            trade = get_object_or_404(TradeForOnlineTest, id=trade_id)
            questions = QuestionForOnlineTest.objects.filter(topic__trade=trade).order_by('?')[:num_questions]
        else:
            # Fetch specific topic
            topic = get_object_or_404(TopicForOnlineTest, id=selected_topic_id)
            questions = QuestionForOnlineTest.objects.filter(topic=topic).order_by('?')[:num_questions]

        total_questions = len(questions)

        # Process the answers
        def map_answer(option_number):
            answer_mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
            return answer_mapping.get(option_number, '')

        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            user_answers[question.id] = selected_answer

            if selected_answer:  # If the user selected an answer for this question
                attempted_questions += 1  # Increment attempted questions

                # Check if the answer is correct
                if int(selected_answer) == question.correct_option:
                    score += 1
                    correct_answers_count += 1

                # Record the correct and user answers
                correct_answers.append({
                    'question': question.text,
                    'correct_answer': map_answer(question.correct_option),
                    'user_answer': map_answer(int(selected_answer)) if selected_answer.isdigit() else 'N/A',
                })
            else:
                # Record unattempted answers as well
                correct_answers.append({
                    'question': question.text,
                    'correct_answer': map_answer(question.correct_option),
                    'user_answer': 'Unattempted',
                })

        # Calculate unattempted questions
        unattempted_questions = total_questions - attempted_questions

        # Prepare context for rendering the result page
        context = {
            'score': f'{score}/{total_questions}',
            'total_questions': total_questions,
            'actual_num_questions': attempted_questions,
            'unattempted_questions': unattempted_questions,
            'correct_answers_count': correct_answers_count,
            'correct_answers': correct_answers,
            'user_answers': user_answers,  # User's answers
            'header_content': header_content,
            'page_title': page_title,
        }

        return render(request, 'test_result.html', context)

    return HttpResponse("Invalid request", status=400)






#ajex reload 
from django.http import JsonResponse
from .models import TopicForOnlineTest

def fetch_topics(request):
    trade_id = request.GET.get('trade_id')
    if not trade_id:
        return JsonResponse({"topics": []})

    topics = TopicForOnlineTest.objects.filter(trade_id=trade_id).values('id', 'name')
    return JsonResponse({"topics": list(topics)})
#tenders
from django.shortcuts import render
from .models import Tender

# main_app/views.py
from django.shortcuts import render
from .models import Tender

# views.py
from django.shortcuts import render
from .models import Tender

def tender_list(request):
    header_content = get_header_content()  # Retrieve header content
    page_title = "Tenders"
    # Fetch all tenders from the Tender model
    tenders = Tender.objects.all()  # You can filter or order the data if needed
    
    # Pass the tenders to the template
    return render(request, 'tenders.html', {'tenders': tenders,'header_content': header_content,
            'page_title': page_title,})




















#trainee detail from django.shortcuts import render, get_object_or_404
from .models import TraineeDetails

from django.shortcuts import render, get_object_or_404
from .models import TraineeDetails

def trainee_detail(request, trainee_id):
    header_content = get_header_content()  # Get header content (adjust if necessary)
    page_title = "Trainee Full Detail"
    
    # Get the trainee based on trainee_id (primary key)
    trainee = get_object_or_404(TraineeDetails, pk=trainee_id)
    
    # Get the list of all trainees
    trainees = TraineeDetails.objects.all()
    
    # Check if the current user is an admin
    is_admin = request.user.is_superuser
    
    # Find the previous and next trainees
    previous_trainee = trainees.filter(pk__lt=trainee_id).last()  # Previous trainee (ID less than current)
    next_trainee = trainees.filter(pk__gt=trainee_id).first()  # Next trainee (ID greater than current)
    
    # Pass the context to the template
    return render(request, 'trainee_detail.html', {
        'trainee': trainee,
        'is_admin': is_admin,
        'header_content': header_content,
        'page_title': page_title,
        'previous_trainee': previous_trainee,
        'next_trainee': next_trainee,
    })
