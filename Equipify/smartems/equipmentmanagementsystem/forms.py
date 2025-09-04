
import datetime
from django import forms
from equipmentmanagementsystem.models import Category, Room, Equipment
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import F

from equipmentmanagementsystem.models import CustomUser
from equipmentmanagementsystem.models import AllocatorHOD


class AddManagerForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    phonenumber = forms.IntegerField(label="Phone Number", widget=forms.NumberInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    fullname = forms.CharField(label="Fullname", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    profilepicture = forms.FileField(label="Profile Picture", max_length=50, widget=forms.FileInput(attrs={"class":"form-control"}))

class EditManagerForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    phonenumber = forms.IntegerField(label="Phone Number", widget=forms.NumberInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    fullname = forms.CharField(label="Fullname", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    profilepicture = forms.FileField(label="Profile Picture", max_length=50, widget=forms.FileInput(attrs={"class":"form-control"}), required=False)



class AddAllocatorForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    phonenumber = forms.IntegerField(label="Phone Number", widget=forms.NumberInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    fullname = forms.CharField(label="Fullname", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    registrationnumber = forms.IntegerField(label="Registration Number", widget=forms.NumberInput(attrs={"class":"form-control"}))
    faculty = forms.CharField(label="Faculty", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    speciality = forms.CharField(label="Speciality", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    profilepicture = forms.FileField(label="Profile Picture", max_length=50, widget=forms.FileInput(attrs={"class":"form-control"}))
    role = forms.ChoiceField(label="Role", choices=(('student', 'Student'), ('researcher', 'Researcher')), widget=forms.Select(attrs={"class":"form-control"}))

# def clean_email(self):
#         email = self.cleaned_data['email']
#         if CustomUser.objects.filter(email=email).exists():
#             existing_user = CustomUser.objects.get(email=email)
#             if existing_user.allocation is not None:
#                 raise ValidationError("Email is already registered as an allocator.")
#         return email

# def clean_username(self):
#         username = self.cleaned_data['username']
#         if CustomUser.objects.filter(username=username).exists():
#             existing_user = CustomUser.objects.get(username=username)
#             if existing_user.allocation is not None:
#                 raise ValidationError("Username is already registered as an allocator.")
#         return username



class EditAllocatorForm(forms.Form):
    ROLES = [
        ('student', 'Student'),
        ('researcher', 'Researcher'),
    ]
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    phonenumber = forms.IntegerField(label="Phone Number", widget=forms.NumberInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    fullname = forms.CharField(label="Fullname", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    registrationnumber = forms.IntegerField(label="Registration Number",
                                            widget=forms.NumberInput(attrs={"class": "form-control"}))
    faculty = forms.CharField(label="Faculty", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    speciality = forms.CharField(label="Speciality", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    role = forms.ChoiceField(label="Role", choices=ROLES, widget=forms.Select(attrs={"class": "form-control"}))                             
    profilepicture = forms.FileField(label="Profile Picture", max_length=50, widget=forms.FileInput(attrs={"class": "form-control"}))

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     super(EditAllocatorForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].initial = self.user.email
    #     self.fields['phonenumber'].initial = self.user.profile.phonenumber
    #     self.fields['username'].initial = self.user.username
    #     self.fields['first_name'].initial = self.user.first_name
    #     self.fields['last_name'].initial = self.user.last_name
    #     self.fields['fullname'].initial = self.user.profile.fullname
    #     self.fields['registrationnumber'].initial = self.user.profile.registrationnumber
    #     self.fields['faculty'].initial = self.user.profile.faculty
    #     self.fields['speciality'].initial = self.user.profile.speciality
    #     self.fields['role'].initial = self.user.profile.role
    #     self.fields['profilepicture'].initial = self.user.profile.profilepicture

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if email != self.user.email and User.objects.filter(email=email).exists():
    #         raise ValidationError("Email already exists")
    #     return email

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if username != self.user.username and User.objects.filter(username=username).exists():
    #         raise ValidationError("Username already exists")
    #     return username
    


class AddCategoryForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label="Description", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    #icone = forms.FileField(label="Icone", max_length=50, widget=forms.FileInput(attrs={"class":"form-control"}))



class EditCategoryForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label="Description", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    #icone = forms.FileField(label="Icone", max_length=50, widget=forms.FileInput(attrs={"class":"form-control"}))


class AddRoomForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    location = forms.CharField(label="Location", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    capacity = forms.IntegerField(label="Capacity",
                                            widget=forms.NumberInput(attrs={"class": "form-control"}))



class EditRoomForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    location = forms.CharField(label="Location", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    capacity = forms.IntegerField(label="Capacity",
                                            widget=forms.NumberInput(attrs={"class": "form-control"}))


                                    


class AddEquipmentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    serialnumber = forms.IntegerField(label="Serial Number", widget=forms.NumberInput(attrs={"class": "form-control"}))
    type = forms.CharField(label="Type", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    brand = forms.CharField(label="Brand", max_length=50,
                             widget=forms.TextInput(attrs={"class": "form-control"}))
    model = forms.CharField(label="Model", max_length=50,
                             widget=forms.TextInput(attrs={"class": "form-control"}))
    code = forms.CharField(label="Code", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    totalnumber = forms.IntegerField(label="Total Number", widget=forms.NumberInput(attrs={"class": "form-control"}))
    category = forms.ChoiceField(label="Category", choices=[], widget=forms.Select(attrs={"class": "form-control"}))
    room = forms.ChoiceField(label="Room", choices=[], widget=forms.Select(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        self.fields['category'].choices = [(category.id, category.name) for category in categories]
        rooms = Room.objects.all()
        self.fields['room'].choices = [(room.id, room.name) for room in rooms]


class EditEquipmentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    serialnumber = forms.IntegerField(label="Serial Number", widget=forms.NumberInput(attrs={"class": "form-control"}))
    type = forms.CharField(label="Type", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    brand = forms.CharField(label="Brand", max_length=50,
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    model = forms.CharField(label="Model", max_length=50,
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    code = forms.CharField(label="Code", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    totalnumber = forms.IntegerField(label="Total Number", widget=forms.NumberInput(attrs={"class": "form-control"}))
    category = forms.ChoiceField(label="Category", choices=[], widget=forms.Select(attrs={"class": "form-control"}))
    room = forms.ChoiceField(label="Room", choices=[], widget=forms.Select(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        self.fields['category'].choices = [(category.id, category.name) for category in categories]
        rooms = Room.objects.all()
        self.fields['room'].choices = [(room.id, room.name) for room in rooms]



# class AddEquipmentPlanningForm(forms.Form):
#     DAY_CHOICES = [
#         ('sunday', 'Sunday'),
#         ('monday', 'Monday'),
#         ('tuesday', 'Tuesday'),
#         ('wednesday', 'Wednesday'),
#         ('thursday', 'Thursday'),
#         ('saturday', 'Saturday'),
#     ]
#     TIME_CHOICES = [
#         (datetime.time(8, 0), '08:00'),
#         (datetime.time(9, 0), '09:00'),
#         (datetime.time(10, 0), '10:00'),
#         (datetime.time(11, 0), '11:00'),
#         (datetime.time(12, 0), '12:00'),
#         (datetime.time(13, 0), '13:00'),
#         (datetime.time(14, 0), '14:00'),
#         (datetime.time(15, 0), '15:00'),
#         (datetime.time(16, 0), '16:00'),
#     ]
#     equipments = Equipment.objects.all()
#     equipment_list=[]
#     for equipment in equipments :
#         small_equipment = (equipment.id, equipment.name)
#         equipment_list.append(small_equipment)
#     equipment = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"}))
#     day = forms.ChoiceField(choices=DAY_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
#     start_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
#     end_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))

class AddEquipmentPlanningForm(forms.Form):
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
    equipments = Equipment.objects.all()
    equipment_list = [(equipment.id, equipment.name) for equipment in equipments]
    equipment = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"}))
    day = forms.ChoiceField(choices=DAY_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    start_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    end_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    

class EditEquipmentPlanningForm(forms.Form):
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
    equipments = Equipment.objects.all()
    equipment_list=[]
    for equipment in equipments :
        small_equipment = (equipment.id, equipment.name)
        equipment_list.append(small_equipment)
    equipment = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"}))
    day = forms.ChoiceField(choices=DAY_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    start_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    end_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))    

# class EquipmentAllocationForm(forms.Form):
#     equipments = Equipment.objects.all()
#     equipment_list=[]
#     for equipment in equipments :
#         small_equipment = (equipment.id, equipment.name)
#         equipment_list.append(small_equipment)
#     equipment = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"}))
#     start_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#     end_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

class EquipmentAllocationForm(forms.Form):
    start_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        equipment_list = []
        available_equipment = Equipment.objects.exclude(
            equipmentallocation__start_datetime__lt=F('equipmentallocation__end_datetime'),
            equipmentallocation__end_datetime__gt=F('equipmentallocation__start_datetime'),
        ).distinct()
        for equipment in available_equipment:
            small_equipment = (equipment.id, equipment.name)
            equipment_list.append(small_equipment)
        self.fields['equipment'] = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"}))







# class AddAllocationForm(forms.Form):
#     equipments = Equipment.objects.all()
#     equipment_list=[]
#     for equipment in equipments :
#         small_equipment = (equipment.id, equipment.name)
#         equipment_list.append(small_equipment)
#     equipment = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"}))
#     allocators = AllocatorHOD.objects.all()
#     allocator_list=[]
#     for allocator in allocators :
#         small_allocator = (allocator.id, allocator.fullname)
#         allocator_list.append(small_allocator)
#     allocator = forms.ChoiceField(label="Allocator", choices=allocator_list, widget=forms.Select(attrs={"class": "form-control"}))
#     start_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#     end_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))  
# 
class AddAllocationForm(forms.Form):
    allocators = AllocatorHOD.objects.all()
    allocator_list=[]
    for allocator in allocators :
        small_allocator = (allocator.id, allocator.fullname)
        allocator_list.append(small_allocator)
    allocator = forms.ChoiceField(label="Allocator", choices=allocator_list, widget=forms.Select(attrs={"class": "form-control"}))
    start_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        equipment_list = [(equipment.id, equipment.name) for equipment in Equipment.objects.filter(equipment_plannings__isnull=False)]
        self.fields['equipment'] = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"})) 







class EditAllocationForm(forms.Form):
    equipments = Equipment.objects.all()
    equipment_list=[]
    for equipment in equipments :
        small_equipment = (equipment.id, equipment.name)
        equipment_list.append(small_equipment)
    equipment = forms.ChoiceField(label="Equipment", choices=equipment_list, widget=forms.Select(attrs={"class": "form-control"}))
    allocators = AllocatorHOD.objects.all()
    allocator_list=[]
    for allocator in allocators :
        small_allocator = (allocator.id, allocator.fullname)
        allocator_list.append(small_allocator)
    allocator = forms.ChoiceField(label="Allocator", choices=allocator_list, widget=forms.Select(attrs={"class": "form-control"}))
    start_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))    







