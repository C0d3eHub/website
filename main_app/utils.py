# utils.py
from .models import HeaderContent

def get_header_content():
    return HeaderContent.objects.first()  # Fetch the first instance of header content
