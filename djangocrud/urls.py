from django.contrib import admin
from django.urls import path
from enroll import views
# from django.http import HttpResponseNotFound

# urlpatterns = [
#     # Other URLs...
#     path('favicon.ico', lambda x: HttpResponseNotFound()),  # Handle favicon request with 404
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('save/', views.save_data, name='save'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.edit_data, name='edit'),
    # path('favicon.ico', lambda x: HttpResponseNotFound()),
]
