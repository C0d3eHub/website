from django.db import models
from django.utils import timezone


# Header model
class HeaderContent(models.Model):
    logo = models.ImageField(upload_to='logos/')
    h1 = models.CharField(max_length=200)
    h2 = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField()
    button1_text = models.CharField(max_length=100)
    button1_url = models.CharField(max_length=200)
    button2_text = models.CharField(max_length=100)
    button2_url = models.CharField(max_length=200)

    def __str__(self):
        return self.h1


# News Alert model
class NewsAlert(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(default=timezone.now)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return self.title


# Principal Desk model
class PrincipalDesk(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='principal_images/', blank=True, null=True)

    def __str__(self):
        return self.title


# Admin Staff model
class AdminStaff(models.Model):
    serial_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


# Example model
class MyModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)
    field3 = models.DateField()

    def __str__(self):
        return self.field1


# Technical Staff model
class TechStaff(models.Model):
    serial_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='techstaff_photos/', null=True, blank=True)

    def __str__(self):
        return self.name


# Slider Image model
class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f'Image {self.id}'


# Electric Power Supply model
class ElectricPowerSupply(models.Model):
    name_of_trade = models.TextField(blank=True)
    available_load_kw = models.TextField(blank=True)
    sanction_load_kw = models.TextField(blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name_of_trade if self.name_of_trade else "Unnamed Trade"


# Key Performance Indicator Content model
class KeyPerformanceIndicatorContent(models.Model):
    header = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.header or "KPI Content"


# About Institute Content model
class AboutInstituteContent(models.Model):
    header = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.header or "About Institute"


# Trainee Details model
class TraineeDetails(models.Model):
    TRADE_CHOICES = [
        ('COPA', 'COPA'),
        ('MMV', 'MMV'),
        # Add more trades if needed
    ]

    RESULT_CHOICES = [
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('Reappear', 'Reappear'),
    ]

    SESSION_CHOICES = [
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
    ]

    sn = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    address = models.TextField()
    phoneno = models.CharField(max_length=15)
    aadharcard = models.CharField(max_length=20)
    trade = models.CharField(max_length=100, choices=TRADE_CHOICES)
    session = models.CharField(max_length=50, choices=SESSION_CHOICES)
    result = models.CharField(max_length=50, choices=RESULT_CHOICES)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Gallery Image model
class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"


# Trade model (for trades view)
class Trade(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.submitted_at}"

class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profiles/')
    position = models.CharField(max_length=50, unique=True)  # e.g., 'Principal', 'Director'

    def __str__(self):
        return f"{self.name} - {self.designation}"
from django.db import models

class InstituteAmenity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
class InstituteInfrastructure(models.Model):
    TRADE_CHOICES = [
        ('COPA', 'COPA'),
        ('MMV', 'MMV'),
    ]
    
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    trade = models.CharField(max_length=4, choices=TRADE_CHOICES)
    remarks = models.TextField(blank=True ,default="")

    def __str__(self):
        return self.name
from django.db import models

class AdmissionCriteria(models.Model):
    content = models.TextField()  # Store the content for the <p> tag

    def __str__(self):
        return "Admission Criteria Content"
from django.db import models

class NCVTTrade(models.Model):
    name = models.CharField(max_length=200)
    affiliated_to = models.CharField(max_length=10, choices=[('NCVT', 'NCVT'), ('SCVT', 'SCVT')])
    remarks = models.TextField(blank=True, null=True)
    intake_capacity = models.PositiveIntegerField(default=0)  # New field for intake capacity
    units = models.CharField(max_length=100, blank=True, null=True)  # New field for units

    def __str__(self):
        return self.name
# models.py
from django.db import models

# models.py
from django.db import models

class Placement(models.Model):
    trainee_name = models.CharField(max_length=100)
    industry_name = models.CharField(max_length=100)
    package = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True , default="")
    trade = models.CharField(max_length=50)  # New column for trade

    def __str__(self):
        return self.trainee_name

# models.py
from django.db import models

class ECA(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField()  # More than 500 words can be added
    date = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
# models.py
from django.db import models

class IndustryCollaboration(models.Model):
    MOU_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    
    industry_name = models.CharField(max_length=200)
    partner_name = models.CharField(max_length=200)
    mou_signed = models.CharField(max_length=3, choices=MOU_CHOICES, default='No')
    mou_date = models.DateField()
    valid_upto = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.industry_name} - {self.partner_name}"
# models.py
from django.db import models

class RTI(models.Model):
    information = models.TextField()  # Store RTI information
    attachment = models.FileField(upload_to='rti_attachments/', null=True, blank=True)  # Store optional PDF attachment
    remarks = models.TextField(null=True, blank=True)  # Store remarks

    def __str__(self):
        return f"RTI Information - {self.id}"
# models.py
from django.db import models

class Inspection(models.Model):
    inspection_name = models.CharField(max_length=255)  # Name of the inspection
    agency = models.CharField(max_length=255)  # Name of the agency
    date = models.DateField()  # Date of the inspection
    result = models.FileField(upload_to='inspection_results/', null=True, blank=True)  # Optional PDF file upload for result
    remarks = models.TextField(null=True, blank=True)  # Remarks

    def __str__(self):
        return f"Inspection - {self.inspection_name}"
# models.py
from django.db import models

class ApprenticeshipSection(models.Model):
    section_name = models.CharField(max_length=255)  # Name of the section (Eligibility, Application Process, Benefits)
    content = models.TextField()  # Content of the section (Paragraph)
    color = models.CharField(max_length=7, default='#FFFAF0')  # Optional: Background color for each section

    def __str__(self):
        return self.section_name
from django.db import models

class CTSContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)  # To identify each section

    def __str__(self):
        return self.title
from django.db import models

class CommitteeMember(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    address = models.TextField()
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name
# models.py
from django.db import models

class Achievement(models.Model):
    description = models.TextField()

    def __str__(self):
        return f"Achievement {self.id}"
from django.db import models

# HPKVN Training Program Model
class HPKVNTrainingProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# HPKVN Enrollment Process Model
class HPKVNEnrollmentProcess(models.Model):
    step = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.step

# HPKVN Placement Model
class HPKVNPlacement(models.Model):
    company_name = models.CharField(max_length=100)
    placement_date = models.DateField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.company_name

# HPKVN Trainee Model
class HPKVNTrainee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name
from django.db import models

class OJTContent(models.Model):
    link_1_text = models.CharField(max_length=255, blank=True, null=True)
    div_1_content = models.TextField(blank=True, null=True)

    link_2_text = models.CharField(max_length=255, blank=True, null=True)
    div_2_content = models.TextField(blank=True, null=True)

    link_3_text = models.CharField(max_length=255, blank=True, null=True)
    div_3_content = models.TextField(blank=True, null=True)

    

    def __str__(self):
        return "OJT Content"
from django.db import models

class OJTTrainee(models.Model):
    sn = models.AutoField(primary_key=True)  # Auto-incremented field for SN
    name = models.CharField(max_length=100)
    ojt_location = models.CharField(max_length=200)
    trade = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
