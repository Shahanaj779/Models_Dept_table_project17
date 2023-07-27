from django.db import models

# Create your models here.
class Dept(models.Model):
    DNAME=models.CharField(max_length=100)
    DNO=models.PositiveIntegerField
    LOC=models.DurationField
class EMP(models.Model):
    ENAME=models.CharField(max_length=100)
    ENO=models.PositiveIntegerField
    DEPTNO=models.PositiveIntegerField

