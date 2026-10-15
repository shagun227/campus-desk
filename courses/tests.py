from django.test import TestCase

from courses.models import Course
from courses.services import EnrollmentError, enroll


class EnrollmentTests(TestCase):
    def test_second_student_is_waitlisted_when_the_course_is_full(self):
        course = Course.objects.create(code="CS101", title="Intro to Computing", seats=1)
        first = enroll(course, "Asha", "asha@example.com")
        second = enroll(course, "Ravi", "ravi@example.com")
        self.assertEqual(first.status, "enrolled")
        self.assertEqual(second.status, "waitlisted")

    def test_duplicate_email_is_rejected(self):
        course = Course.objects.create(code="CS102", title="Databases", seats=10)
        enroll(course, "Asha", "asha@example.com")
        with self.assertRaises(EnrollmentError):
            enroll(course, "Asha Two", "ASHA@example.com")
