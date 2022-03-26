from django.db import models
from django.urls import reverse
import uuid

class Lecturer(models.Model):
    name=models.CharField(max_length=100)
    college=models.ForeignKey('College',on_delete=models.CASCADE,null=True)
    qualification=models.TextField(max_length=1000,help_text='Enter the qualification of lecturer')
    rating=models.DecimalField(max_digits=5, decimal_places=2)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    student_passing_percentage=models.DecimalField(max_digits=5, decimal_places=2,null=True)
    percentage_of_student_above_60=models.DecimalField(max_digits=5, decimal_places=2,null=True)
    def __str__(self):
        return f'{self.name} ({self.college})'

    def get_absolute_url(self):
        return reverse('lecturer-detail',args=[str(self.id)])

    
class LecturerFeedback(models.Model):
    lecturer=models.ForeignKey('Lecturer',on_delete=models.RESTRICT,null=True)
    one=models.CharField(max_length=200,null=True)
    two=models.CharField(max_length=200,null=True)
    three=models.CharField(max_length=200,null=True)
    four=models.CharField(max_length=200,null=True)
    w1=models.IntegerField(default=0,null=True)
    w2=models.IntegerField(default=0,null=True)
    w3=models.IntegerField(default=0,null=True)
    w4=models.IntegerField(default=0,null=True)
    def __str__(self):
        return f'{self.id} ({self.lecturer.name})'


class College(models.Model):
    name=models.CharField(max_length=100)
    rating=models.DecimalField(max_digits=5, decimal_places=2)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    student_passing_percentage=models.DecimalField(max_digits=5, decimal_places=2,null=True)
    percentage_of_student_above_60=models.DecimalField(max_digits=5, decimal_places=2,null=True)

    # class Meta:
    #     ordering=['name','founder_name']

    def get_absolute_url(self):
        return reverse("college-detail", args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'
    
class CollegeFeedback(models.Model):
    college=models.ForeignKey('College',on_delete=models.RESTRICT,null=True)
    one=models.CharField(max_length=200,null=True)
    two=models.CharField(max_length=200,null=True)
    three=models.CharField(max_length=200,null=True)
    four=models.CharField(max_length=200,null=True)
    w1=models.IntegerField(default=0,null=True)
    w2=models.IntegerField(default=0,null=True)
    w3=models.IntegerField(default=0,null=True)
    w4=models.IntegerField(default=0,null=True)
    def __str__(self):
        return f'{self.id} ({self.college.name})'

class Lrating(models.Model):
    lecturer=models.ForeignKey('Lecturer',on_delete=models.RESTRICT,null=True)
    form=models.ForeignKey('LecturerFeedback',on_delete=models.RESTRICT,null=True)
    r1=models.IntegerField(default=0,null=True)
    r2=models.IntegerField(default=0,null=True)
    r3=models.IntegerField(default=0,null=True)
    r4=models.IntegerField(default=0,null=True)
    total=models.DecimalField(max_digits=5,decimal_places=2,null=True)

class Crating(models.Model):
    college=models.ForeignKey('College',on_delete=models.RESTRICT,null=True)
    form=models.ForeignKey('CollegeFeedback',on_delete=models.RESTRICT,null=True)
    r1=models.IntegerField(default=0,null=True)
    r2=models.IntegerField(default=0,null=True)
    r3=models.IntegerField(default=0,null=True)
    r4=models.IntegerField(default=0,null=True)
    total=models.DecimalField(max_digits=5,decimal_places=2,null=True)
