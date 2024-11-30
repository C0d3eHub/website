from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from .forms import AboutInstituteForm, OJTContentForm
from .views import bulk_upload_trainees  # Ensure this view is defined
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
    Trade,
    ContactForm,
    Profile,
    InstituteAmenity,
    InstituteInfrastructure,
    AdmissionCriteria,
    NCVTTrade,
    Placement,
    ECA,
    IndustryCollaboration,
    RTI,
    Inspection,
    ApprenticeshipSection,
    CTSContent,
    CommitteeMember,
    Achievement,
    HPKVNTrainingProgram,
    HPKVNEnrollmentProcess,
    HPKVNPlacement,
    HPKVNTrainee,
    OJTContent,
    OJTTrainee,
    Marks,
    Testimonial,
    Meeting,
    Video,
    Stream,
    ReachUsContent,
)

# Custom Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin Panel"
    index_template = "admin/index1.html"  # Ensure this template exists
#techstaff
from django.contrib import admin

@admin.register(TechStaff)
class TechStaffAdmin(admin.ModelAdmin):
    list_display = (
        'serial_number', 
        'name', 
        'designation', 
        'date_of_joining', 
        'phone_number', 
        'gender', 
        'total_experience', 
        'last_working_place'
    )
    search_fields = ('name', 'father_name', 'qualification', 'last_working_place')
    list_filter = ('designation', 'gender', 'date_of_joining')

# Instantiate the custom admin site
admin_site = CustomAdminSite(name='custom_admin')

# Admin configurations
@admin.register(PrincipalDesk)
class PrincipalDeskAdmin(admin.ModelAdmin):
    pass

@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'image')
    search_fields = ('caption',)

@admin.register(NewsAlert)
class NewsAlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        queryset.update(status='published')
        self.message_user(request, "Selected alerts marked as published.")

    mark_as_published.short_description = "Mark selected news alerts as published"

@admin.register(AboutInstituteContent)
class AboutInstituteAdmin(admin.ModelAdmin):
    form = AboutInstituteForm

@admin.register(AdminStaff)
class AdminStaffAdmin(admin.ModelAdmin):
    list_display = (
        'serial_number', 
        'name', 
        'designation', 
        'date_of_joining', 
        'phone', 
        'gender', 
        'total_experience', 
        'last_working_place'
    )
    search_fields = ('name', 'father_name', 'qualification', 'last_working_place')
    list_filter = ('designation', 'gender', 'date_of_joining')


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2', 'field3']

from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from .models import TraineeDetails
from .views import bulk_upload_trainees  # Import your view function

@admin.register(TraineeDetails)
class TraineeDetailsAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name', 'fathername', 'trade', 'session', 'result', 'bulk_upload_link')

    # Custom link for bulk upload
    def bulk_upload_link(self, obj=None):
        return format_html('<a href="{}">Bulk Upload</a>', reverse('admin:bulk_upload_trainees'))
    bulk_upload_link.short_description = 'Bulk Upload'

    def get_urls(self):
        # Custom URL for bulk upload functionality
        urls = super().get_urls()
        custom_urls = [
            path('bulk_upload/', self.admin_site.admin_view(bulk_upload_trainees), name='bulk_upload_trainees'),
        ]
        return custom_urls + urls


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')
    search_fields = ('title',)

# Other model registrations

admin.site.register(HeaderContent)
admin.site.register(ElectricPowerSupply)
admin.site.register(KeyPerformanceIndicatorContent)
admin.site.register(Trade)
admin.site.register(ContactForm, admin.ModelAdmin)
admin.site.register(Profile)
admin.site.register(InstituteAmenity)
admin.site.register(InstituteInfrastructure)
admin.site.register(AdmissionCriteria)
admin.site.register(NCVTTrade)
admin.site.register(Placement)
admin.site.register(ECA)
admin.site.register(IndustryCollaboration)
admin.site.register(RTI)
admin.site.register(Inspection)
admin.site.register(ApprenticeshipSection)
admin.site.register(CTSContent)
admin.site.register(CommitteeMember)
admin.site.register(Achievement)
admin.site.register(OJTContent, admin.ModelAdmin)
admin.site.register(OJTTrainee, admin.ModelAdmin)
admin.site.register(Marks)
admin.site.register(Testimonial)
admin.site.register(Meeting)
admin.site.register(Video)
admin.site.register(Stream)
admin.site.register(ReachUsContent)

