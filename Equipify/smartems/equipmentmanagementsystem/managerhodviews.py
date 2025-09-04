# import datetime
# from urllib import request

# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import redirect, render
# from django.urls import reverse

# from equipmentmanagementsystem.forms import AddAllocatorForm, EditAllocatorForm, AddEquipmentForm, EditEquipmentForm
# from equipmentmanagementsystem.models import CustomUser, Category, Equipment, Room, AllocatorHOD, ManagerHOD



# def showManagerPage(request):
#     equipments = Equipment.objects.all()
#     equipment_count = equipments.count()
#     return render(request, 'managerhod_templates/home_content.html', {"equipment_count":equipment_count})


# def addAllocator(request):
#     form = AddAllocatorForm()
#     return render(request, 'managerhod_templates/add_allocator.html', {"form":form})


# def saveAddAllocator(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         form = AddAllocatorForm(request.POST, request.FILES)
#         if form.is_valid():
#             fullname = form.cleaned_data['fullname']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             phonenumber = form.cleaned_data['phonenumber']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             speciality = form.cleaned_data['speciality']
#             faculty = form.cleaned_data['faculty']
#             registrationnumber = form.cleaned_data['registrationnumber']
#             role = form.cleaned_data['role']
#             profilepicture = request.FILES['profilepicture']
#             fss = FileSystemStorage()
#             filename = fss.save(profilepicture.name, profilepicture)
#             profilepictureurl = fss.url(filename)

#             try:
#                 user = CustomUser.objects.create_user(username=username,
#                                                       email=email, password=password, first_name=first_name,
#                                                       last_name=last_name, user_type=3)
#                 user.allocatorhod.fullname = fullname
#                 user.allocatorhod.phonenumber = phonenumber
#                 user.allocatorhod.speciality = speciality
#                 user.allocatorhod.faculty = faculty
#                 user.allocatorhod.registrationnumber = registrationnumber
#                 user.allocatorhod.profilepicture = profilepictureurl
#                 user.allocatorhod.role = role
#                 user.save()
#                 messages.success(request, "Successfully Added")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_allocator"))
#             except:
#                 messages.error(request, "Could Not Add ")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_allocator"))

#         else:
#             form = AddAllocatorForm(request.POST, request.FILES)
#             return render(request, 'managerhod_templates/add_allocator.html', {"form":form})





# def viewAllocator(request):
#     students = AllocatorHOD.objects.filter(admin__user_type=3, admin__allocatorhod__role='student')
#     researchers = AllocatorHOD.objects.filter(admin__user_type=3, admin__allocatorhod__role='researcher')
#     return render(request, 'managerhod_templates/view_allocator.html', {"students": students, "researchers": researchers})

# def editAllocator(request,allocator_id ):
#     request.session['allocator_id']=allocator_id
#     allocator = AllocatorHOD.objects.get(admin=allocator_id)
#     form = EditAllocatorForm()
#     form.fields['email'].initial=allocator.admin.email
#     form.fields['phonenumber'].initial = allocator.phonenumber
#     form.fields['username'].initial = allocator.admin.username
#     form.fields['first_name'].initial = allocator.admin.first_name
#     form.fields['last_name'].initial = allocator.admin.email
#     form.fields['fullname'].initial = allocator.fullname
#     form.fields['faculty'].initial = allocator.faculty
#     form.fields['speciality'].initial = allocator.speciality
#     form.fields['registrationnumber'].initial = allocator.registrationnumber
#     form.fields['role'].initial = allocator.admin.allocatorhod.role
#     form.fields['profilepicture'].initial = allocator.profilepicture
#     return render(request, 'managerhod_templates/edit_allocator.html', {"form": form, "id":allocator_id})

# def saveEditAllocator(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         allocator_id = request.session.get('allocator_id')
#         if allocator_id == None:
#             return HttpResponseRedirect("/view_allocator")
#         form = EditAllocatorForm(request.POST, request.FILES)
#         if form.is_valid():
#             role = form.cleaned_data['role']
#             fullname = form.cleaned_data['fullname']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             phonenumber = form.cleaned_data['phonenumber']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             faculty = form.cleaned_data['faculty']
#             speciality = form.cleaned_data['speciality']
#             registrationnumber = form.cleaned_data['registrationnumber']
            

#             if request.FILES.get('profilepicture', False):
#                 profilepicture = request.FILES['profilepicture']
#                 fss = FileSystemStorage()
#                 filename = fss.save(profilepicture.name, profilepicture)
#                 profilepictureurl = fss.url(filename)
#             else:
#                 profilepictureurl = None

#             try:

#                 user = CustomUser.objects.get(id=allocator_id)
#                 user.first_name = first_name
#                 user.last_name = last_name
#                 user.username = username
#                 user.email = email
#                 user.save()
#                 allocator_model = AllocatorHOD.objects.get(admin=allocator_id)
#                 allocator_model.fullname = fullname
#                 allocator_model.phonenumber = phonenumber
#                 allocator_model.faculty = faculty
#                 allocator_model.speciality = speciality
#                 allocator_model.registrationnumber = registrationnumber
#                 allocator_model.admin.allocatorhod.role = role

#                 if profilepictureurl != None:
#                     allocator_model.profilepicture = profilepictureurl

#                 allocator_model.save()
#                 del request.session['allocator_id']
#                 messages.success(request, "Successfully Edited")
#                 return HttpResponseRedirect("/edit_allocator/" + allocator_id)
#             except:
#                 messages.error(request, "Could Not Edit ")
#                 return HttpResponseRedirect("/edit_allocator/" + allocator_id)
#         else:
#             form = EditAllocatorForm(request.POST)
#             return render(request, 'managerhod_templates/edit_allocator.html', {"form": form, "id": allocator_id})








# def deleteAllocator(request, allocator_id):
#     allocator = AllocatorHOD.objects.get(admin=allocator_id)

    
#     allocator.delete()
#     return HttpResponseRedirect("/view_allocator")

# def addEquipment(request):
#     form = AddEquipmentForm()
#     return render(request, 'managerhod_templates/add_equipment.html', {"form":form})



# def saveAddEquipment(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         form = AddEquipmentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             type = form.cleaned_data['type']
#             brand = form.cleaned_data['brand']
#             model = form.cleaned_data['model']
#             code = form.cleaned_data['code']
#             serialnumber = form.cleaned_data['serialnumber']
#             totalnumber = form.cleaned_data['totalnumber']
#             category_id = form.cleaned_data['category']
#             room_id = form.cleaned_data['room']

