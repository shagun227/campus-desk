from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from courses.models import Course
from courses.services import EnrollmentError, enroll


def course_list(request: HttpRequest) -> HttpResponse:
    return render(request, "courses/list.html", {"courses": Course.objects.all()})


def course_detail(request: HttpRequest, code: str) -> HttpResponse:
    course = get_object_or_404(Course, code=code)
    error = ""
    if request.method == "POST":
        try:
            enroll(course, request.POST.get("student_name", ""), request.POST.get("email", ""))
            return redirect("course-detail", code=course.code)
        except EnrollmentError as exc:
            error = str(exc)
    return render(
        request,
        "courses/detail.html",
        {"course": course, "error": error, "enrollments": course.enrollments.all()},
    )
