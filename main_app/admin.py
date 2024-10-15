from django.contrib import admin
from django.urls import path
from .models import NewsAlert, PrincipalDesk, AboutInstitute, AdminStaff, MyModel,TechStaff,HeaderContent,SliderImage
from .forms import AboutInstituteForm  # Ensure the form is imported

# Register PrincipalDesk without custom admin class
admin.site.register(PrincipalDesk)
#headaer
#slider
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'image')  # Fields to display in the list view
    search_fields = ('caption',)  # Searchable fields

admin.site.register(SliderImage, SliderImageAdmin)

# Custom Admin class for NewsAlert
@admin.register(NewsAlert)
class NewsAlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Display specific fields in the admin list view

    # Custom actions for the admin interface
    actions = ['mark_as_published']

    def mark_as_published(self, request, queryset):
        # Logic to mark selected NewsAlert entries as published
        # Uncomment the following line if 'status' field exists in the NewsAlert model
        # queryset.update(status='published')  
        self.message_user(request, "Selected alerts marked as published.")

    mark_as_published.short_description = "Mark selected news alerts as published"

# Custom Admin class for AboutInstitute
class AboutInstituteAdmin(admin.ModelAdmin):
    form = AboutInstituteForm  # Use the custom form here

# Register the AboutInstitute model with the custom admin class
admin.site.register(AboutInstitute, AboutInstituteAdmin)

# Custom Admin for AdminStaff (only one registration)
@admin.register(AdminStaff)  # This decorator registers AdminStaff once
class AdminStaffAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'designation', 'date_of_joining', 'phone')  # Ensure the correct field names are used

    def serial_number(self, obj):
        return obj.id  # Auto-generate serial number based on ID
    serial_number.short_description = 'Serial Number'  # Optional: Rename column header

# Custom Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin Panel"
    index_template = "admin/index1.html"  # Ensure this template exists
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2', 'field3']  # Check this line

# Instantiate the custom admin site
admin_site = CustomAdminSite(name='custom_admin')
admin.site.register(MyModel, MyModelAdmin)

# Add models to the custom admin site
admin_site.register(NewsAlert)
admin_site.register(PrincipalDesk)
admin_site.register(AboutInstitute)
admin.site.register(TechStaff)
admin.site.register(HeaderContent)

# Update urlpatterns to include the custom admin site
urlpatterns = [
    path('admin/', admin_site.urls),  # Custom admin panel route
]
