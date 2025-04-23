from django.urls import path
from . import views
from django.contrib import admin
from .views import header_content_view, key_performance_indicator_view,trainee_view,study_material
from django.conf import settings
from django.conf.urls.static import static
from .admin import admin_site
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('custom-admin/', admin_site.urls, name='custom_admin'),
    path('', views.index, name='index'),  # Homepage route    
    path('news/', views.news_list, name='news_list'),  # News and alerts
    path('principal_desk/', views.principal_desk_list, name='principal_desk_list'),  # Principal's Desk posts
    path('admission/', views.admission, name='admission'),  # Admission page route
    path('about/', views.about_institute_view, name='about_institute'),  # About Institute page
    path('electric_power_supply/', views.electric_power_supply, name='electric_power_supply'),  # Electric Power Supply page
    path('key-performance-indicator/', key_performance_indicator_view, name='key_performance_indicator'),
    path('institute_amenities/', views.institute_amenities, name='institute_amenities'),  # Institute Amenities page
    path('institute_infrastructure/', views.institute_infrastructure, name='institute_infrastructure'),  # Institute Infrastructure page
    path('trades/', views.trades, name='trades'),
    path('admission_criteria/', views.admission_criteria, name='admission_criteria'),  # Admission Criteria page
    path('trades_ncvt/', views.trades_ncvt, name='trades_ncvt'),  # Trades NCVT page
    path('overall_results/', views.overall_results, name='overall_results'),  # Overall Results page
    path('trade_wise_result/', views.trade_wise_result, name='trade_wise_result'),  # Trade-wise Results page
    path('session_wise_result/', views.session_wise_result, name='session_wise_result'),  # Session-wise Results page
    path('trade_infrastructure/', views.trade_infrastructure, name='trade_infrastructure'),  # Trade Infrastructure page
    path('placement/', views.placement, name='placement'),  # Placement page
    path('eca/', views.eca, name='eca'),  # Extra-curricular Activities page
    path('adminstaff/', views.adminstaff, name='adminstaff'),  # Administrative Staff page
    path('adminstaff/<int:serial_number>/', views.adminstaff_detail, name='adminstaff_detail'),
    path('techstaff/', views.techstaff, name='techstaff'),  # Technical Staff page
    path('techstaff/', views.techstaff, name='techstaff_list'),
    path('techstaff/<int:serial_number>/', views.techstaff_detail, name='techstaff_detail'),
    path('rti/', views.rti, name='rti'),  # RTI page
    path('ats/', views.ats, name='ats'),  # ATS page
    path('cts/', views.cts, name='cts'),  # CTS page
    path('imc/', views.imc, name='imc'),  # IMC page
    path('hpkvn/', views.hpkvn, name='hpkvn'),  # HPKVN page
    path('ojt/', views.ojt, name='ojt'),  # OJT page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('admin/header-content/', header_content_view, name='header_content'),
    path('industry-collaboration/', views.industry_collaboration, name='industry_collaboration'),
    path('inspection/', views.inspection, name='inspection'),
    path('trainee_view/', trainee_view, name='trainee_view'),
    path('upload_trainee/', views.upload_trainee_details, name='upload_trainee'),
    path('bulk_upload/', views.bulk_upload_trainees, name='bulk_upload_page'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('upload/', views.upload_image, name='upload_image'),
    path('trainees/', views.trainee_list, name='trainee_list'),
    path('report-card/', views.report_card, name='report_card'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('success/', views.success, name='success'),    
    path('social-media/', views.social_media_page, name='social_media'),
    path('meetings/', views.meetings_view, name='meetings'),
    path('videos/', views.video_view, name='video'),
    path('detailtrade/', views.detailtrade_view, name='detailtrade'),
    path('reach_us/', views.reach_us, name='reach_us'),
    path('update-counter/', views.update_visitor_count, name='update_counter'),
    path('grievance/', views.grievance_list_create, name='grievance'),
    path('chairman-desk/', views.chairman_desk, name='chairman_desk'),
    path('study-material/', study_material, name='study_material'),
    path('select_test/', views.select_test, name='select_test'),
    path('start_test/<int:trade_id>/<topic_id>/<int:num_questions>/', views.start_test, name='start_test'),
    path('submit_test/', views.submit_test, name='submit_test'),
    path('start_test/', views.start_test, name='start_test'),
    path('trainee/<int:trainee_id>/', views.trainee_detail, name='trainee_detail'),
    path('fetch-topics/', views.fetch_topics, name='fetch_topics'),
    path('start_test/<int:trade_id>/<str:topic_id>/<int:num_questions>/<str:user_name>/<str:iti_name>/',views.start_test,name='start_test'),
    path('tenders/', views.tender_list, name='tender_list'),
    path('qpr/', views.qpr_view, name='qpr'),
    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
