from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=160)
    seats = models.PositiveIntegerField()

    def seats_taken(self) -> int:
        return self.enrollments.filter(status="enrolled").count()

    def seats_left(self) -> int:
        return self.seats - self.seats_taken()

    def __str__(self) -> str:
        return f"{self.code} {self.title}"


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ("enrolled", "Enrolled"),
        ("waitlisted", "Waitlisted"),
        ("cancelled", "Cancelled"),
    ]

    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=120)
    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="enrolled")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["course", "email"], name="unique_course_email")
        ]
