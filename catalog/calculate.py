from django.db.models import Avg
from catalog.models import Lecturer,College,LecturerFeedback,CollegeFeedback,Lrating,Crating

def calcc():
    list=College.objects.all()
    for coll in list:
        a=Crating.objects.filter(college=coll).aggregate(Avg('total'))
        h1=float(coll.student_passing_percentage)
        h2=float(coll.percentage_of_student_above_60)
        h=((h1+h2)/2)*0.4
        coll.rating=float(a['total__avg'])+h
        coll.save()

def calcl():
    list=Lecturer.objects.all()
    for lec in list:
        a=Lrating.objects.filter(lecturer=lec).aggregate(Avg('total'))
        lec.student_passing_percentage
        h1=float(lec.student_passing_percentage)
        h2=float(lec.percentage_of_student_above_60)
        h=((h1+h2)/2)*0.4
        lec.rating=float(a['total__avg'])+h
        lec.save()
