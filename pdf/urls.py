from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('display/', views.display_pdf, name='display_pdf'),
    path('display_maths/', views.display_maths, name='display_math'),
    path('display_bme/', views.display_bme, name='display_bme'),
    path('display_chem/', views.display_chem, name='display_chem'),
    path('display_be/', views.display_be, name='display_be'),
    path('display_mos/', views.display_be, name='display_mos'),
    path('pdf/display_be/<str:success_message>/', views.display_be, name='display_be'),
    path('display/<str:success_message>/', views.display_pdf, name='display_pdf_with_message'),  # Add this line
    path('reward_selection/', views.reward_selection, name='reward_selection'),
    path('first/', views.first_year, name='first')
    

]