#             try:
#                 equipment = Equipment(name=name, type=type,
#                                       brand=brand, model=model,
#                                       code=code, serialnumber=serialnumber,
#                                       totalnumber=totalnumber)
#                 category_obj = Category.objects.get(id=category_id)
#                 equipment.category_id=category_obj
#                 room_obj = Room.objects.get(id=room_id)
#                 equipment.room_id=room_obj
#                 equipment.save()
#                 messages.success(request, "Successfully Added")
#                 return HttpResponseRedirect("/add_equipment")
#             except:
#                 messages.error(request, "Could Not Add ")
#                 return HttpResponseRedirect("/add_equipment")
#         else:
#             form = AddEquipmentForm(request.POST)
#             return render(request, 'managerhod_templates/add_equipment.html', {"form":form})


# def viewEquipment(request):
#     equipment = Equipment.objects.all()
#     return render(request, 'managerhod_templates/view_equipment.html', {"equipments":equipment})


# def editEquipment(request, equipment_id):
#     request.session['equipment_id'] = equipment_id
#     equipment = Equipment.objects.get(id=equipment_id)
#     form = EditEquipmentForm()
#     form.fields['name'].initial = equipment.name
#     form.fields['serialnumber'].initial = equipment.serialnumber
#     form.fields['type'].initial = equipment.type
#     form.fields['brand'].initial = equipment.brand
#     form.fields['model'].initial = equipment.model
#     form.fields['code'].initial = equipment.code
#     form.fields['totalnumber'].initial = equipment.totalnumber
#     form.fields['category'].initial = equipment.category_id.id
#     form.fields['room'].initial = equipment.room_id.id

#     return render(request, 'managerhod_templates/edit_equipment.html', {"form": form, "id": equipment_id})


# def saveEditEquipment(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         equipment_id = request.session.get('equipment_id')
#         if equipment_id == None:
#             return HttpResponseRedirect("/view_equipment")
#         form = EditEquipmentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             type = form.cleaned_data['type']
#             brand = form.cleaned_data['brand']
#             model = form.cleaned_data['model']
#             code = form.cleaned_data['code']
#             serialnumber = form.cleaned_data['serialnumber']
#             totalnumber = form.cleaned_data['totalnumber']
#             category_id = form.cleaned_data['category']
#             room_id = form.cleaned_data['room']

#             try:

#                 equipment_model = Equipment.objects.get(id=equipment_id)
#                 equipment_model.name = name
#                 equipment_model.type = type
#                 equipment_model.brand = brand
#                 equipment_model.model = model
#                 equipment_model.code = code
#                 equipment_model.serialnumber = serialnumber
#                 equipment_model.totalnumber = totalnumber

#                 category=Category.objects.get(id=category_id)
#                 equipment_model.category_id= category

#                 room=Room.objects.get(id=room_id)
#                 equipment_model.room_id= room



#                 equipment_model.save()
#                 del request.session['equipment_id']
#                 messages.success(request, "Successfully Edited")
#                 return HttpResponseRedirect("/edit_equipment/" + equipment_id)
#             except:
#                 messages.error(request, "Could Not Edit ")
#                 return HttpResponseRedirect("/edit_equipment/" + equipment_id)
#         else:
#             form = EditAllocatorForm(request.POST)
#             return render(request, 'managerhod_templates/edit_equipment.html', {"form": form, "id": equipment_id})




# def deleteEquipment(request, equipment_id):
#     equipment = Equipment.objects.get(id=equipment_id)
#     equipment.delete()
#     return HttpResponseRedirect("/view_equipment")





# def manager_profile(request):
#     user = CustomUser.objects.get(id=request.user.id)
#     manager = ManagerHOD.objects.get(admin=user)
#     return render(request, "managerhod_templates/manager_profile.html", {"user": user, "manager": manager})


# def manager_profile_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("manager_profile"))
#     else:
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         fullname = request.POST.get("fullname")
#         phonenumber = request.POST.get("phonenumber")
#         password_changed = False

#         try:
#             customuser = CustomUser.objects.get(id=request.user.id)
#             customuser.email = email
#             if password is not None and password != "":
#                 customuser.set_password(password)
#                 customuser.save()
#                 password_changed = True

#             manager = ManagerHOD.objects.get(admin=customuser.id)
#             manager.fullname = fullname
#             manager.phonenumber = phonenumber
#             manager.save()

#             if password_changed:
#                 messages.success(request, "Successfully Updated Profile")
#                 return HttpResponseRedirect(reverse("show_login"))
#             else:
#                 messages.success(request, "Successfully Updated Profile")
#                 return HttpResponseRedirect(reverse("manager_profile"))
#         except:
#             messages.error(request, "Failed to Update Profile")
#             return HttpResponseRedirect(reverse("manager_profile"))  




import datetime
import os
from urllib import request
from datetime import time, datetime, timedelta
from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from datetime import time

from django.urls import reverse

from equipmentmanagementsystem.forms import AddAllocatorForm, EditAllocatorForm, AddEquipmentForm, EditEquipmentForm
from equipmentmanagementsystem.models import CustomUser, Category, Equipment, Room, AllocatorHOD, ManagerHOD
from equipmentmanagementsystem.forms import AddAllocationForm, AddEquipmentPlanningForm, EditAllocationForm, EditEquipmentPlanningForm
from equipmentmanagementsystem.models import EquipmentAllocation, EquipmentAllowedDays, EquipmentPlanning
import datetime
from urllib import request
from datetime import time, datetime, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import time
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from equipmentmanagementsystem.forms import AddAllocatorForm, EditAllocatorForm, AddEquipmentForm, EditEquipmentForm, AddEquipmentPlanningForm, EditEquipmentPlanningForm,AddAllocationForm, EditAllocationForm
from equipmentmanagementsystem.models import CustomUser, Category, Equipment, Room, AllocatorHOD, ManagerHOD, EquipmentPlanning, EquipmentAllowedDays, EquipmentAllocation
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import datetime
from django.db.models import Sum
from qrcode import QRCode

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from qrcode import make as qr_make
import io
import base64




def showManagerPage(request):
    equipments = Equipment.objects.all()
    equipment_count = equipments.count()

    students = AllocatorHOD.objects.filter(role='student')
    student_count = students.count()

    researchers = AllocatorHOD.objects.filter(role='researcher')
    researcher_count = researchers.count()

    allocations = EquipmentAllocation.objects.all()
    allocation_count = allocations.count()

    return render(request, 'managerhod_templates/home_content.html', {
        "equipment_count": equipment_count,
        "student_count": student_count,
        "researcher_count": researcher_count,
        "allocation_count": allocation_count
    })


def addAllocator(request):
    form = AddAllocatorForm()
    return render(request, 'managerhod_templates/add_allocator.html', {"form":form})


