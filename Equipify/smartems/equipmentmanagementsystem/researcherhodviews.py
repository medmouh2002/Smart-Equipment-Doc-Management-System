from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from equipmentmanagementsystem.models import AllocatorHOD, CustomUser


from equipmentmanagementsystem.forms import EquipmentAllocationForm
from equipmentmanagementsystem.models import Equipment, EquipmentAllocation, AllocatorHOD, EquipmentAllowedDays
from django.shortcuts import render, redirect
from datetime import datetime 
from django.db.models import Q

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse

from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render
from itertools import groupby
from .models import EquipmentAllocation, EquipmentPlanning
import datetime
import time
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




# def showResearcherPage(request):
#     return render(request, 'allocatorhod_templates/researcher_home_content.html')  

def showResearcherPage(request):
    equipment_plannings = EquipmentPlanning.objects.all()
    context = {'equipment_plannings': equipment_plannings}
    return render(request, 'allocatorhod_templates/researcher_home_content.html', context)      

def researcher_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    researcher = AllocatorHOD.objects.get(admin=user, role='researcher')
    return render(request, "allocatorhod_templates/researcher_profile.html", {"user": user, "researcher": researcher})

def researcher_profile_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("researcher_profile"))
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
                customuser.save()
                password_changed = True

            researcher = AllocatorHOD.objects.get(admin=customuser.id, role='researcher')
            researcher.fullname = fullname
            researcher.phonenumber = phonenumber
            researcher.save()

            if password_changed:
                messages.success(request, "Successfully Updated password !")
                return redirect('equipmentmanagementsystem:show_login')
            
            else:
                messages.success(request, "Successfully Updated Profile !")
                return redirect('equipmentmanagementsystem:researcher_profile')
        except:
            messages.error(request, "Failed to Update Profile !")
            return redirect('equipmentmanagementsystem:researcher_profile')
        

        




# def allocate_equipment_researcher(request):
#     if request.method == 'POST':
#         form = EquipmentAllocationForm(request.POST)
#         if form.is_valid():
#             equipment_id = form.cleaned_data['equipment']
#             start_datetime = form.cleaned_data['start_datetime']
#             end_datetime = form.cleaned_data['end_datetime']

#             if end_datetime <= start_datetime:
#                 # Invalid time range, display an error message
#                 form.add_error('end_datetime', 'End datetime must be greater than start time.')
#             else:
#                 equipment = Equipment.objects.get(id=equipment_id)
#                 day_of_week = start_datetime.strftime('%A').lower()  # Récupérer le jour de la semaine de la date choisie

#                 # Vérifier si le jour de la semaine est autorisé par le manager
#                 allowed_days = EquipmentAllowedDays.objects.filter(
#                     equipment=equipment,
#                     allowed_day=day_of_week
#                 )

#                 if not allowed_days:
#                     # Le jour sélectionné n'est pas autorisé pour l'équipement, afficher un message d'erreur
#                     form.add_error('start_datetime', 'This day is not allowed for equipment allocation.')
#                 else:
#                     # Vérifier la disponibilité de l'équipement et la non-réservation par un autre allocataire
#                     existing_allocation = EquipmentAllocation.objects.filter(
#                         equipment=equipment,
#                         start_datetime__lt=end_datetime,
#                         end_datetime__gt=start_datetime
#                     ).exists()

#                     if existing_allocation:
#                         # Il existe déjà une allocation pour cet équipement et ce créneau, afficher un message d'erreur
#                         form.add_error(None, 'This equipment is already allocated for the selected time range.')
#                     else:
#                         # Récupérer l'instance AllocatorHOD correspondant à l'utilisateur connecté
#                         allocator = get_object_or_404(AllocatorHOD, admin=request.user)
                        
                        
#                         # Créer l'allocation
#                         allocation = EquipmentAllocation(
#                             equipment=equipment,
#                             allocator=allocator,
#                             start_datetime=start_datetime,
#                             end_datetime=end_datetime
#                         )
#                         allocation.save()
#                         send_allocation_notification(allocation)
#                         return redirect('equipmentmanagementsystem:view_equipment_allocation')
#     else:
#         form = EquipmentAllocationForm()

