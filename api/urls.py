from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("users", views.users),
    path("users/<int:uid>", views.users),
    path("atendance_list", views.attendance_list),
    path("live_capture", views.attendance_live_capture),
    path("refresh", views.refresh),
    path("data", views.new_record),
]

urlpatterns = format_suffix_patterns(urlpatterns)
