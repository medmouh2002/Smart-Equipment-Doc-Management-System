

import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ValidationError



# Create your models here.

class CustomUser(AbstractUser):
    email= models.EmailField(unique=True)
    pass
    user_type_data = ((1, "HOD"), (2, "ManagerHOD"), (3, "AllocatorHOD"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=100)


class AdminHOD(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phonenumber = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ManagerHOD(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phonenumber = models.IntegerField(null = True)
    profilepicture = models.ImageField(null = True,  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AllocatorHOD(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('researcher', 'Researcher'),
    ]
    id = models.BigAutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phonenumber = models.IntegerField(null = True)
    manager = models.ForeignKey(ManagerHOD, models.CASCADE, null=True)
    registrationnumber = models.IntegerField(null = True, unique=True)
    faculty = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    profilepicture  = models.ImageField(null = True,  blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    





class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    objects = models.Manager()    


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField(null = True)
    def __str__(self):
        return self.name

    objects = models.Manager()

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    serialnumber = models.IntegerField(null = True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    manager = models.ForeignKey(ManagerHOD, models.CASCADE, null=True)
    model = models.CharField(max_length=255)
    totalnumber = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def is_day_allowed(self, day):
        return self.allowed_days.filter(day=day).exists()

    def is_time_allowed(self, time):
        return self.allowed_days.filter(start_time__lte=time, end_time__gte=time).exists()
    objects = models.Manager()


class EquipmentPlanning(models.Model):
    DAY_CHOICES = [
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('saturday', 'Saturday'),
    ]
    TIME_CHOICES = [
        (datetime.time(8, 0), '08:00'),
        (datetime.time(9, 0), '09:00'),
        (datetime.time(10, 0), '10:00'),
        (datetime.time(11, 0), '11:00'),
        (datetime.time(12, 0), '12:00'),
        (datetime.time(13, 0), '13:00'),
        (datetime.time(14, 0), '14:00'),
        (datetime.time(15, 0), '15:00'),
        (datetime.time(16, 0), '16:00'),
    ]
    id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='equipment_plannings')
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default='saturday')
    start_time = models.TimeField(choices=TIME_CHOICES, default=datetime.time(8, 0))
    end_time = models.TimeField(choices=TIME_CHOICES, default=datetime.time(16, 0))
    manager = models.ForeignKey(ManagerHOD, models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class EquipmentAllowedDays(models.Model):
    DAY_CHOICES = [
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('saturday', 'Saturday'),
    ]

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    equipment_planning = models.ForeignKey(EquipmentPlanning, on_delete=models.CASCADE)
    allowed_day = models.CharField(max_length=10, choices=DAY_CHOICES)

    def __str__(self):
        return f"{self.day} - Equipment: {self.equipment} - Planning: {self.equipment_planning}"
    


class EquipmentAllocation(models.Model):
    id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    allocator = models.ForeignKey(AllocatorHOD, models.CASCADE, null=True)
    manager = models.ForeignKey(ManagerHOD, models.CASCADE, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()   

   





@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            ManagerHOD.objects.create(admin=instance)
        if instance.user_type == 3:
            AllocatorHOD.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.managerhod.save()
    if instance.user_type == 3:
        instance.allocatorhod.save()


class Notification(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def mark_as_read(self):
        self.is_read = True
        self.save()
    def __str__(self):
        return self.message




