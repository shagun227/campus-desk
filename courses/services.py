from courses.models import Course, Enrollment


class EnrollmentError(Exception):
    pass


def enroll(course: Course, student_name: str, email: str) -> Enrollment:
    email = email.strip().lower()
    if Enrollment.objects.filter(course=course, email=email).exists():
        raise EnrollmentError("This email is already registered for the course.")
    status = "enrolled" if course.seats_left() > 0 else "waitlisted"
    return Enrollment.objects.create(
        course=course,
        student_name=student_name.strip(),
        email=email,
        status=status,
    )