# Custom HPKVN Admins
@admin.register(HPKVNTrainingProgram)
class HPKVNTrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(HPKVNEnrollmentProcess)
class HPKVNEnrollmentProcessAdmin(admin.ModelAdmin):
    list_display = ('step', 'description')
    search_fields = ('step',)
    ordering = ('step',)

@admin.register(HPKVNPlacement)
class HPKVNPlacementAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'placement_date', 'remarks')
    search_fields = ('company_name',)
    ordering = ('placement_date',)

@admin.register(HPKVNTrainee)
class HPKVNTraineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'course', 'remarks')
    search_fields = ('name', 'course')
    ordering = ('name',)


    from django.contrib import admin
from .models import Grievance

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

#chairman
# admin.py

from .models import Chairman

class ChairmanAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'message', 'image']  # Fields to display in the admin list
    search_fields = ['name', 'position']  # Enable search functionality

admin.site.register(Chairman, ChairmanAdmin)

#study material
# admin.py

from .models import StudyMaterial

class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ['trade', 'topic', 'remarks']  # Customize columns in the admin
    list_filter = ['trade']  # Add filter by trade
    search_fields = ['trade', 'topic']

admin.site.register(StudyMaterial, StudyMaterialAdmin)


#online test

from django.contrib import admin
from .models import TradeForOnlineTest, TopicForOnlineTest, QuestionForOnlineTest

# Register TradeForOnlineTest model
class TradeForOnlineTestAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display trade names in the admin list view
    search_fields = ('name',)  # Enable search functionality by trade name

admin.site.register(TradeForOnlineTest, TradeForOnlineTestAdmin)

# Register TopicForOnlineTest model
class TopicForOnlineTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'trade')  # Show the topic name and associated trade
    search_fields = ('name', 'trade__name')  # Enable search by topic name and trade name

admin.site.register(TopicForOnlineTest, TopicForOnlineTestAdmin)

# Register QuestionForOnlineTest model
class QuestionForOnlineTestAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'option1', 'option2', 'option3', 'option4', 'correct_option')  # Display question details
    search_fields = ('text', 'topic__name')  # Enable search by question text and topic name

admin.site.register(QuestionForOnlineTest, QuestionForOnlineTestAdmin)


from django.contrib import admin
from .models import VisitorCounter

@admin.register(VisitorCounter)
class VisitorCounterAdmin(admin.ModelAdmin):
    list_display = ['id', 'count']
    fields = ['count', 'visitor_ips', 'visitor_sessions', 'visitor_users']
    readonly_fields = ['count']  # 'count' remains read-only

    actions = ['reset_counter']

    def reset_counter(self, request, queryset):
        queryset.update(count=0, visitor_ips={}, visitor_sessions={}, visitor_users={})
        self.message_user(request, "Visitor counter reset successfully!")
    
    reset_counter.short_description = "Reset Visitor Counter"

#tender
# main_app/admin.py

from django.contrib import admin
from .models import Tender

# Optionally, you can create a custom admin class for better display or functionality
class TenderAdmin(admin.ModelAdmin):
    list_display = ('particulars', 'status', 'remarks', 'attachment')  # Customize which fields to display in the admin list view
    list_filter = ('status',)  # Add a filter for the status field
    search_fields = ('particulars',)  # Add a search box for the 'particulars' field
    ordering = ('status',)  # Order tenders by the 'status' field by default

# Register the Tender model with the custom admin class
admin.site.register(Tender, TenderAdmin)

# Custom admin panel route
urlpatterns = [
    path('admin/', admin_site.urls),
]
