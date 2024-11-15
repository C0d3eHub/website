from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from .models import (
    NewsAlert, 
    PrincipalDesk, 
    AboutInstituteContent, 
    AdminStaff, 
    MyModel, 
    TechStaff, 
    HeaderContent, 
    SliderImage, 
    ElectricPowerSupply, 
    KeyPerformanceIndicatorContent, 
    TraineeDetails, 
    GalleryImage,
)
from .forms import AboutInstituteForm
from .views import bulk_upload_trainees  # Ensure this view is defined

# Custom Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin Panel"
    index_template = "admin/index1.html"  # Ensure this template exists

# Instantiate the custom admin site
admin_site = CustomAdminSite(name='custom_admin')


# Register models with custom admin site
@admin.register(PrincipalDesk)
class PrincipalDeskAdmin(admin.ModelAdmin):
    pass  # No custom admin configuration for now


# Slider Image Admin Class
@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'image')  # Fields to display in the list view
    search_fields = ('caption',)  # Searchable fields


# NewsAlert Admin Class
@admin.register(NewsAlert)
class NewsAlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Display specific fields in the admin list view
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        # Logic to mark selected NewsAlert entries as published
        queryset.update(status='published')  # Uncomment if 'status' field exists
        self.message_user(request, "Selected alerts marked as published.")

    mark_as_published.short_description = "Mark selected news alerts as published"


# AboutInstituteContent Admin Class
@admin.register(AboutInstituteContent)
class AboutInstituteAdmin(admin.ModelAdmin):
    form = AboutInstituteForm  # Use the custom form here


# AdminStaff Admin Class
@admin.register(AdminStaff)
class AdminStaffAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'designation', 'date_of_joining', 'phone')

    def serial_number(self, obj):
        return obj.id  # Auto-generate serial number based on ID

    serial_number.short_description = 'Serial Number'  # Optional: Rename column header


# MyModel Admin Class
@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2', 'field3']  # Ensure these field names are correct


# Register additional models with the custom admin site
admin.site.register(TechStaff)
admin.site.register(HeaderContent)
admin.site.register(ElectricPowerSupply)
admin.site.register(KeyPerformanceIndicatorContent)


# TraineeDetails Admin Class
@admin.register(TraineeDetails)
class TraineeDetailsAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name', 'fathername', 'trade', 'session', 'result', 'bulk_upload_link')  # Include the link in the display

    def bulk_upload_link(self, obj):
        return format_html('<a href="{}">Bulk Upload</a>', reverse('admin:bulk_upload_trainees'))

    bulk_upload_link.short_description = 'Bulk Upload'  # Optional: Customize the column name

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('bulk_upload/', admin.site.admin_view(bulk_upload_trainees), name='bulk_upload_trainees'),
        ]
        return custom_urls + urls


# GalleryImage Admin Class
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')  # Fields to display in the list view
    search_fields = ('title',)  # Searchable fields

# admin.py
from django.contrib import admin
from .models import Trade

admin.site.register(Trade)
from django.contrib import admin
from .models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # You can customize which fields to show
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'message')

admin.site.register(ContactForm, ContactFormAdmin)
from .models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'position')
    ordering = ('position',)
from django.contrib import admin
from .models import InstituteAmenity

admin.site.register(InstituteAmenity)
from .models import InstituteInfrastructure

admin.site.register(InstituteInfrastructure)
from .models import AdmissionCriteria

admin.site.register(AdmissionCriteria)
# Update urlpatterns to include the custom admin site
# admin.py
from django.contrib import admin
from .models import NCVTTrade

class NCVTTradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'affiliated_to', 'remarks', 'intake_capacity', 'units')  # Add new fields here
    list_filter = ('affiliated_to',)  # Add filtering by 'affiliated_to'
    search_fields = ('name', 'remarks')  # Make the 'name' and 'remarks' searchable

admin.site.register(NCVTTrade, NCVTTradeAdmin)
# admin.py
from django.contrib import admin
from .models import Placement

admin.site.register(Placement)
# admin.py
from django.contrib import admin
from .models import ECA

class ECAAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'remarks']

admin.site.register(ECA, ECAAdmin)
# admin.py
from django.contrib import admin
from .models import IndustryCollaboration

class IndustryCollaborationAdmin(admin.ModelAdmin):
    list_display = ['industry_name', 'partner_name', 'mou_signed', 'mou_date', 'valid_upto', 'remarks']

admin.site.register(IndustryCollaboration, IndustryCollaborationAdmin)
# admin.py
from django.contrib import admin
from .models import RTI

admin.site.register(RTI)
# admin.py
from django.contrib import admin
from .models import Inspection

admin.site.register(Inspection)
# admin.py
from django.contrib import admin
from .models import ApprenticeshipSection

admin.site.register(ApprenticeshipSection)
from django.contrib import admin
from .models import CTSContent

admin.site.register(CTSContent)
# admin.py
from django.contrib import admin
from django.contrib import admin
from .models import CommitteeMember, Achievement

admin.site.register(CommitteeMember)
admin.site.register(Achievement)

from django.contrib import admin
from .models import HPKVNTrainingProgram, HPKVNEnrollmentProcess, HPKVNPlacement, HPKVNTrainee

# Register HPKVNTrainingProgram model
@admin.register(HPKVNTrainingProgram)
class HPKVNTrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name',)  # Allow search by name
    ordering = ('name',)  # Default ordering by name

# Register HPKVNEnrollmentProcess model
@admin.register(HPKVNEnrollmentProcess)
class HPKVNEnrollmentProcessAdmin(admin.ModelAdmin):
    list_display = ('step', 'description')  # Display these fields in the list view
    search_fields = ('step',)  # Allow search by step
    ordering = ('step',)  # Default ordering by step

# Register HPKVNPlacement model
@admin.register(HPKVNPlacement)
class HPKVNPlacementAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'placement_date', 'remarks')  # Display these fields in the list view
    search_fields = ('company_name',)  # Allow search by company name
    ordering = ('placement_date',)  # Default ordering by placement date

# Register HPKVNTrainee model
@admin.register(HPKVNTrainee)
class HPKVNTraineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'course', 'remarks')  # Display these fields in the list view
    search_fields = ('name', 'course')  # Allow search by name and course
    ordering = ('name',)  # Default ordering by trainee name
#ojt
from django.contrib import admin
from .models import OJTContent
from .forms import OJTContentForm

class OJTContentAdmin(admin.ModelAdmin):
    form = OJTContentForm

admin.site.register(OJTContent, OJTContentAdmin)
from django.contrib import admin
from .models import OJTTrainee

class OJTTraineeAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name', 'ojt_location', 'trade', 'remarks')
    search_fields = ('name', 'ojt_location', 'trade')
    list_filter = ('trade',)

admin.site.register(OJTTrainee, OJTTraineeAdmin)

urlpatterns = [
    path('admin/', admin_site.urls),  # Custom admin panel route
]
