from django.db import models
from django.core import validators as v
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import (
    validate_name_format,
    validate_school_email,
    validate_combination_format,
)

class Student(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_name_format],
    )
    student_email = models.EmailField(
        unique=True,
        validators=[validate_school_email],
    )
    personal_email = models.EmailField(
        blank=True,
        null=True,
        unique=True,
    )
    locker_number = models.IntegerField(
        unique=True,
        default=110,
        validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
    )
    locker_combination = models.CharField(
        max_length=20,
        default="12-12-12",
        validators=[validate_combination_format],
    )
    good_student = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, new_locker_number: int):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self, is_good_student: bool):
        self.good_student = is_good_student
        self.save()
