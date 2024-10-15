from django.urls import path
from . import views
from django.contrib import admin
from .views import header_content_view


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', views.index, name='index'),  # Homepage route    
    path('news/', views.news_list, name='news_list'),  # News and alerts
    path('principal_desk/', views.principal_desk_list, name='principal_desk_list'),  # Principal's Desk posts
    path('admission/', views.admission, name='admission'),  # Admission page route
    path('about/', views.about_institute_view, name='about_institute'),  # About Institute page
    path('electric_power_supply/', views.electric_power_supply, name='electric_power_supply'),  # Electric Power Supply page
    path('key_performance_indicator/', views.key_performance_indicator, name='key_performance_indicator'),  # Key Performance Indicator page
    path('institute_amenities/', views.institute_amenities, name='institute_amenities'),  # Institute Amenities page
    path('institute_infrastructure/', views.institute_infrastructure, name='institute_infrastructure'),  # Institute Infrastructure page
    path('trades/', views.trades, name='trades'),  # Trades page
    path('admission_criteria/', views.admission_criteria, name='admission_criteria'),  # Admission Criteria page
    path('trades_ncvt/', views.trades_ncvt, name='trades_ncvt'),  # Trades NCVT page
    path('overall_results/', views.overall_results, name='overall_results'),  # Overall Results page
    path('trade_wise_result/', views.trade_wise_result, name='trade_wise_result'),  # Trade-wise Results page
    path('session_wise_result/', views.session_wise_result, name='session_wise_result'),  # Session-wise Results page
    path('trade_infrastructure/', views.trade_infrastructure, name='trade_infrastructure'),  # Trade Infrastructure page
    path('placement/', views.placement, name='placement'),  # Placement page
    path('eca/', views.eca, name='eca'),  # Extra-curricular Activities page
    path('adminstaff/', views.adminstaff, name='adminstaff'),  # Administrative Staff page
    path('techstaff/', views.techstaff, name='techstaff'),  # Technical Staff page
    path('rti/', views.rti, name='rti'),  # RTI page
    path('ats/', views.ats, name='ats'),  # ATS page
    path('cts/', views.cts, name='cts'),  # CTS page
    path('imc/', views.imc, name='imc'),  # IMC page
    path('hpkvn/', views.hpkvn, name='hpkvn'),  # HPKVN page
    path('ojt/', views.ojt, name='ojt'),  # OJT page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('admin/header-content/', header_content_view, name='header_content'),
    
    
]