#     context = {'form': form}
#     return render(request, 'allocatorhod_templates/researcher_allocate_equipment.html', context)





from datetime import time

def allocate_equipment_researcher(request):
    if request.method == 'POST':
        form = EquipmentAllocationForm(request.POST)
        if form.is_valid():
            equipment_id = form.cleaned_data['equipment']
            start_datetime = form.cleaned_data['start_datetime']
            end_datetime = form.cleaned_data['end_datetime']

            if end_datetime <= start_datetime:
                # Invalid time range, display an error message
                messages.error(request, 'End datetime must be greater than start time.')
            elif start_datetime.date() < datetime.today().date():
                # Start datetime is earlier than the current date, display an error messageS
                messages.error(request, 'Cannot allocate equipment for a date earlier than today.')
            else:
                equipment = Equipment.objects.get(id=equipment_id)
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
                        # Récupérer l'instance AllocatorHOD correspondant à l'utilisateur connecté
                        allocator = get_object_or_404(AllocatorHOD, admin=request.user)

                        if start_datetime.time() < time(8, 0) or start_datetime.time() > time(16, 0):
                            # La plage horaire sélectionnée est en dehors de l'heure autorisée, afficher un message d'erreur
                            messages.error(request, 'Equipment allocation is only allowed between 8am and 4pm.')
                        else:
                            # Créer l'allocation
                            allocation = EquipmentAllocation(
                                equipment=equipment,
                                allocator=allocator,
                                start_datetime=start_datetime,
                                end_datetime=end_datetime
                            )
                            allocation.save()
                            send_allocation_notification(allocation)
                            return redirect('equipmentmanagementsystem:view_researcher_equipment_allocation')
    else:
        form = EquipmentAllocationForm()
        form.fields['equipment'].choices = [(equipment.id, equipment.name) for equipment in Equipment.objects.filter(equipment_plannings__isnull=False)]

    context = {'form': form}
    return render(request, 'allocatorhod_templates/researcher_allocate_equipment.html', context)






def viewResearcherEquipmentAllocation(request):
    equipment_allocations = EquipmentAllocation.objects.all()
    context = {'equipment_allocations': equipment_allocations}
    return render(request, 'allocatorhod_templates/view_researcher_equipment_allocation.html', context)     


def send_allocation_notification(allocation):
    subject = 'New Allocation'
    message = f'Dear allocator you have been allocated equipment {allocation.equipment.name} from {allocation.start_datetime} to {allocation.end_datetime} Succesfuly.'
    from_email = 'equipifysystem@gmail.com'  # Adresse e-mail de l'expéditeur
    to_email_allocator = allocation.allocator.admin.email
    

    send_mail(subject, message, from_email, [to_email_allocator])        




my_time_choices = EquipmentPlanning.TIME_CHOICES

def viewResearchertHPCscheduling(request):
    equipment_allocations = EquipmentAllocation.objects.all().order_by('start_datetime', 'equipment__name')
    equipment_names = set(allocation.equipment.name for allocation in equipment_allocations)
    
    start_times = set(allocation.start_datetime.time() for allocation in equipment_allocations)
    start_times = [(start_time, start_time.strftime('%I:%M %p')) for start_time in sorted(start_times)]
    
    scheduling = []
    for equipment_name in equipment_names:
        row = [equipment_name]
        equipment_allocations_for_equipment = equipment_allocations.filter(equipment__name=equipment_name)
        for start_time in start_times:  
            count = 0
            for allocation in equipment_allocations_for_equipment:
                if allocation.start_datetime.time() == start_time[0]:
                    count += 1
            if count > 0:
                row.append('allocated at')
            else:
                row.append('')
        scheduling.append(row)
    
    context = {
        'equipment_names': equipment_names,
        'TIME_CHOICES': my_time_choices,
        'start_times': start_times,
        'scheduling': scheduling
    }
    
    return render(request, 'allocatorhod_templates/view_researcher_HPC_scheduling.html', context)




