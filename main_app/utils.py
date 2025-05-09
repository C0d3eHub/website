# utils.py
from .models import HeaderContent

def get_header_content():
    return HeaderContent.objects.first()  # Fetch the first instance of header content
# In utils.py

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
