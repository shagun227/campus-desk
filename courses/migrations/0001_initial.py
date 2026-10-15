from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=20, unique=True)),
                ("title", models.CharField(max_length=160)),
                ("seats", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("student_name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("status", models.CharField(choices=[("enrolled", "Enrolled"), ("waitlisted", "Waitlisted"), ("cancelled", "Cancelled")], default="enrolled", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="enrollments", to="courses.course")),
            ],
        ),
        migrations.AddConstraint(
            model_name="enrollment",
            constraint=models.UniqueConstraint(fields=("course", "email"), name="unique_course_email"),
        ),
    ]
