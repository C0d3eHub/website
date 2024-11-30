from django.db import models
from django.utils import timezone


# Header modelfrom django.db import models

class HeaderContent(models.Model):
    # Existing fields
    logo = models.ImageField(upload_to='logos/')  # Left logo
    right_logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # Right logo (new)
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
    
    # New fields
    father_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], 
        null=True, 
        blank=True
    )
    aadharcard2 = models.CharField(max_length=20, null=True, blank=True)
    total_experience = models.IntegerField(null=True, blank=True)  # In years
    qualification = models.CharField(max_length=200, null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)  # Multiple hobbies can be listed as text
    last_working_place = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

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
    
    # New fields
    father_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], 
        null=True, 
        blank=True
    )
    aadharcard1 = models.CharField(max_length=20, null=True, blank=True)
    total_experience = models.IntegerField(null=True, blank=True)  # In years
    qualification = models.CharField(max_length=200, null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)  # Multiple hobbies can be listed as text
    last_working_place = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

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
from django.db import models

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

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    trainee_id = models.CharField(max_length=20, unique=True)  # New unique trainee_id field
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

    # New Fields
    highest_qualification = models.CharField(max_length=100, blank=True, null=True)
    marks_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Percentage
    marks_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Percentage
    hobbies = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)  # New gender field

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
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Added description field
    
    def __str__(self):
        return self.name

    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15,blank=True)  # Added phone number field
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


class AdmissionCriteria(models.Model):
    content = models.TextField()  # Store the content for the <p> tag

    def __str__(self):
        return "Admission Criteria Content"


class NCVTTrade(models.Model):
    name = models.CharField(max_length=200)
    affiliated_to = models.CharField(max_length=10, choices=[('NCVT', 'NCVT'), ('SCVT', 'SCVT')])
    remarks = models.TextField(blank=True, null=True)
    intake_capacity = models.PositiveIntegerField(default=0)  # New field for intake capacity
    units = models.CharField(max_length=100, blank=True, null=True)  # New field for units

    def __str__(self):
        return self.name
# models.py




class Placement(models.Model):
    trainee_name = models.CharField(max_length=100)
    industry_name = models.CharField(max_length=100)
    package = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True , default="")
    trade = models.CharField(max_length=50)  # New column for trade

    def __str__(self):
        return self.trainee_name

# models.py


class ECA(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField()  # More than 500 words can be added
    date = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
# models.py


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


class RTI(models.Model):
    information = models.TextField()  # Store RTI information
    attachment = models.FileField(upload_to='rti_attachments/', null=True, blank=True)  # Store optional PDF attachment
    remarks = models.TextField(null=True, blank=True)  # Store remarks

    def __str__(self):
        return f"RTI Information - {self.id}"
# models.py


class Inspection(models.Model):
    inspection_name = models.CharField(max_length=255)  # Name of the inspection
    agency = models.CharField(max_length=255)  # Name of the agency
    date = models.DateField()  # Date of the inspection
    result = models.FileField(upload_to='inspection_results/', null=True, blank=True)  # Optional PDF file upload for result
    remarks = models.TextField(null=True, blank=True)  # Remarks

    def __str__(self):
        return f"Inspection - {self.inspection_name}"
# models.py


class ApprenticeshipSection(models.Model):
    section_name = models.CharField(max_length=255)  # Name of the section (Eligibility, Application Process, Benefits)
    content = models.TextField()  # Content of the section (Paragraph)
    color = models.CharField(max_length=7, default='#FFFAF0')  # Optional: Background color for each section

    def __str__(self):
        return self.section_name


class CTSContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)  # To identify each section

    def __str__(self):
        return self.title


class CommitteeMember(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    address = models.TextField()
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    description = models.TextField()

    def __str__(self):
        return f"Achievement {self.id}"


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


class OJTContent(models.Model):
    link_1_text = models.CharField(max_length=255, blank=True, null=True)
    div_1_content = models.TextField(blank=True, null=True)

    link_2_text = models.CharField(max_length=255, blank=True, null=True)
    div_2_content = models.TextField(blank=True, null=True)

    link_3_text = models.CharField(max_length=255, blank=True, null=True)
    div_3_content = models.TextField(blank=True, null=True)

    

    def __str__(self):
        return "OJT Content"


class OJTTrainee(models.Model):
    sn = models.AutoField(primary_key=True)  # Auto-incremented field for SN
    name = models.CharField(max_length=100)
    ojt_location = models.CharField(max_length=200)
    trade = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class Marks(models.Model):
    trainee_sn = models.ForeignKey(TraineeDetails, on_delete=models.CASCADE)
    monthly_attendance = models.IntegerField()
    trade_theory_marks = models.IntegerField()
    trade_practical_marks = models.IntegerField()
    es_marks = models.IntegerField()
    ws_marks = models.IntegerField()
    total_marks = models.IntegerField()
    remarks = models.TextField(blank=True)
    month = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.trainee_sn.name} - {self.month}"