def saveAddAllocator(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        form = AddAllocatorForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phonenumber = form.cleaned_data['phonenumber']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            speciality = form.cleaned_data['speciality']
            faculty = form.cleaned_data['faculty']
            registrationnumber = form.cleaned_data['registrationnumber']
            role = form.cleaned_data['role']
            profilepicture = request.FILES['profilepicture']
            fss = FileSystemStorage()
            filename = fss.save(profilepicture.name, profilepicture)
            profilepictureurl = fss.url(filename)

            try:
                user = CustomUser.objects.create_user(username=username,
                                                      email=email, password=password, first_name=first_name,
                                                      last_name=last_name, user_type=3)
                user.allocatorhod.fullname = fullname
                user.allocatorhod.phonenumber = phonenumber
                user.allocatorhod.speciality = speciality
                user.allocatorhod.faculty = faculty
                user.allocatorhod.registrationnumber = registrationnumber
                user.allocatorhod.profilepicture = profilepictureurl
                user.allocatorhod.role = role
                user.save()
                messages.success(request, "Successfully Added")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_allocator"))
            except:
                messages.error(request, "Could Not Add ")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_allocator"))

        else:
            form = AddAllocatorForm(request.POST, request.FILES)
            return render(request, 'managerhod_templates/add_allocator.html', {"form":form})





def viewAllocator(request):
    selected_faculty = request.GET.get('faculty', '')
    selected_speciality = request.GET.get('speciality', '')
    
    students = AllocatorHOD.objects.filter(
        admin__user_type=3, 
        admin__allocatorhod__role='student',
        faculty__icontains=selected_faculty,
        speciality__icontains=selected_speciality,
    )
    
    researchers = AllocatorHOD.objects.filter(
        admin__user_type=3, 
        admin__allocatorhod__role='researcher',
        faculty__icontains=selected_faculty,
        speciality__icontains=selected_speciality,
    )
    
    faculties = AllocatorHOD.objects.order_by('faculty').values_list('faculty', flat=True).distinct()
    specialities = AllocatorHOD.objects.order_by('speciality').values_list('speciality', flat=True).distinct()
    
    return render(request, 'managerhod_templates/view_allocator.html', {
        "students": students, 
        "researchers": researchers,
        "selected_faculty": selected_faculty,
        "selected_speciality": selected_speciality,
        "faculties": faculties,
        "specialities": specialities,
    })

def editAllocator(request,allocator_id ):
    request.session['allocator_id']=allocator_id
    allocator = AllocatorHOD.objects.get(admin=allocator_id)
    form = EditAllocatorForm()
    form.fields['email'].initial=allocator.admin.email
    form.fields['phonenumber'].initial = allocator.phonenumber
    form.fields['username'].initial = allocator.admin.username
    form.fields['first_name'].initial = allocator.admin.first_name
    form.fields['last_name'].initial = allocator.admin.email
    form.fields['fullname'].initial = allocator.fullname
    form.fields['faculty'].initial = allocator.faculty
    form.fields['speciality'].initial = allocator.speciality
    form.fields['registrationnumber'].initial = allocator.registrationnumber
    form.fields['role'].initial = allocator.admin.allocatorhod.role
    form.fields['profilepicture'].initial = allocator.profilepicture
    return render(request, 'managerhod_templates/edit_allocator.html', {"form": form, "id":allocator_id})

def saveEditAllocator(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        allocator_id = request.session.get('allocator_id')
        if allocator_id == None:
            return HttpResponseRedirect("/view_allocator")
        form = EditAllocatorForm(request.POST, request.FILES)
        if form.is_valid():
            role = form.cleaned_data['role']
            fullname = form.cleaned_data['fullname']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phonenumber = form.cleaned_data['phonenumber']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            faculty = form.cleaned_data['faculty']
            speciality = form.cleaned_data['speciality']
            registrationnumber = form.cleaned_data['registrationnumber']
            

            if request.FILES.get('profilepicture', False):
                profilepicture = request.FILES['profilepicture']
                fss = FileSystemStorage()
                filename = fss.save(profilepicture.name, profilepicture)
                profilepictureurl = fss.url(filename)
            else:
                profilepictureurl = None

            try:

                user = CustomUser.objects.get(id=allocator_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()
                allocator_model = AllocatorHOD.objects.get(admin=allocator_id)
                allocator_model.fullname = fullname
                allocator_model.phonenumber = phonenumber
                allocator_model.faculty = faculty
                allocator_model.speciality = speciality
                allocator_model.registrationnumber = registrationnumber
                allocator_model.admin.allocatorhod.role = role

                if profilepictureurl != None:
                    allocator_model.profilepicture = profilepictureurl

                allocator_model.save()
                del request.session['allocator_id']
                messages.success(request, "Successfully Edited")
                return HttpResponseRedirect("/edit_allocator/" + allocator_id)
            except:
                messages.error(request, "Could Not Edit ")
                return HttpResponseRedirect("/edit_allocator/" + allocator_id)
        else:
            form = EditAllocatorForm(request.POST)
            return render(request, 'managerhod_templates/edit_allocator.html', {"form": form, "id": allocator_id})










def deleteAllocator(request, allocator_id):
    try:
        allocator_hod = AllocatorHOD.objects.get(admin=allocator_id)
        custom_user = CustomUser.objects.get(id=allocator_id)
    except (AllocatorHOD.DoesNotExist, CustomUser.DoesNotExist):
        return HttpResponseNotFound("Allocator not found")
    allocator_hod.delete()
    custom_user.delete()

    return HttpResponseRedirect("/view_allocator")



def addEquipment(request):
    form = AddEquipmentForm()
    return render(request, 'managerhod_templates/add_equipment.html', {"form":form})



# def saveAddEquipment(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         form = AddEquipmentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             type = form.cleaned_data['type']
#             brand = form.cleaned_data['brand']
#             model = form.cleaned_data['model']
#             serialnumber = form.cleaned_data['serialnumber']
#             totalnumber = form.cleaned_data['totalnumber']
#             category_id = form.cleaned_data['category']
#             room_id = form.cleaned_data['room']
#             code = form.cleaned_data['code']

#             existing_equipment = Equipment.objects.filter(name=name, type=type, 
#                               brand=brand, model=model, category_id=category_id, room_id=room_id, serialnumber=serialnumber).first()
                        
#             if existing_equipment:                
#                 existing_equipment.totalnumber += totalnumber
#                 existing_equipment.save()
#                 messages.success(request, "Quantity updated successfully") 
#                 return HttpResponseRedirect("/add_equipment")
#             else:
               
#                  try:
#                     equipment = Equipment(name=name, type=type,
#                                         brand=brand, model=model,
#                                         code=code, serialnumber=serialnumber,
#                                         totalnumber=totalnumber)
#                     category_obj = Category.objects.get(id=category_id)
#                     equipment.category_id=category_obj
#                     room_obj = Room.objects.get(id=room_id)
#                     equipment.room_id=room_obj
#                     equipment.save()
#                     messages.success(request, "Successfully Added")
#                     return HttpResponseRedirect("/add_equipment")
#                  except:
#                   messages.error(request, "Could Not Add ")
#                   return HttpResponseRedirect("/add_equipment")
#         else:
#             form = AddEquipmentForm(request.POST)
#             categories = Category.objects.all()  
#             rooms = Room.objects.all() 
#             return render(request, 'managerhod_templates/add_equipment.html', {"form": form, "categories": categories, "rooms": rooms})




def saveAddEquipment(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        form = AddEquipmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            serialnumber = form.cleaned_data['serialnumber']
            totalnumber = form.cleaned_data['totalnumber']
            category_id = form.cleaned_data['category']
            room_id = form.cleaned_data['room']
            code = form.cleaned_data['code']

            existing_equipment = Equipment.objects.filter(name=name, type=type, 
                              brand=brand, model=model, category_id=category_id, room_id=room_id, serialnumber=serialnumber).first()
                        
            if existing_equipment:                
                existing_equipment.totalnumber += totalnumber
                existing_equipment.save()
                messages.success(request, "Quantity updated successfully") 
                return HttpResponseRedirect("/add_equipment")
            else:
                try:
                    # Calculate the total capacity of all existing equipment in the room
                    existing_capacity = Equipment.objects.filter(room_id=room_id).aggregate(Sum('totalnumber'))['totalnumber__sum'] or 0
                    
                    # Get the capacity of the room
                    room_capacity = Room.objects.get(id=room_id).capacity

                    # Check if adding the new equipment would exceed the room capacity
                    if existing_capacity + totalnumber > room_capacity:
                        messages.error(request, "Could not add equipment. The room is already at full capacity.")
                        return HttpResponseRedirect("/add_equipment")

                    equipment = Equipment(name=name, type=type,
                                        brand=brand, model=model,
                                        code=code, serialnumber=serialnumber,
                                        totalnumber=totalnumber)
                    category_obj = Category.objects.get(id=category_id)
                    equipment.category_id=category_obj
                    room_obj = Room.objects.get(id=room_id)
                    equipment.room_id=room_obj
                    equipment.save()
                    messages.success(request, "Successfully Added")
                    return HttpResponseRedirect("/add_equipment")
                except:
                    messages.error(request, "Could Not Add ")
                    return HttpResponseRedirect("/add_equipment")
        else:
            form = AddEquipmentForm(request.POST)
            categories = Category.objects.all()  
            rooms = Room.objects.all() 
            return render(request, 'managerhod_templates/add_equipment.html', {"form": form, "categories": categories, "rooms": rooms})
        

def viewEquipment(request):
    category = request.GET.get('category')
    room = request.GET.get('room')

    equipments = Equipment.objects.all().order_by('-id')
    if category:
        equipments = equipments.filter(category_id__name__icontains=category)
    if room:
        equipments = equipments.filter(room_id__name__icontains=room)

    context = {
        'equipments': equipments,
        'categories': Category.objects.all(),
        'rooms': Room.objects.all(),
        'selected_category': category,
        'selected_room': room,
        'selected_type': type,

        
    }
    

    return render(request, 'managerhod_templates/view_equipment.html', context)





def editEquipment(request, equipment_id):
    request.session['equipment_id'] = equipment_id
    equipment = Equipment.objects.get(id=equipment_id)
    form = EditEquipmentForm()
    form.fields['name'].initial = equipment.name
    form.fields['serialnumber'].initial = equipment.serialnumber
    form.fields['type'].initial = equipment.type
    form.fields['brand'].initial = equipment.brand
    form.fields['model'].initial = equipment.model
    form.fields['code'].initial = equipment.code
    form.fields['totalnumber'].initial = equipment.totalnumber
    form.fields['category'].initial = equipment.category_id.id
    form.fields['room'].initial = equipment.room_id.id

    return render(request, 'managerhod_templates/edit_equipment.html', {"form": form, "id": equipment_id})


def saveEditEquipment(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        equipment_id = request.session.get('equipment_id')
        if equipment_id is None:
            return HttpResponseRedirect("/view_equipment")
        form = EditEquipmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            code = form.cleaned_data['code']
            serialnumber = form.cleaned_data['serialnumber']
            totalnumber = form.cleaned_data['totalnumber']
            category_id = form.cleaned_data['category']
            room_id = form.cleaned_data['room']

            try:
                room = Room.objects.get(id=room_id)
                existing_capacity = Equipment.objects.filter(room_id=room_id).exclude(id=equipment_id).aggregate(Sum('totalnumber'))['totalnumber__sum'] or 0
                if existing_capacity + totalnumber > room.capacity:
                    messages.error(request, "Could not edit equipment. The room will be at full capacity.")
                    return HttpResponseRedirect("/edit_equipment/" + equipment_id)

                equipment_model = Equipment.objects.get(id=equipment_id)
                existing_equipment = Equipment.objects.filter(name=name, type=type, brand=brand, model=model, category_id=category_id, room_id=room_id, serialnumber=serialnumber).exclude(id=equipment_id).first()

                if existing_equipment:
                    existing_equipment.totalnumber += totalnumber
                    existing_equipment.save()
                    equipment_model.delete()
                    messages.success(request, "Quantity updated successfully")
                else:
                    equipment_model.name = name
                    equipment_model.type = type
                    equipment_model.brand = brand
                    equipment_model.model = model
                    equipment_model.code = code
                    equipment_model.serialnumber = serialnumber
                    equipment_model.totalnumber = totalnumber

                    category = Category.objects.get(id=category_id)
                    equipment_model.category_id = category

                    room = Room.objects.get(id=room_id)
                    equipment_model.room_id = room

                    equipment_model.save()
                    messages.success(request, "Successfully Edited")
                del request.session['equipment_id']
                return HttpResponseRedirect("/edit_equipment/" + equipment_id)
            except:
                messages.error(request, "Could Not Edit ")
                return HttpResponseRedirect("/edit_equipment/" + equipment_id)
        else:
            form = EditAllocatorForm(request.POST)
            return render(request, 'managerhod_templates/edit_equipment.html', {"form": form, "id": equipment_id})
        



def deleteEquipment(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    equipment.delete()
    return HttpResponseRedirect("/view_equipment")





def manager_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    manager = ManagerHOD.objects.get(admin=user)
    return render(request, "managerhod_templates/manager_profile.html", {"user": user, "manager": manager})


def manager_profile_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("manager_profile"))
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        fullname = request.POST.get("fullname")
        phonenumber = request.POST.get("phonenumber")
        password_changed = False

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.email = email
            if password is not None and password != "":
                customuser.set_password(password)
                password_changed = True
            customuser.save()

            manager = ManagerHOD.objects.get(admin=customuser.id)
            manager.fullname = fullname
            manager.phonenumber = phonenumber
            manager.save()

            if password_changed:
                messages.success(request, "Successfully Updated password !")
                return redirect('equipmentmanagementsystem:show_login')
            else:
                messages.success(request, "Successfully Updated Profile !")
                return redirect('equipmentmanagementsystem:manager_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('equipmentmanagementsystem:manager_profile !')
        

# def add_equipment_planning(request):
#     if request.method == 'POST':
#         form = AddEquipmentPlanningForm(request.POST)
#         if form.is_valid():
#             equipment_id = form.cleaned_data['equipment']
#             day = form.cleaned_data['day']
#             start_time = form.cleaned_data['start_time']
#             end_time = form.cleaned_data['end_time']
#             allowed_days = [day]  # Récupérer les jours autorisés du formulaire

#             if end_time <= start_time:
#                 # Invalid time range, display an error message
#                 form.add_error('end_time', 'End time must be greater than start time.')
#             else:
#                 equipment = Equipment.objects.get(id=equipment_id)

#                 # Vérifier l'existence d'autres plannings pour le même équipement et le même jour
#                 existing_planning = EquipmentPlanning.objects.filter(equipment=equipment, day=day).exists()
#                 if existing_planning:
#                     # Il existe déjà un planning pour cet équipement et ce jour, vérifier le temps
#                     conflicting_planning = EquipmentPlanning.objects.filter(
#                         equipment=equipment, day=day, start_time__lte=end_time, end_time__gte=start_time
#                     ).exists()
#                     if conflicting_planning:
#                         # Conflit de temps, afficher un message d'erreur
#                         form.add_error(None, 'There is a time conflict with an existing equipment planning.')
#                     else:
#                         # Pas de conflit de temps, enregistrer le nouveau planning
#                         manager = get_object_or_404(ManagerHOD, admin=request.user)
#                         equipment_planning = EquipmentPlanning(
#                             equipment=equipment,
#                             day=day,
#                             start_time=start_time,
#                             end_time=end_time,
#                             manager=manager
#                         )
#                         equipment_planning.save()

#                         # Enregistrer les jours autorisés pour l'équipement planifié
#                         for allowed_day in allowed_days:
#                             EquipmentAllowedDays.objects.create(
#                                 equipment=equipment,
#                                 equipment_planning=equipment_planning,
#                                 allowed_day=allowed_day
#                             )

#                         return redirect('equipmentmanagementsystem:view_equipment_planning')
#                 else:
#                     # Aucun planning existant, enregistrer le nouveau planning
#                     manager = get_object_or_404(ManagerHOD, admin=request.user)
#                     equipment_planning = EquipmentPlanning(
#                         equipment=equipment,
#                         day=day,
#                         start_time=start_time,
#                         end_time=end_time,
#                         manager=manager
#                     )
#                     equipment_planning.save()

#                     # Enregistrer les jours autorisés pour l'équipement planifié
#                     for allowed_day in allowed_days:
#                         EquipmentAllowedDays.objects.create(
#                             equipment=equipment,
#                             equipment_planning=equipment_planning,
#                             allowed_day=allowed_day
#                         )

#                     return redirect('equipmentmanagementsystem:view_equipment_planning')
#     else:
#         form = AddEquipmentPlanningForm()

#     context = {'form': form}
#     return render(request, 'managerhod_templates/add_equipment_planning.html', context)


from django.contrib import messages

def add_equipment_planning(request):
    if request.method == 'POST':
        form = AddEquipmentPlanningForm(request.POST)
        if form.is_valid():
            equipment_id = form.cleaned_data['equipment']
            day = form.cleaned_data['day']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            allowed_days = [day]  # Récupérer les jours autorisés du formulaire

            if end_time <= start_time:
                # Invalid time range, display an error message
                messages.error(request, 'End datetime must be greater than start time.')
            else:
                equipment = Equipment.objects.get(id=equipment_id)

                # Vérifier l'existence d'autres plannings pour le même équipement et le même jour
                existing_planning = EquipmentPlanning.objects.filter(equipment=equipment, day=day).exists()
                if existing_planning:
                    # Il existe déjà un planning pour cet équipement et ce jour, vérifier le temps
                    conflicting_planning = EquipmentPlanning.objects.filter(
                        equipment=equipment, day=day, start_time__lte=end_time, end_time__gte=start_time
                    ).exists()
                    if conflicting_planning:
                        # Conflit de temps, afficher un message d'erreur
                        messages.error(request, 'There is a time conflict with an existing equipment planning.')
                    else:
                        # Pas de conflit de temps, enregistrer le nouveau planning
                        manager = get_object_or_404(ManagerHOD, admin=request.user)
                        equipment_planning = EquipmentPlanning(
                            equipment=equipment,
                            day=day,
                            start_time=start_time,
                            end_time=end_time,
                            manager=manager
                        )
                        equipment_planning.save()

                        # Enregistrer les jours autorisés pour l'équipement planifié
                        for allowed_day in allowed_days:
                            EquipmentAllowedDays.objects.create(
                                equipment=equipment,
                                equipment_planning=equipment_planning,
                                allowed_day=allowed_day
                            )

                        messages.success(request, 'Equipment planning added successfully !')
                        return redirect('equipmentmanagementsystem:view_equipment_planning')
                else:
                    # Aucun planning existant, enregistrer le nouveau planning
                    manager = get_object_or_404(ManagerHOD, admin=request.user)
                    equipment_planning = EquipmentPlanning(
                        equipment=equipment,
                        day=day,
                        start_time=start_time,
                        end_time=end_time,
                        manager=manager
                    )
                    equipment_planning.save()

                    # Enregistrer les jours autorisés pour l'équipement planifié
                    for allowed_day in allowed_days:
                        EquipmentAllowedDays.objects.create(
                            equipment=equipment,
                            equipment_planning=equipment_planning,
                            allowed_day=allowed_day
                        )

                    messages.success(request, 'Equipment planning added successfully !') 
                    return redirect('equipmentmanagementsystem:view_equipment_planning')
                
    else:
        form = AddEquipmentPlanningForm()

    context = {'form': form}
    return render(request, 'managerhod_templates/add_equipment_planning.html', context)

def view_equipment_planning(request):
    equipments = Equipment.objects.all()
    equipment_plannings = EquipmentPlanning.objects.all()
    context = {'equipments': equipments, 'equipment_plannings': equipment_plannings}
    return render(request, 'managerhod_templates/view_equipment_planning.html', context)

    

def viewEquipmentPlanning(request):
    equipment_plannings = EquipmentPlanning.objects.all()
    context = {'equipment_plannings': equipment_plannings}
    return render(request, 'managerhod_templates/view_equipment_planning.html', context)   

def editEquipmentPlanning(request, equipment_planning_id):
    request.session['equipment_planning_id'] = equipment_planning_id
    equipment_planning = EquipmentPlanning.objects.get(id=equipment_planning_id)
    form = EditEquipmentPlanningForm()
    form.fields['equipment'].initial = equipment_planning.equipment.id
    form.fields['day'].initial = equipment_planning.day
    form.fields['start_time'].initial = equipment_planning.start_time
    form.fields['end_time'].initial = equipment_planning.end_time
    

    return render(request, 'managerhod_templates/edit_equipment_planning.html', {"form": form, "id": equipment_planning_id})


def saveEditEquipmentPlanning(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        equipment_planning_id = request.session.get('equipment_planning_id')
        if equipment_planning_id is None:
            return HttpResponseRedirect("/view_equipment_planning")
        form = EditEquipmentPlanningForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            
            if end_time <= start_time:
                # Invalid time range, display an error message
                messages.error(request, 'End datetime must be greater than start time.')
                return render(request, 'managerhod_templates/edit_equipment_planning.html', {"form": form, "id": equipment_planning_id})

            try:
                equipment_planning_model = EquipmentPlanning.objects.get(id=equipment_planning_id)
                equipment = equipment_planning_model.equipment
                # Vérifier l'existence d'autres plannings pour le même équipement et le même jour
                existing_planning = EquipmentPlanning.objects.filter(equipment=equipment, day=day).exclude(id=equipment_planning_id).exists()
                if existing_planning:
                    # Il existe déjà un planning pour cet équipement et ce jour, vérifier le temps
                    conflicting_planning = EquipmentPlanning.objects.filter(
                        equipment=equipment, day=day, start_time__lte=end_time, end_time__gte=start_time
                    ).exclude(id=equipment_planning_id).exists()
                    if conflicting_planning:
                        # Conflit de temps, afficher un message d'erreur
                        messages.error(request, 'There is a time conflict with an existing equipment planning. ')
                        return render(request, 'managerhod_templates/edit_equipment_planning.html', {"form": form, "id": equipment_planning_id})

                equipment_planning_model.day = day
                equipment_planning_model.start_time = start_time
                equipment_planning_model.end_time = end_time
                equipment_planning_model.save()

                del request.session['equipment_planning_id']
                messages.success(request, "Successfully edited")
                return HttpResponseRedirect("/edit_equipment_planning/" + equipment_planning_id)
            except EquipmentPlanning.DoesNotExist:
                messages.error(request, "Could not find the equipment planning")
                return HttpResponseRedirect("/edit_equipment_planning/" + equipment_planning_id)
        else:
            return render(request, 'managerhod_templates/edit_equipment_planning.html', {"form": form, "id": equipment_planning_id})




def deleteEquipmentPlanning(request, equipment_planning_id):
    equipment_planning = EquipmentPlanning.objects.get(id=equipment_planning_id)
    equipment_planning.delete()
    return HttpResponseRedirect("/view_equipment_planning") 




def viewAllocation(request):
    equipment_allocations = EquipmentAllocation.objects.all()
    context = {'equipment_allocations': equipment_allocations}
    return render(request, 'managerhod_templates/view_allocations.html', context)  

   
def send_allocation_notification_from_manager(allocation):
    subject = 'New Allocation'
    message = f'You have been allocated equipment {allocation.equipment.name} from {allocation.start_datetime} to {allocation.end_datetime} Succesfuly, Thanks.'
    from_email = 'equipifysystem@gmail.com'  # Adresse e-mail de l'expéditeur
    to_email = allocation.allocator.admin.email  # Adresse e-mail du destinataire

    send_mail(subject, message, from_email, [to_email])


def addAllocation(request):
    if request.method == 'POST':
        form = AddAllocationForm(request.POST)
        if form.is_valid():
            equipment_id = form.cleaned_data['equipment']
            allocator_id = form.cleaned_data['allocator']
            start_datetime = form.cleaned_data['start_datetime']
            end_datetime = form.cleaned_data['end_datetime']

            if end_datetime <= start_datetime:
                # Invalid time range, display an error message
                messages.error(request, 'End datetime must be greater than start time.')
            else:
                equipment = Equipment.objects.get(id=equipment_id)
                allocator = AllocatorHOD.objects.get(id=allocator_id)
                day_of_week = start_datetime.strftime('%A').lower()  # Récupérer le jour de la semaine de la date choisie

                # Vérifier si le jour de la semaine est autorisé par le manager
                allowed_days = EquipmentAllowedDays.objects.filter(
                    equipment=equipment,
                    allowed_day=day_of_week
                )

                if not allowed_days:
                    # Le jour sélectionné n'est pas autorisé pour l'équipement, afficher un message d'erreur
                    messages.error(request, 'This day is not allowed for equipment allocation.')
                else:
                    # Vérifier la disponibilité de l'équipement et la non-réservation par un autre allocataire
                    existing_allocation = EquipmentAllocation.objects.filter(
                        equipment=equipment,
                        start_datetime__lt=end_datetime,
                        end_datetime__gt=start_datetime
                    ).exists()

                    if existing_allocation:
                        # Il existe déjà une allocation pour cet équipement et ce créneau, afficher un message d'erreur
                        messages.error(request, 'This equipment is already allocated for the selected time range.')
                    else:
                        # Récupérer l'instance AllocatorHOD correspondant à l'utilisateur
                        # allocator = get_object_or_404(AllocatorHOD, admin=request.user)
                        # manager = get_object_or_404(ManagerHOD, admin=request.user)
                        # Créer l'allocation
                        manager = get_object_or_404(ManagerHOD, admin=request.user)
                        allocation = EquipmentAllocation(
                            equipment=equipment,
                            allocator=allocator,
                            start_datetime=start_datetime,
                            end_datetime=end_datetime,
                            manager=manager
                        )
                        allocation.save()
                        send_allocation_notification_from_manager(allocation)
                        # Rediriger vers une page de confirmation ou une autre vue appropriée
                        return redirect('equipmentmanagementsystem:view_allocations')
    else:
        form = AddAllocationForm()

    context = {'form': form}
    return render(request, 'managerhod_templates/add_allocation.html', context)    



def editAllocation(request, equipment_allocation_id):
    request.session['equipment_allocation_id'] = equipment_allocation_id
    equipment_allocation = EquipmentAllocation.objects.get(id=equipment_allocation_id)
    form = EditAllocationForm()
    form.fields['allocator'].initial = equipment_allocation.allocator.id
    form.fields['equipment'].initial = equipment_allocation.equipment.id
    form.fields['start_datetime'].initial = equipment_allocation.start_datetime
    form.fields['end_datetime'].initial = equipment_allocation.end_datetime
    

    return render(request, 'managerhod_templates/edit_allocation.html', {"form": form, "id": equipment_allocation_id})  

def saveEditEquipmentAllocation(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        equipment_allocation_id = request.session.get('equipment_allocation_id')
        if equipment_allocation_id is None:
            return HttpResponseRedirect("/view_allocation")
        form = EditAllocationForm(request.POST)
        if form.is_valid():
            start_datetime = form.cleaned_data['start_datetime']
            end_datetime = form.cleaned_data['end_datetime']
            
            if end_datetime <= start_datetime:
                # Invalid time range, display an error message
                messages.error(request, 'End datetime must be greater than start time.')
                return render(request, 'managerhod_templates/edit_allocation.html', {"form": form, "id": equipment_allocation_id})

            try:
                equipment_allocation_model = EquipmentAllocation.objects.get(id=equipment_allocation_id)
                equipment = equipment_allocation_model.equipment
                # Vérifier l'existence d'autres plannings pour le même équipement et le même jour
                existing_allocation = EquipmentAllocation.objects.filter(equipment=equipment, start_datetime=start_datetime, end_datetime=end_datetime).exists()
                if existing_allocation:
                    # Il existe déjà un planning pour cet équipement et ce jour, vérifier le temps
                    conflicting_allocation = EquipmentAllocation.objects.filter(
                      equipment=equipment, start_datetime__lte=end_datetime, end_datetime__gte=start_datetime
                    ).exists()
                    if conflicting_allocation:
                        # Conflit de temps, afficher un message d'erreur
                        messages.error(request, 'There is a time conflict with an existing equipment allocation !')
                        return render(request, 'managerhod_templates/edit_allocation.html', {"form": form, "id": equipment_allocation_id})

                equipment_allocation_model.equipment = equipment
                equipment_allocation_model.start_datetime = start_datetime
                equipment_allocation_model.end_datetime = end_datetime
                equipment_allocation_model.save()

                del request.session['equipment_allocation_id']
                messages.success(request, "Successfully edited")
                return HttpResponseRedirect("/edit_equipment_allocation/" + equipment_allocation_id)
            except EquipmentAllocation.DoesNotExist:
                messages.error(request, "Could not find the equipment allocation")
                return HttpResponseRedirect("/edit_equipment_allocation/" + equipment_allocation_id)
        else:
            return render(request, 'managerhod_templates/edit_allocation.html', {"form": form, "id": equipment_allocation_id})    


def deleteAllocation(request, equipment_allocation_id):
    equipment_allocation = EquipmentAllocation.objects.get(id=equipment_allocation_id)
    equipment_allocation.delete()
    return HttpResponseRedirect("/view_allocations")     


import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import EquipmentPlanning
from django.core.files.storage import FileSystemStorage
from reportlab.pdfgen import canvas
from django.http import FileResponse
import pandas as pd
from openpyxl import Workbook
import PyPDF2
import xlwt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings
from django.template.loader import get_template
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib import colors


# def exportEquipmentPlanning(request):
#     if request.method == 'POST':
#         file_format = request.POST.get('format')
#         equipment_plannings = EquipmentPlanning.objects.all()  
        
#         if file_format == 'csv':
#             # Generate CSV file
#             response = HttpResponse(content_type='text/csv')
#             filename = 'equipment_planning.csv'  # Default file name
#             filepath = os.path.join('exports', filename)  # Default file path
            
#             # Get custom file name from request
#             custom_filename = request.POST.get('filename')
#             if custom_filename:
#                 filename = f'{custom_filename}.csv'
#                 filepath = os.path.join('exports', filename)
            
#             response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
#             writer = csv.writer(response)
#             writer.writerow(['Id','Equipment', 'Start Time', 'End Time', 'Assigned To'])
#             for equipment_planning in equipment_plannings:
#                 writer.writerow([equipment_planning.id, equipment_planning.equipment.name, equipment_planning.start_time, equipment_planning.end_time, equipment_planning.assigned_to.username])
            
#             return response
        
#     equipment_plannings = EquipmentPlanning.objects.all()
#     context = {'equipment_plannings': equipment_plannings}
#     return render(request, 'managerhod_templates/view_equipment_planning.html', context)




# import xlwt

# import csv
# import os
# from io import BytesIO
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.template.loader import get_template
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import landscape, letter
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# import xlwt


from urllib import request
from django import template
from django.template.loader import render_to_string
from datetime import datetime, date
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
import os
import csv
from jinja2 import Environment, FileSystemLoader
from equipmentmanagementsystem.forms import AddManagerForm, EditManagerForm, AddCategoryForm, EditCategoryForm, AddRoomForm, EditRoomForm
from equipmentmanagementsystem.models import CustomUser, Category, ManagerHOD , AllocatorHOD, Equipment, Room,  AdminHOD
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from reportlab.pdfgen import canvas
from django.http import FileResponse
import pandas as pd
from openpyxl import Workbook
import PyPDF2
import xlwt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings
from django.template.loader import get_template
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, TableStyle
from reportlab.platypus.tables import Table
from reportlab.lib.styles import getSampleStyleSheet



def exportEquipmentPlanning(request):
    if request.method == 'POST':
        file_format = request.POST.get('format')
        equipment_plannings = EquipmentPlanning.objects.all()  
    
        if file_format == 'csv':
            # Générer le fichier CSV
            response = HttpResponse(content_type='text/csv')
            filename = 'equipment_planning.csv'  # Nom de fichier par défaut
            filepath = os.path.join('plannings', filename)  # Emplacement par défaut
            
            # Récupérer le nom de fichier personnalisé depuis la requête
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.csv'
                filepath = os.path.join('plannings', filename)
            
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            writer = csv.writer(response)
            writer.writerow(['Equipment', 'Day', 'Start Time', 'End Time' ])
            for equipment_planning in equipment_plannings:
                writer.writerow([equipment_planning.equipment.name, equipment_planning.day, equipment_planning.start_time, equipment_planning.end_time])
            
            return response
        
        elif file_format == 'pdf':
            # Generate PDF file
            filename = 'equipment_planning.pdf'  # Default file name
            
            # Get custom file name from request
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.pdf'
            
            filepath = os.path.join('plannings', filename)  # Default file path
            
            # Create data for table
            data = [['Equipment', 'Day', 'Start Time', 'End Time']]
            for equipment_planning in equipment_plannings:
                data.append([
                    equipment_planning.equipment.name,
                    equipment_planning.get_day_display(),
                    equipment_planning.start_time.strftime('%H:%M'),
                    equipment_planning.end_time.strftime('%H:%M'),
                ])
            
            # Create PDF document
            doc = SimpleDocTemplate(filepath, pagesize=landscape(letter))
            styles = getSampleStyleSheet()
            table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.black),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('LEFTPADDING', (0, 1), (-1, -1), 10),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ('LINEBEFORE', (0, 0), (-1, -1), 1, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 1, colors.black),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    
])
            
  # Créer le tableau
            table = Table(data)
            table.setStyle(table_style)

            

            # Add the table and a PageBreak flowable to the elements list
            elements = [table, PageBreak()]
            
            # Construire le document PDF
            elements = [table]
            doc.build(elements)
            
            # Renvoyer le fichier en tant que réponse HTTP
            with open(filepath, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            return response
        
        elif file_format == 'xls':
            # Récupérer le nom de fichier personnalisé depuis la requête
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.xls'
            else:
                filename = 'equipment_planning.xls'  # Nom de fichier par défaut
            
            filepath = os.path.join('plannings', filename)  # Emplacement par défaut
            
            # Code pour générer le fichier XLS en utilisant la bibliothèque xlwt
            wb = xlwt.Workbook()
            sheet = wb.add_sheet('equipment_planning')
            sheet.write(0, 0, 'Equipment')
            sheet.write(0, 1, 'Day')
            sheet.write(0, 2, 'Start Time')
            sheet.write(0, 3, 'End Time')
            row = 1
            for equipment_planning in equipment_plannings:
                sheet.write(row, 0, equipment_planning.equipment.name)
                sheet.write(row, 1, equipment_planning.get_day_display())
                sheet.write(row, 2, equipment_planning.start_time.strftime('%H:%M'))
                sheet.write(row, 3, equipment_planning.end_time.strftime('%H:%M'))
                row += 1

            wb.save(filepath)
            
            with open(filepath, 'rb') as xls_file:
                response = HttpResponse(xls_file.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            return response
    
    return render(request, 'template.html', {'equipment_plannings': equipment_plannings, 'template_content': template.render({'equipment_plannings': equipment_plannings})})  




def viewResearchers(request):
    researcher = AllocatorHOD.objects.filter(role='researcher')
    return render(request, 'managerhod_templates/view_researchers.html', {"researchers": researcher}) 


def viewStudents(request):
    student = AllocatorHOD.objects.filter(role='student')
    return render(request, 'managerhod_templates/view_students.html', {"students": student}) 

def viewEquipments(request):
    equipment = Equipment.objects.all()
    return render(request, 'managerhod_templates/view_equipments.html', {"equipments": equipment})    

def viewAllocations(request):
    equipment_allocations = EquipmentAllocation.objects.all()
    context = {'equipment_allocations': equipment_allocations}
    return render(request, 'managerhod_templates/view_allocation.html', context) 




def exportEquipment(request):
    if request.method == 'POST':
        file_format = request.POST.get('format')
        equipments = Equipment.objects.all()

        if file_format == 'csv':
            # Generate CSV file
            response = HttpResponse(content_type='text/csv')
            filename = 'equipment.csv'  # Default filename
            filepath = os.path.join('equipments', filename)  # Default filepath

            # Get custom filename from request
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.csv'
                filepath = os.path.join('equipments', filename)

            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            writer = csv.writer(response)
            writer.writerow(['Id', 'Serialnumber', 'Code', 'Type', 'Brand', 'Model', 'TotalNumber', 'Category', 'Room'])
            for equipment in equipments:
                writer.writerow([equipment.id, equipment.serialnumber, equipment.code, equipment.type, equipment.brand,
                                 equipment.model, equipment.totalnumber, equipment.category_id.name, equipment.room_id.name])

            return response

        elif file_format == 'pdf':
            # Get custom filename from request
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.pdf'
            else:
                filename = 'equipment.pdf'  # Default filename

            filepath = os.path.join('equipments', filename)  # Default filepath

            # Create data for table
            data = [['Id', 'Serialnumber', 'Code', 'Type', 'Brand', 'Model', 'TotalNumber', 'Category', 'Room']]
            for equipment in equipments:
                data.append([equipment.id, equipment.serialnumber, equipment.code, equipment.type, equipment.brand,
                             equipment.model, equipment.totalnumber, equipment.category_id.name, equipment.room_id.name])

            # Create the document PDF
            doc = SimpleDocTemplate(filepath, pagesize=landscape(letter))

            # Set styles for table
            styles = getSampleStyleSheet()
            style_title = styles["Heading1"]
            table_style = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.black),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('LEFTPADDING', (0, 1), (-1, -1), 10),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
                    ('LINEBEFORE', (0, 0), (-1, -1), 1, colors.black),
                    ('LINEAFTER', (0, 0), (-1, -1), 1, colors.black),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])

            # Create the table
            table = Table(data)
            table.setStyle(table_style)

            

            # Add the table and a PageBreak flowable to the elements list
            elements = [table, PageBreak()]
            
            # Construire le document PDF
            elements = [table]
            doc.build(elements)

            # Return the file as an HTTP response
            with open(filepath, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'

            return response

        elif file_format == 'xls':
            # Get custom filename from request
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.xls'
            else:
                filename = 'equipment.xls'  # Default filename

            filepath = os.path.join('equipments', filename)  # Default filepath

            # Generate XLS file using xlwt library
            wb = xlwt.Workbook()
            sheet = wb.add_sheet('equipment_list')
            sheet.write(0, 0, 'Id')
            sheet.write(0, 1, 'Serialnumber')
            sheet.write(0, 2, 'Code')
            sheet.write(0, 3, 'Type')
            sheet.write(0, 4, 'Brand')
            sheet.write(0, 5, 'Model')
            sheet.write(0, 6, 'TotalNumber')
            sheet.write(0, 7, 'Category')
            sheet.write(0, 8, 'Room')
            row = 1
            for equipment in equipments:
                sheet.write(row, 0, equipment.id)
                sheet.write(row, 1, equipment.serialnumber)
                sheet.write(row, 2, equipment.code)
                sheet.write(row, 3, equipment.type)
                sheet.write(row, 4, equipment.brand)
                sheet.write(row, 5, equipment.model)
                sheet.write(row, 6, equipment.totalnumber)
                sheet.write(row, 7, equipment.category_id.name)
                sheet.write(row, 8, equipment.room_id.name)
                row += 1

            wb.save(filepath)

            # Return the file as an HTTP response
            with open(filepath, 'rb') as xls_file:
                response = HttpResponse(xls_file.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'

            return response
       
    return render(request, 'template.html', {'equipments': equipments, 'template_content': template.render({'equipments': equipments})})   






def generate_qr_code(request, equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    qr_data = f"{equipment.code} {equipment.room_id.name} {equipment.totalnumber}"
    
    qr_img = qr_make(qr_data)
    
    buffer = io.BytesIO()
    qr_img.save(buffer, format='PNG')
    buffer.seek(0)
    
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    qr_code_url = f"data:image/png;base64,{qr_code_base64}"
    
    context = {
        'equipment': equipment,
        'qr_code_url': qr_code_url
    }
    return render(request, 'qr_code.html', context)

















