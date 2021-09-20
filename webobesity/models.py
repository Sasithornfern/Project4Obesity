from django.db import models

# Create your models here.
class NameHospital(models.Model):
    name = models.CharField(max_length=200)#ชื่อโรงพยาบาล
    provinces = models.CharField(max_length=200) #จังหวัด
    Phonenumber = models.CharField(max_length=200)#เบอร์โทร
    Desc = models.CharField(max_length=500)#รายละเอียดเพิ่มเติม


class Dobesity(models.Model):
    eat=models.CharField(max_length=200) #การปรับเปลี่ยนพฤติกรรมการกิน
    exercise=models.CharField(max_length=200)#การปรับเปลี่ยนพฤติกรรมการออกกำลังกาย
    feel=models.CharField(max_length=200)#การปรับเปลี่ยนอารมณ์

class diabetes(models.Model):
    eating=models.TextField()#การกินอาหาร
    exercises=models.TextField()#การออกกำลังกาย
    protect=models.TextField()#การป้องกัน

class hypertention(models.Model):
    habit=models.TextField()#พฤติกรรม
    exercises=models.TextField()#การออกกำลังกาย
    feeling=models.TextField()#ความเครียด

class dyslipidemia(models.Model):
    eat=models.TextField()#การกิน
    exercises=models.TextField()#การออกกำลังกาย


class Question(models.Model):
    score = models.CharField(max_length=200)
    typename = models.CharField(max_length=200)

class EatQuestion(models.Model):
    score1 = models.CharField(max_length=200)
    typename1 = models.CharField(max_length=200)

class exerciseQuestion(models.Model):
    score2 = models.CharField(max_length=200)
    typename2 = models.CharField(max_length=200)