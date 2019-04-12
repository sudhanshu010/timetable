from django.db import models
# from subject.models import subjects
from django.contrib.auth import get_user_model
from sortedm2m.fields import SortedManyToManyField
# Create your models here.

User = get_user_model()
class faculty_info(models.Model):
    name = models.CharField(max_length=50,blank=True)
    # username = models.ForeignKey(User,related_name='name',on_delete=models.CASCADE,blank=True)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    # subject_priority = SortedManyToManyField(subjects)
    # subject1 = models.ForeignKey(subjects, related_name='faculty1',on_delete=models.CASCADE,blank=True)
    #     # subject2 = models.ForeignKey(subjects, related_name='faculty2',on_delete=models.CASCADE,blank=True)
    #     # subject3 = models.ForeignKey(subjects, related_name='faculty3',on_delete=models.CASCADE,blank=True)
    #     # subject4 = models.ForeignKey(subjects, related_name='faculty4',on_delete=models.CASCADE,blank=True)
    #     # subject5 = models.ForeignKey(subjects, related_name='faculty5',on_delete=models.CASCADE,blank=True)
    # subject_assigned =  models.ManyToManyField(subjects,related_name='faculty_assigned',blank=True)

    def __str__(self):
        return f'{self.pk} {self.name}'