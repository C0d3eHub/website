from django.shortcuts import render, redirect,get_object_or_404
from .models import (
    NewsAlert, PrincipalDesk, AboutInstitute, 
    AdminStaff, TechStaff, HeaderContent,SliderImage
)
from .forms import (
    NewsAlertForm, PrincipalDeskForm, 
    AboutInstituteForm, HeaderContentForm,SliderImageForm
)
from django.core.mail import send_mail
from django.contrib import messages
from .utils import get_header_content

# Header content view
def header_content_view(request):
    header_content = HeaderContent.objects.first()  # Assuming only one header content
    if request.method == 'POST':
        form = HeaderContentForm(request.POST, request.FILES, instance=header_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Header content updated successfully.')
            return redirect('header_content')  # Redirect to the same page after saving
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

    # Pass 'images' to the template context
    return render(request, 'index.html', {
        'news_alerts': news_alerts,
        'principal_desk_posts': principal_desk_posts,
        'header_content': header_content,
        'images': images,  # Add images to the context
    })


# About page view
def about(request):
    header_content = get_header_content()
    return render(request, 'about.html', {
        'header_content': header_content,
    })

# Contact page view
def contact(request):
    header_content = get_header_content()  # Ensure header content is fetched
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

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

    return render(request, 'contact.html', {'header_content': header_content})

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

# About Institute view
def about_institute_view(request):
    about_institute = AboutInstitute.objects.first()
    header_content = get_header_content()

    if not about_institute:
        return render(request, 'about_institute.html', {'error': 'No About Institute data found.'})

    if request.method == 'POST':
        form = AboutInstituteForm(request.POST, instance=about_institute)
        if form.is_valid():
            form.save()
            messages.success(request, 'About Institute content updated successfully.')
            return redirect('about_institute')
    else:
        form = AboutInstituteForm(instance=about_institute)

    context = {
        'content': about_institute,
        'form': form,
        'header_content': header_content,
    }
    return render(request, 'about_institute.html', context)

# Admission page
def admission(request):
    header_content = get_header_content()
    return render(request, 'admission.html', {'header_content': header_content})

# Electric Power Supply page
def electric_power_supply(request):
    header_content = get_header_content()
    return render(request, 'electric_power_supply.html', {'header_content': header_content})

# Key Performance Indicator page
def key_performance_indicator(request):
    header_content = get_header_content()
    return render(request, 'key_performance_indicator.html', {'header_content': header_content})

# Institute Amenities page
def institute_amenities(request):
    header_content = get_header_content()
    return render(request, 'institute_amenities.html', {'header_content': header_content})

# Institute Infrastructure page
def institute_infrastructure(request):
    header_content = get_header_content()
    return render(request, 'institute_infrastructure.html', {'header_content': header_content})

# Trades page
def trades(request):
    header_content = get_header_content()
    return render(request, 'trades.html', {'header_content': header_content})

# Admission Criteria page
def admission_criteria(request):
    header_content = get_header_content()
    return render(request, 'admission_criteria.html', {'header_content': header_content})

# Trades NCVT page
def trades_ncvt(request):
    header_content = get_header_content()
    return render(request, 'trades_ncvt.html', {'header_content': header_content})

# Overall Results page
def overall_results(request):
    header_content = get_header_content()
    return render(request, 'overall_results.html', {'header_content': header_content})

# Trade-wise Results page
def trade_wise_result(request):
    header_content = get_header_content()
    return render(request, 'trade_wise_result.html', {'header_content': header_content})

# Session-wise Results page
def session_wise_result(request):
    header_content = get_header_content()
    return render(request, 'session_wise_result.html', {'header_content': header_content})

# Trade Infrastructure page
def trade_infrastructure(request):
    header_content = get_header_content()
    return render(request, 'trade_infrastructure.html', {'header_content': header_content})

# Placement page
def placement(request):
    header_content = get_header_content()
    return render(request, 'placement.html', {'header_content': header_content})

# Extra-curricular Activities page
def eca(request):
    header_content = get_header_content()
    return render(request, 'eca.html', {'header_content': header_content})

# Administrative Staff page: Fetch and display all staff members
def adminstaff(request):
    staff_members = AdminStaff.objects.all()
    header_content = get_header_content()
    return render(request, 'adminstaff.html', {
        'staff_members': staff_members,
        'header_content': header_content,
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
def rti(request):
    header_content = get_header_content()
    return render(request, 'rti.html', {'header_content': header_content})

# Apprenticeship Training Scheme (ATS) page
def ats(request):
    header_content = get_header_content()
    return render(request, 'ats.html', {'header_content': header_content})

# Craftsman Training Scheme (CTS) page
def cts(request):
    header_content = get_header_content()
    return render(request, 'cts.html', {'header_content': header_content})

# IMC page
def imc(request):
    header_content = get_header_content()
    return render(request, 'imc.html', {'header_content': header_content})

# HPKVN page
def hpkvn(request):
    header_content = get_header_content()
    return render(request, 'hpkvn.html', {'header_content': header_content})

# On Job Training (OJT) page
def ojt(request):
    header_content = get_header_content()
    return render(request, 'ojt.html', {'header_content': header_content})
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
