from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('docx-to-pdf/', views.docx_to_pdf, name='docx_to_pdf'),
    path('image-to-pdf/', views.image_to_pdf, name='image_to_pdf'),
    path('pdf-to-docx/', views.pdf_to_docx, name='pdf_to_docx'),
    path('pdf-to-text/', views.pdf_to_text, name='pdf_to_text'),
]
