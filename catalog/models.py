from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Skill(models.Model):
    name=models.CharField(max_length=200,help_text='Enter a skill (e.g. Web development)')

    def __str__(self):
        return self.name

class Job(models.Model):
    title=models.CharField(max_length=200)
    company=models.ForeignKey('Company',on_delete=models.CASCADE,null=True)
    description=models.TextField(max_length=1000,help_text='Enter a breif description of the job')
    skills=models.ManyToManyField(Skill,help_text='Select skills required for the job')

    def __str__(self):
        return f'{self.title} ({self.company})'

    def get_absolute_url(self):
        return reverse('job-detail',args=[str(self.id)])
    def display_skill(self):
        """Create a string for the Skill. This is required to display skill in Admin."""
        return ', '.join(skill.name for skill in self.skills.all()[:3])

    display_skill.short_description = 'Skill'

    
class JobInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique ID for this particular book across whole library')
    job=models.ForeignKey('Job',on_delete=models.RESTRICT,null=True)
    location=models.CharField(max_length=200)
    last_date=models.DateField(null=True,blank=True)

    JOB_STATUS=(
        ('o','Occupied'),
        ('a','Available'),
        ('r','Reserved'),
    )

    status=models.CharField(
        max_length=1,
        choices=JOB_STATUS,
        blank=True,
        default='o',
        help_text='Job availability',
    )

    class Meta:
        ordering=['last_date']

    def __str__(self):
        return f'{self.id} ({self.job.title})'


class Company(models.Model):
    name=models.CharField(max_length=100)
    founder_name=models.CharField(max_length=100)
    date_of_est=models.DateField(null=True,blank=True)

    class Meta:
        ordering=['name','founder_name']

    def get_absolute_url(self):
        return reverse("company-detail", args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'
    