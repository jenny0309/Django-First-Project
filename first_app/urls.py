from django.urls import path, include
from first_app import views, urls

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('formpage/', views.form_name_view, name='form_name'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]