from django.urls import path

from courses import views

urlpatterns = [
    path("", views.course_list, name="course-list"),
    path("courses/<str:code>/", views.course_detail, name="course-detail"),
]