from datetime import datetime
import pytz
def exportResearcherAllocation(request):
    if request.method == 'POST':
        file_format = request.POST.get('format')
        allocations = EquipmentAllocation.objects.all()  
    
        if file_format == 'csv':
            # Generate CSV file
            response = HttpResponse(content_type='text/csv')
            filename = 'allocation.csv'  # Default file name
            filepath = os.path.join('researcher_allocations', filename)  # Default file path
            
            # Get custom file name from request
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.csv'
                filepath = os.path.join('researcher_allocations', filename)
            
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            writer = csv.writer(response)
            writer.writerow(['Equipment', 'Start Date', 'Start Time', 'End Date', 'End Time'])
            for allocation in allocations:
                start_date = allocation.start_datetime.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d')
                start_time = allocation.start_datetime.astimezone(pytz.timezone('UTC')).strftime('%H:%M:%S')
                end_date = allocation.end_datetime.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d')
                end_time = allocation.end_datetime.astimezone(pytz.timezone('UTC')).strftime('%H:%M:%S')
                writer.writerow([allocation.equipment.name, start_date, start_time, end_date, end_time])
            
            return response
        
        elif file_format == 'pdf':
            # Generate PDF file
            filename = 'allocation.pdf'  # Default file name
            
            # Get custom file name from request
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.pdf'
            
            filepath = os.path.join('researcher_allocations', filename)  # Default file path
            
            # Create data for table
            data = [['Equipment', 'Start Date', 'Start Time', 'End Date', 'End Time']]
            for allocation in allocations:
                start_date = allocation.start_datetime.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d')
                start_time = allocation.start_datetime.astimezone(pytz.timezone('UTC')).strftime('%H:%M:%S %p')
                end_date = allocation.end_datetime.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d')
                end_time = allocation.end_datetime.astimezone(pytz.timezone('UTC')).strftime('%H:%M:%S %p')
                data.append([
                    allocation.equipment.name,
                    start_date,
                    start_time,
                    end_date,
                    end_time,
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
            
            # Create the table
            table = Table(data)
            table.setStyle(table_style)

            # Add the table and a PageBreak flowable to the elements list
            elements= [table, PageBreak()]
            
            # Build the PDF document
            doc.build(elements)
            
            # Return the file as an HTTP response
            with open(filepath, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            return response
        
        elif file_format == 'xls':
            # Get custom file name from request
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.xls'
            else:
                filename = 'allocation.xls'  # Default file name
            
            filepath = os.path.join('researcher_allocations', filename)  # Default file path
            
            # Code to generate XLS file using xlwt library
            wb = xlwt.Workbook()
            sheet = wb.add_sheet('allocation')
            sheet.write(0, 0, 'Equipment')
            sheet.write(0, 1, 'Start Date')
            sheet.write(0, 2, 'Start Time')
            sheet.write(0, 3, 'End Date')
            sheet.write(0, 4, 'End Time')
            row = 1
            for allocation in allocations:
                start_date = allocation.start_datetime.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d')
                start_time = allocation.start_datetime.astimezone(pytz.timezone('UTC')).strftime('%H:%M:%S %p')
                end_date = allocation.end_datetime.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d')
                end_time = allocation.end_datetime.astimezone(pytz.timezone('UTC')).strftime('%H:%M:%S %p')
                sheet.write(row, 0, allocation.equipment.name)
                sheet.write(row, 1, start_date)
                sheet.write(row, 2, start_time)
                sheet.write(row, 3, end_date)
                sheet.write(row, 4, end_time)
                row += 1

            wb.save(filepath)
            
            with open(filepath, 'rb') as xls_file:
                response = HttpResponse(xls_file.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            return response
    
    return render(request, 'template.html', {'allocations': allocations, 'template_content': template.render({'allocations': allocations})})



def showResearcherAboutUsPage(request):
    
    return render(request, 'allocatorhod_templates/researcher_about_us.html') 