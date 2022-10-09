from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator


sectionChoices = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),

)
classChoices = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('Masters', 'Masters'),

)

deptChoice = (
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('ETE', 'ETE'),
    ('EEE', 'EEE'),

    ('CE', 'CE'),
    ('BECM', 'BECM'),
    ('Arch', 'Arch'),
    ('URP', 'URP'),

    ('ME', 'ME'),
    ('IPE', 'IPE'),
    ('GCE', 'GCE'),
    ('MTE', 'MTE'),
    ('MSE', 'MSE'),
    ('CFPE', 'CFPE'),

    ('Chem', 'Chem'),
    ('Math', 'Math'),
    ('Phy', 'Phy'),
    ('Hum', 'Hum'),

)


class Student(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    department = models.CharField(max_length=5, choices=deptChoice, default="CSE")
    year = models.CharField(max_length=7, choices=classChoices)
    section = models.CharField(max_length=2, choices=sectionChoices)
    roll = models.IntegerField(default=1903)
    phoneNum = models.BigIntegerField(default=880)
    fathersName = models.CharField(max_length=200)
    fathersNum = models.BigIntegerField(default=880)
    mothersName = models.CharField(max_length=200)
    mothersNum = models.BigIntegerField(default=880)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.roll}-{self.department}'


posChoice = (
    ('Lecturer', 'Lecturer'),
    ('Professor ', 'Professor '),
    ('Assistant Professor ', 'Assistant Professor '),
    ('Head Master', 'Head Master'),

)


class Teacher(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    mobile = models.BigIntegerField(default=880)
    position = models.CharField(
        max_length=20, choices=posChoice, blank=False, default="")
    department = models.CharField(max_length=5, choices=deptChoice, default="")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