class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/')  # Ensure you have media setup

    def __str__(self):
        return self.name



class Meeting(models.Model):
    sn = models.AutoField(primary_key=True)  # Automatically increments for each meeting
    agenda = models.TextField(blank=True, null=True)  # Agenda of the meeting
    date = models.DateField(blank=True, null=True)  # Date of the meeting
    time = models.TimeField(blank=True, null=True)  # Time of the meeting
    minutes = models.TextField(blank=True, null=True)  # Minutes of the meeting
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # Optional attachment

    def __str__(self):
        return f'Meeting {self.sn}'



#video


class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # Video upload
    youtube_link = models.URLField(blank=True, null=True)  # YouTube video link
    description = models.TextField(blank=True)  # Optional description
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Video {self.id}"



class Stream(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  # Optional
    intake_capacity = models.PositiveIntegerField(blank=True, null=True)  # Optional
    filled = models.PositiveIntegerField(blank=True, null=True)  # Optional
    unit = models.CharField(max_length=100, blank=True, null=True)  # Optional
    shift = models.CharField(max_length=50, blank=True, null=True)  # Optional
    syllabus = models.FileField(upload_to='syllabus_pdfs/', blank=True, null=True)  # Optional PDF upload
    remarks = models.TextField(blank=True, null=True)  # Optional

    def __str__(self):
        return self.name if self.name else "Unnamed Stream"





#reach us

class ReachUsContent(models.Model):
    location_url = models.TextField(help_text="Google Maps Embed URL", blank=False)
    description = models.TextField(help_text="Add a short description or contact info.", blank=False)

    def __str__(self):
        return "Reach Us Content"


#visiter counter


from django.db import models
from django.utils.timezone import now

from django.db import models

from django.db import models

class VisitorCounter(models.Model):
    # The total visitor count
    count = models.PositiveIntegerField(default=0)

    # Store IP addresses, sessions, and users (as JSON fields)
    visitor_ips = models.JSONField(default=dict)  # Stores IP addresses
    visitor_sessions = models.JSONField(default=dict)  # Stores session data
    visitor_users = models.JSONField(default=dict)  # Stores user IDs if logged in

    def __str__(self):
        return f"Visitor Count: {self.count}"





#grievance


class Grievance(models.Model):
    title = models.CharField(max_length=200)  # Title of the grievance
    description = models.TextField()  # Detailed description of the grievance
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')],
        default='Pending',
    )  # Status of the grievance
    response = models.TextField(blank=True, null=True)  # Admin's response to the grievance
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when grievance is created

    def __str__(self):
        return self.title
#chairman desk
# models.py
from django.db import models

class Chairman(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='chairman_images/')

    def __str__(self):
        return self.name
#study material


class StudyMaterial(models.Model):
    TRADE_CHOICES = [
        ('COPA', 'COPA'),
        ('MMV', 'MMV'),
        
        # Add more trades as needed
    ]
    
    sn = models.AutoField(primary_key=True)
    trade = models.CharField(max_length=50, choices=TRADE_CHOICES)
    topic = models.CharField(max_length=200)
    material = models.FileField(upload_to='study_materials/')  # Files stored in MEDIA_URL/study_materials/
    remarks = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.trade} - {self.topic}"
#online test
# models.py





class TradeForOnlineTest(models.Model):
    id = models.IntegerField(primary_key=True)  # Manually setting the primary key
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class TopicForOnlineTest(models.Model):
    trade = models.ForeignKey(TradeForOnlineTest, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name 


class QuestionForOnlineTest(models.Model):
    topic = models.ForeignKey(TopicForOnlineTest, on_delete=models.CASCADE)
    text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

    def __str__(self):
        return self.text

# tenders
# main_app/models.py

from django.db import models

class Tender(models.Model):
    STATUS_CHOICES = [
        ('Open Soon', 'Open Soon'),
        ('Upcoming', 'Upcoming'),
        ('Opened', 'Opened'),
        ('Closed', 'Closed'),
        ('Re-Open', 'Re-Open'),
        ('Pending', 'Pending'),
        ('Under Review', 'Under Review'),
        ('Awarded', 'Awarded'),
    ]

    particulars = models.CharField(max_length=255)
    attachment = models.FileField(upload_to='tenders/', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Upcoming')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.particulars
