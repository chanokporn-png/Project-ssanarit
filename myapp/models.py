from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=225)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True) #กรอกอัตโนมัติ
    # date = models.DateField(blank=True, null=True) #กรอกเอง

    def __str__(self):
        return self.name + ", "+str(self.age) #กำหนดรูปแบบการแสดงผลในหน้า admin 
    
# class Person(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
    # age = models.IntegerField()


class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')  # เก็บไฟล์วิดีโอ

    def __str__(self):
        return self.title
    


class sat_data(models.Model):
    bstar = models.FloatField()  # ตัวอย่างฟิลด์ที่คุณใช้
    # เพิ่มฟิลด์อื่น ๆ ที่มีในตารางฐานข้อมูลของคุณ เช่น
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
 