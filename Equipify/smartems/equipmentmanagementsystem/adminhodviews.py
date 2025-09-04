# from django.shortcuts import render
# from equipmentmanagementsystem.models import AllocatorHOD, Category, Equipment, ManagerHOD
# from urllib import request

# from urllib import request

# from django.contrib import messages
# # from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect, get_object_or_404

# # from equipmentmanagementsystem.forms import AddManagerForm, EditManagerForm, AddCategoryForm, EditCategoryForm
# from equipmentmanagementsystem.models import CustomUser, Category, ManagerHOD, AllocatorHOD, Equipment, AdminHOD
# from django.urls import reverse
# from django.core.files.storage import FileSystemStorage

# from urllib import request
# from django import template
# from django.template.loader import render_to_string
# from datetime import datetime, date
# from django.contrib import messages
# from django.db.models import Q
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect, get_object_or_404
# import os
# import csv
# from jinja2 import Environment, FileSystemLoader
# from equipmentmanagementsystem.forms import AddManagerForm, EditManagerForm, AddCategoryForm, EditCategoryForm, AddRoomForm, EditRoomForm, AddInventoryForm
# from equipmentmanagementsystem.models import CustomUser, Category, ManagerHOD , AllocatorHOD, Equipment, Room, Inventory, AdminHOD
# from django.urls import reverse
# from django.core.files.storage import FileSystemStorage
# # from reportlab.pdfgen import canvas
# from django.http import FileResponse
# # import pandas as pd
# # from openpyxl import Workbook
# import PyPDF2
# # import xlwt
# # from reportlab.lib.pagesizes import letter
# # from reportlab.lib import colors
# # from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
# # from reportlab.lib.styles import getSampleStyleSheet
# from django.conf import settings
# from django.template.loader import get_template

from tkinter.ttk import Style
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


# def showAdminPage(request):
#     managers = ManagerHOD.objects.all()
#     manager_count = managers.count()
#     allocators = AllocatorHOD.objects.all()
#     allocator_count = allocators.count()
#     categories = Category.objects.all()
#     category_count = categories.count()
#     equipments = Equipment.objects.all()
#     equipment_count = equipments.count()

#     return render(request, 'adminhod_templates/home_content.html',
#      {'manager_count':manager_count, 'allocator_count':allocator_count, 'category_count':category_count,
#       'equipment_count':equipment_count})



# def addManager(request):
#     form = AddManagerForm()
#     return render(request, 'adminhod_templates/add_manager.html', {"form":form})


# def saveAddManager(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         form = AddManagerForm(request.POST, request.FILES)
#         if form.is_valid():
#             fullname = form.cleaned_data['fullname']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             phonenumber = form.cleaned_data['phonenumber']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             profilepicture = request.FILES['profilepicture']
#             fss = FileSystemStorage()
#             filename = fss.save(profilepicture.name, profilepicture)
#             profilepictureurl = fss.url(filename)

#             try:
#                 user = CustomUser.objects.create_user(username=username,
#                                                       email=email, password=password, first_name=first_name,
#                                                       last_name=last_name, user_type=2)
#                 user.managerhod.fullname = fullname
#                 user.managerhod.phonenumber = phonenumber
#                 user.managerhod.profilepicture = profilepictureurl
#                 user.save()
#                 messages.success(request, "Successfully Added")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_manager"))
#             except:
#                 messages.error(request, "Could Not Add ")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_manager"))

#         else:
#             form = AddManagerForm(request.POST, request.FILES)
#             return render(request, 'adminhod_templates/add_manager.html', {"form":form})

# def addCategory(request):
#     form = AddCategoryForm()
#     return render(request, 'adminhod_templates/add_category.html', {"form":form})

# def saveAddCategory(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         form = AddCategoryForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             #icone= request.FILES['icone']
#             #fss = FileSystemStorage()
#             #filename = fss.save(icone.name, icone)
#             #iconeurl = fss.url(filename)


#             try:
#                 category_model = Category(name=name, description=description )
#                 category_model.save()
#                 messages.success(request, "Successfully Added")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_category"))
#             except:
#                 messages.error(request, "Failled Added ")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_category"))

#         else:
#             form = AddCategoryForm(request.POST)
#             return render(request, 'adminhod_templates/add_category.html', {"form":form})


# def addRoom(request):
#     form = AddRoomForm()
#     return render(request, 'adminhod_templates/add_room.html', {"form":form})

# def saveAddRoom(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         form = AddRoomForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             location = form.cleaned_data['location']
#             capacity = form.cleaned_data['capacity']
           


#             try:
#                 room_model = Room(name=name, location=location, capacity=capacity)
#                 room_model.save()
#                 messages.success(request, "Successfully Added")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_room"))
#             except:
#                 messages.error(request, "Failled Added ")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_room"))

#         else:
#             form = AddRoomForm(request.POST)
#             return render(request, 'adminhod_templates/add_room.html', {"form":form})




# def addInventory(request):
#     form = AddInventoryForm()
#     return render(request, 'adminhod_templates/add_inventory.html', {"form":form})

# def saveAddInventory(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         form = AddInventoryForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
            


#             try:
#                 inventory_model = Inventory(name=name, description=description)
#                 inventory_model.save()
#                 messages.success(request, "Successfully Added")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_inventory"))
#             except:
#                 messages.error(request, "Failled Added ")
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_inventory"))

#         else:
#             form = AddInventoryForm(request.POST)
#             return render(request, 'adminhod_templates/add_inventory.html', {"form":form})

  
# def viewManager(request):
#     manager = ManagerHOD.objects.all()
#     return render(request, 'adminhod_templates/view_manager.html', {"managers": manager})


# def viewCategory(request):
#     category = Category.objects.all()
#     return render(request, 'adminhod_templates/view_category.html', {"categories": category})

# def viewRoom(request):
#     room = Room.objects.all()
#     return render(request, 'adminhod_templates/view_room.html', {"rooms": room})    

# def viewInventories(request):
#     inventory = Inventory.objects.all()
#     return render(request, 'adminhod_templates/view_inventories.html', {"inventories": inventory})    



# def editManager(request, manager_id):
#     request.session['manager_id']=manager_id
#     manager = ManagerHOD.objects.get(admin=manager_id)
#     form = EditManagerForm()
#     form.fields['email'].initial=manager.admin.email
#     form.fields['phonenumber'].initial = manager.phonenumber
#     form.fields['username'].initial = manager.admin.username
#     form.fields['first_name'].initial = manager.admin.first_name
#     form.fields['last_name'].initial = manager.admin.email
#     form.fields['fullname'].initial = manager.fullname
#     form.fields['profilepicture'].initial = manager.profilepicture
#     return render(request, 'adminhod_templates/edit_manager.html', {"form": form, "id":manager_id})


# def saveEditManager(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         manager_id = request.session.get('manager_id')
#         if manager_id == None :
#             return HttpResponseRedirect("/view_manager")
#         form = EditManagerForm(request.POST, request.FILES)
#         if form.is_valid():
#             fullname = form.cleaned_data['fullname']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             phonenumber = form.cleaned_data['phonenumber']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']

#             if request.FILES.get('profilepicture', False):
#                 profilepicture = request.FILES['profilepicture']
#                 fss = FileSystemStorage()
#                 filename = fss.save(profilepicture.name, profilepicture)
#                 profilepictureurl = fss.url(filename)
#             else:
#                 profilepictureurl = None

#             try:

#                 user = CustomUser.objects.get(id=manager_id)
#                 user.first_name = first_name
#                 user.last_name = last_name
#                 user.username = username
#                 user.email = email
#                 user.save()
#                 manager_model = ManagerHOD.objects.get(admin=manager_id)
#                 manager_model.fullname = fullname
#                 manager_model.phonenumber = phonenumber

#                 if profilepictureurl != None:
#                     manager_model.profilepicture = profilepictureurl

#                 manager_model.save()
#                 del request.session['manager_id']
#                 messages.success(request, "Successfully Edited")
#                 return HttpResponseRedirect("/edit_manager/" + manager_id)
#             except:
#                 messages.error(request, "Could Not Edit ")
#                 return HttpResponseRedirect("/edit_manager/" + manager_id)
#         else:
#             form = EditManagerForm(request.POST)
#             return render(request, 'adminhod_templates/edit_manager.html', {"form":form , "id":manager_id})


# def editCategory(request, category_id):
#     request.session['category_id']=category_id
#     category = Category.objects.get(id=category_id)
#     form = EditCategoryForm()
#     form.fields['name'].initial = category.name
#     form.fields['description'].initial = category.description
#     #form.fields['icone'].initial = manager.icone
#     return render(request, 'adminhod_templates/edit_category.html' , {"form": form, "id":category_id})






# def saveEditCategory(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         category_id = request.session.get('category_id')
#         if category_id == None :
#             return HttpResponseRedirect("/view_categories")
#         form = EditCategoryForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']

#             #if request.FILES.get('icone', False):
#                 #icone = request.FILES['picone']
#                 #fss = FileSystemStorage()
#                 #filename = fss.save(icone.name, icone)
#                 #iconeurl = fss.url(filename)
#             #else:
#                 #iconeurl = None

#             try:

#                 category_model = Category.objects.get(id=category_id)
#                 category_model .name = name
#                 category_model .description = description

#                 #if iconeurl != None:
#                     #Scategory_model.icone = iconeurl

#                 category_model .save()
#                 del request.session['category_id']
#                 messages.success(request, "Successfully Edited")
#                 return HttpResponseRedirect("/edit_category/" + category_id)
#             except:
#                 messages.error(request, "Could Not Edit ")
#                 return HttpResponseRedirect("/edit_category/" + category_id)
#         else:
#             form = EditCategoryForm(request.POST)
#             return render(request, 'adminhod_templates/edit_category.html', {"form":form , "id":category_id})





# def editRoom(request, room_id):
#     request.session['room_id']=room_id
#     room = Room.objects.get(id=room_id)
#     form = EditRoomForm()
#     form.fields['name'].initial = room.name
#     form.fields['location'].initial = room.location
#     form.fields['capacity'].initial = room.capacity
    
#     return render(request, 'adminhod_templates/edit_room.html' , {"form": form, "id":room_id})






# def saveEditRoom(request):
#     if request.method != "POST":
#         return HttpResponse("method not allowed")
#     else:
#         room_id = request.session.get('room_id')
#         if room_id == None :
#             return HttpResponseRedirect("/view_rooms")
#         form = EditRoomForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             location = form.cleaned_data['location']
#             capacity = form.cleaned_data['capacity']



#             try:

#                 room_model = Room.objects.get(id=room_id)
#                 room_model.name = name
#                 room_model.location = location
#                 room_model.capacity = capacity



#                 room_model.save()
#                 del request.session['room_id']
#                 messages.success(request, "Successfully Edited")
#                 return HttpResponseRedirect("/edit_room/" + room_id)
#             except:
#                 messages.error(request, "Could Not Edit ")
#                 return HttpResponseRedirect("/edit_room/" + room_id)
#         else:
#             form = EditRoomForm(request.POST)
#             return render(request, 'adminhod_templates/edit_room.html', {"form":form , "id":room_id})



# def deleteManager(request, manager_id):
#     manager = ManagerHOD.objects.get(admin=manager_id)
#     manager.delete()
#     return HttpResponseRedirect("/view_manager")


# def deleteCategory(request, category_id):
#     category = Category.objects.get(id=category_id)
#     category.delete()
#     return HttpResponseRedirect("/view_categories") 

# def deleteRoom(request, room_id):
#     room = Room.objects.get(id=room_id)
#     room.delete()
#     return HttpResponseRedirect("/view_rooms")   

# # def deleteInventory(request, inventory_id):
# #     inventory = Inventory.objects.get(id=inventory_id)
# #     inventory.delete()
# #     return HttpResponseRedirect("/view_inventories")       



# # def addNewInventory(request):
# #     # Récupérer tous les équipements de la base de données, triés par ordre décroissant de la date de création
# #     equipments = Equipment.objects.order_by('-created_at')
# #     categories = Category.objects.all().values_list('name', flat=True).distinct()
# #     types = Equipment.objects.all().values_list('type', flat=True).distinct()
# #     models = Equipment.objects.all().values_list('model', flat=True).distinct()
# #     brands = Equipment.objects.all().values_list('brand', flat=True).distinct()
# #     rooms = Room.objects.all().values_list('name', flat=True).distinct()

# #     context = {
# #         'categories': categories,
# #         'types': types,
# #         'models': models,
# #         'brands': brands,
# #         'rooms': rooms,
# #         'equipments': equipments,
# #     }

# #     return render(request, 'adminhod_templates/view_inventory.html', context)

# # def searchInventory(request):
# #     query = request.GET.get('query')

# #     # Effectuer la recherche dans la base de données
# #     equipments = Equipment.objects.filter(name__icontains=query)

# #     context = {
# #         'equipments': equipments,
# #         'query': query,
# #         'search_results': True
# #     }

# #     return render(request, 'adminhod_templates/view_inventory.html', context)    












# # #def restoreInventory(request):
    

# #     if filepath == os.path.join('inventaires', 'inventory.csv'): 
# #         inventory_content = ''
    
# #         # Lire le contenu du fichier
# #         with open(filepath, 'r') as csvfile:
# #           inventory_content = csvfile.read()

# #         context = {'inventory_content': inventory_content}
# #         return render(request, 'restore_inventory_csv.html', context) 
    


# #     elif filepath == os.path.join('inventaires', 'inventory.pdf'):
# #         inventory_content = ''

# #         # Lire le contenu du fichier PDF
# #         with open(filepath, 'rb') as pdf_file:
# #              reader = PyPDF2.PdfFileReader(pdf_file)
# #              for page in range(reader.numPages):
# #                  page_content = reader.getPage(page).extract_text()
# #                  inventory_content += page_content

# #         context = {'inventory_content': inventory_content}
# #         return render(request, 'restore_inventory_pdf.html', context) 


# #     elif filepath == os.path.join('inventaires', 'inventory.xls'):  # Chemin complet du fichier XLS d'inventaire
# #              inventory_df = pd.read_excel(filepath)

# #              inventory_content = inventory_df.to_html()

# #              context = {'inventory_content': inventory_content}
# #              return render(request, 'restore_inventory_xls.html', context) 


# # def exportInventory(request):

# #     if request.method == 'POST':
# #         file_format = request.POST.get('format')
# #         equipments = Equipment.objects.all() 
        
# #         # Vérifier si des résultats de recherche sont disponibles dans la requête POST
# #         search_results = request.POST.get('search_results')
# #         if search_results:
# #             equipments = Equipment.objects.filter(name__icontains=search_results)

        
# #         if file_format == 'csv':
# #             # Générer le fichier CSV
# #             response = HttpResponse(content_type='text/csv')
# #             filename = 'inventory.csv'  # Nom de fichier par défaut
# #             filepath = os.path.join('inventaires', filename)  # Emplacement par défaut
            
# #             # Récupérer le nom de fichier personnalisé depuis la requête
# #             custom_filename = request.POST.get('filename')
# #             if custom_filename:
# #                 filename = f'{custom_filename}.csv'
# #                 filepath = os.path.join('inventaires', filename)
            
# #             response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
# #             writer = csv.writer(response)
# #             writer.writerow(['Nom', 'Serialnumber', 'Quantité'])
# #             for equipment in equipments:
# #                 writer.writerow([equipment.name, equipment.serialnumber, equipment.totalnumber])
            
# #             return response
        
# #         elif file_format == 'pdf':
# #             # Récupérer le nom de fichier personnalisé depuis la requête
# #             custom_filename = request.POST.get('filename')
# #             if custom_filename:
# #                 filename = f'{custom_filename}.pdf'
# #             else:
# #                 filename = 'inventory.pdf'  # Nom de fichier par défaut
            
# #             filepath = os.path.join('inventaires', filename)  # Emplacement par défaut
            
# #             # Créer les données du tableau
# #             data = [['Nom', 'SerialNumber', 'Quantité']]
# #             for equipment in equipments:
# #                 data.append([equipment.name, equipment.serialnumber, equipment.totalnumber])
            
# #             # Créer le document PDF
# #             doc = SimpleDocTemplate(filepath, pagesize=letter)
            
# #             # Style du tableau
# #             style = TableStyle([
# #                 ('BACKGROUND', (0, 0), (-1, 0), colors.black),
# #                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
# #                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
# #                 ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
# #                 ('FONTSIZE', (0, 0), (-1, 0), 12),
# #                 ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
# #                 ('BACKGROUND', (0, 1), (-1, -1), colors.white),
# #                 ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
# #                 ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
# #                 ('FONTSIZE', (0, 1), (-1, -1), 10),
# #                 ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
# #                 ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
# #                 ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
# #                  # Ajouter des bordures
# #                 ('GRID', (0, 0), (-1, -1), 1, colors.black),
# #             ])
            
# #             # Créer le tableau
# #             table = Table(data)
# #             table.setStyle(style)
            
# #             # Construire le document PDF
# #             elements = [table]
# #             doc.build(elements)
            
# #             # Renvoyer le fichier en tant que réponse HTTP
# #             with open(filepath, 'rb') as pdf_file:
# #                 response = HttpResponse(pdf_file.read(), content_type='application/pdf')
# #                 response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
# #             return response
        
# #         elif file_format == 'xls':
# #             # Récupérer le nom de fichier personnalisé depuis la requête
# #             custom_filename = request.POST.get('filename')
# #             if custom_filename:
# #                 filename = f'{custom_filename}.xls'
# #             else:
# #                 filename = 'inventory.xls'  # Nom de fichier par défaut
            
# #             filepath = os.path.join('inventaires', filename)  # Emplacement par défaut
            
# #             # Code pour générer le fichier XLS en utilisant la bibliothèque xlwt
# #             wb = xlwt.Workbook()
# #             sheet = wb.add_sheet('Inventory')
# #             sheet.write(0, 0, 'Nom')
# #             sheet.write(0, 1, 'Serialnumber')
# #             sheet.write(0, 2, 'Quantité')
# #             row = 1
# #             for equipment in equipments:
# #                 sheet.write(row, 0, equipment.name)
# #                 sheet.write(row, 1, equipment.serialnumber)
# #                 sheet.write(row, 2, equipment.totalnumber)
# #                 row += 1
# #             wb.save(filepath)
            
# #             with open(filepath, 'rb') as xls_file:
# #                 response = HttpResponse(xls_file.read(), content_type='application/vnd.ms-excel')
# #                 response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
# #             return response
    
# #     return render(request, 'template.html', {'equipments': equipments, 'template_content': template.render({'equipments': equipments})})

# # def saveInventory(request):
# #     template_dir = os.path.join(settings.BASE_DIR, 'equipmentmanagementsystem/templates')

# #     # Récupérer le contenu du modèle de l'inventaire
# #     equipments = Equipment.objects.all()  # Récupérer les données des équipements
# #     template_content = render_to_string('inventory_template.html', {'equipments': equipments})

# #     # Chemin et nom de fichier pour le modèle HTML
# #     template_filename = 'inventory_template.html'
# #     template_filepath = os.path.join(template_dir, template_filename)

# #     # Sauvegarder le contenu du modèle HTML dans un fichier
# #     with open(template_filepath, 'w', encoding='utf-8') as file:
# #         file.write(template_content)

# #     # Afficher la page de sauvegarde du modèle de l'inventaire
# #     return HttpResponse('File saved successfully')
# #     return render(request, 'save_inventory.html', {'template_content': template_content})

# # #def viewInventoryTemplate(request):
# #     template_dir = os.path.join(settings.BASE_DIR, 'equipmentmanagementsystem/templates')
# #     template_filepath = os.path.join(template_dir, 'inventory_template.html')

# #     with open(template_filepath, 'r', encoding='utf-8') as file:
# #         template_content = file.read()

# #     equipments = Equipment.objects.all()  # Récupérer les données des équipements

# #     # Rendre la vue en utilisant le contenu du modèle sauvegardé
# #     return render(request, 'view_inventory_template.html', {'equipments': equipments, 'template_content': template_content})

# def admin_profile(request):
#     user = CustomUser.objects.get(id=request.user.id)
#     admin = AdminHOD.objects.get(admin=user)
#     return render(request, "adminhod_templates/admin_profile.html", {"user": user, "admin": admin})




# def admin_profile_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("admin_profile"))
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

#             admin= AdminHOD.objects.get(admin=customuser.id)
#             admin.fullname = fullname
#             admin.phonenumber = phonenumber
#             admin.save()

#             if password_changed:
#                 messages.success(request, "Successfully Updated Profile")
#                 return HttpResponseRedirect(reverse("show_login"))
#             else:
#                 messages.success(request, "Successfully Updated Profile")
#                 return HttpResponseRedirect(reverse("admin_profile"))
#         except:
#             messages.error(request, "Failed to Update Profile")
#             return HttpResponseRedirect(reverse("admin_profile"))  



# #def save_form(request):
#     return render(request, 'adminhod_templates/inventory_save_form.html')    


# #def save_inventory_submit(request):
#     if request.method == 'POST':
#         filename = request.POST.get('filename')
#         description = request.POST.get('description')
#         # Traitez les données soumises et effectuez la sauvegarde

#         return HttpResponse("La sauvegarde a été effectuée avec succès.")
#     else:
#         return HttpResponse("Méthode non autorisée.")    

from django.core import serializers
import json
from django.contrib import messages
from django.urls import reverse

def showAdminPage(request):
    managers = ManagerHOD.objects.all()
    manager_count = managers.count()
    allocators = AllocatorHOD.objects.all()
    allocator_count = allocators.count()
    categories = Category.objects.all()
    category_count = categories.count()
    equipments = Equipment.objects.all()
    equipment_count = equipments.count()

    return render(request, 'adminhod_templates/home_content.html',
     {'manager_count':manager_count, 'allocator_count':allocator_count, 'category_count':category_count,
      'equipment_count':equipment_count})


  


def addManager(request):
    form = AddManagerForm()
    return render(request, 'adminhod_templates/add_manager.html', {"form":form})


def saveAddManager(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        form = AddManagerForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phonenumber = form.cleaned_data['phonenumber']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            profilepicture = request.FILES['profilepicture']
            fss = FileSystemStorage()
            filename = fss.save(profilepicture.name, profilepicture)
            profilepictureurl = fss.url(filename)

            try:
                user = CustomUser.objects.create_user(username=username,
                                                      email=email, password=password, first_name=first_name,
                                                      last_name=last_name, user_type=2)
                user.managerhod.fullname = fullname
                user.managerhod.phonenumber = phonenumber
                user.managerhod.profilepicture = profilepictureurl
                user.save()
                messages.success(request, "Successfully Added")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_manager"))
            except:
                messages.error(request, "Could Not Add ")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_manager"))

        else:
            form = AddManagerForm(request.POST, request.FILES)
            return render(request, 'adminhod_templates/add_manager.html', {"form":form})

def addCategory(request):
    form = AddCategoryForm()
    return render(request, 'adminhod_templates/add_category.html', {"form":form})

def saveAddCategory(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            #icone= request.FILES['icone']
            #fss = FileSystemStorage()
            #filename = fss.save(icone.name, icone)
            #iconeurl = fss.url(filename)


            try:
                category_model = Category(name=name, description=description )
                category_model.save()
                messages.success(request, "Successfully Added")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_category"))
            except:
                messages.error(request, "Failled Added ")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_category"))

        else:
            form = AddCategoryForm(request.POST)
            return render(request, 'adminhod_templates/add_category.html', {"form":form})


def addRoom(request):
    form = AddRoomForm()
    return render(request, 'adminhod_templates/add_room.html', {"form":form})

def saveAddRoom(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        form = AddRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            capacity = form.cleaned_data['capacity']
           


            try:
                room_model = Room(name=name, location=location, capacity=capacity)
                room_model.save()
                messages.success(request, "Successfully Added")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_room"))
            except:
                messages.error(request, "Failled Added ")
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:add_room"))

        else:
            form = AddRoomForm(request.POST)
            return render(request, 'adminhod_templates/add_room.html', {"form":form})






  
def viewManager(request):
    manager = ManagerHOD.objects.all()
    return render(request, 'adminhod_templates/view_manager.html', {"managers": manager})


def viewCategory(request):
    name = request.GET.get('name')
    categories = Category.objects.all().order_by('-id')
    if name:
        categories = categories.filter(name__icontains=name)
    context = {
        'categories': categories,
        'selected_name': name,
    }
    return render(request, 'adminhod_templates/view_category.html', context)



def viewRoom(request):
    name = request.GET.get('name')
    location = request.GET.get('location')
    rooms = Room.objects.all().order_by('-id')
    if name:
        rooms = rooms.filter(name__icontains=name)
    if location:
        rooms = rooms.filter(location__icontains=location)

    context = {
        'rooms': rooms,
    }
    return render(request, 'adminhod_templates/view_room.html', context) 

   



def editManager(request, manager_id):
    request.session['manager_id']=manager_id
    manager = ManagerHOD.objects.get(admin=manager_id)
    form = EditManagerForm()
    form.fields['email'].initial=manager.admin.email
    form.fields['phonenumber'].initial = manager.phonenumber
    form.fields['username'].initial = manager.admin.username
    form.fields['first_name'].initial = manager.admin.first_name
    form.fields['last_name'].initial = manager.admin.email
    form.fields['fullname'].initial = manager.fullname
    form.fields['profilepicture'].initial = manager.profilepicture
    return render(request, 'adminhod_templates/edit_manager.html', {"form": form, "id":manager_id})


def saveEditManager(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        manager_id = request.session.get('manager_id')
        if manager_id == None :
            return HttpResponseRedirect("/view_manager")
        form = EditManagerForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phonenumber = form.cleaned_data['phonenumber']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            if request.FILES.get('profilepicture', False):
                profilepicture = request.FILES['profilepicture']
                fss = FileSystemStorage()
                filename = fss.save(profilepicture.name, profilepicture)
                profilepictureurl = fss.url(filename)
            else:
                profilepictureurl = None

            try:

                user = CustomUser.objects.get(id=manager_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()
                manager_model = ManagerHOD.objects.get(admin=manager_id)
                manager_model.fullname = fullname
                manager_model.phonenumber = phonenumber

                if profilepictureurl != None:
                    manager_model.profilepicture = profilepictureurl

                manager_model.save()
                del request.session['manager_id']
                messages.success(request, "Successfully Edited")
                return HttpResponseRedirect("/edit_manager/" + manager_id)
            except:
                messages.error(request, "Could Not Edit ")
                return HttpResponseRedirect("/edit_manager/" + manager_id)
        else:
            form = EditManagerForm(request.POST)
            return render(request, 'adminhod_templates/edit_manager.html', {"form":form , "id":manager_id})


def editCategory(request, category_id):
    request.session['category_id']=category_id
    category = Category.objects.get(id=category_id)
    form = EditCategoryForm()
    form.fields['name'].initial = category.name
    form.fields['description'].initial = category.description
    #form.fields['icone'].initial = manager.icone
    return render(request, 'adminhod_templates/edit_category.html' , {"form": form, "id":category_id})






def saveEditCategory(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        category_id = request.session.get('category_id')
        if category_id == None :
            return HttpResponseRedirect("/view_categories")
        form = EditCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            #if request.FILES.get('icone', False):
                #icone = request.FILES['picone']
                #fss = FileSystemStorage()
                #filename = fss.save(icone.name, icone)
                #iconeurl = fss.url(filename)
            #else:
                #iconeurl = None

            try:

                category_model = Category.objects.get(id=category_id)
                category_model .name = name
                category_model .description = description

                #if iconeurl != None:
                    #Scategory_model.icone = iconeurl

                category_model .save()
                del request.session['category_id']
                messages.success(request, "Successfully Edited")
                return HttpResponseRedirect("/edit_category/" + category_id)
            except:
                messages.error(request, "Could Not Edit ")
                return HttpResponseRedirect("/edit_category/" + category_id)
        else:
            form = EditCategoryForm(request.POST)
            return render(request, 'adminhod_templates/edit_category.html', {"form":form , "id":category_id})





def editRoom(request, room_id):
    request.session['room_id']=room_id
    room = Room.objects.get(id=room_id)
    form = EditRoomForm()
    form.fields['name'].initial = room.name
    form.fields['location'].initial = room.location
    form.fields['capacity'].initial = room.capacity
    
    return render(request, 'adminhod_templates/edit_room.html' , {"form": form, "id":room_id})






def saveEditRoom(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        room_id = request.session.get('room_id')
        if room_id == None :
            return HttpResponseRedirect("/view_rooms")
        form = EditRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            capacity = form.cleaned_data['capacity']



            try:

                room_model = Room.objects.get(id=room_id)
                room_model.name = name
                room_model.location = location
                room_model.capacity = capacity



                room_model.save()
                del request.session['room_id']
                messages.success(request, "Successfully Edited")
                return HttpResponseRedirect("/edit_room/" + room_id)
            except:
                messages.error(request, "Could Not Edit ")
                return HttpResponseRedirect("/edit_room/" + room_id)
        else:
            form = EditRoomForm(request.POST)
            return render(request, 'adminhod_templates/edit_room.html', {"form":form , "id":room_id})



# def deleteManager(request, manager_id):
#     manager = ManagerHOD.objects.get(admin=manager_id)
#     manager.delete()
#     return HttpResponseRedirect("/view_manager")

def deleteManager(request, manager_id):
    try:
        manager_hod = ManagerHOD.objects.get(admin=manager_id)
        custom_user = CustomUser.objects.get(id=manager_id)
    except (ManagerHOD.DoesNotExist, CustomUser.DoesNotExist):
        return HttpResponseNotFound("Manager not found")

    # Delete the manager
    manager_hod.delete()
    custom_user.delete()

    return HttpResponseRedirect("/view_manager")




# def deleteCategory(request, category_id):
#     category = Category.objects.get(id=category_id)
#     category.delete()
#     return HttpResponseRedirect("/view_categories") 








def deleteCategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    equipment_count = Equipment.objects.filter(category_id=category_id).count()

    if equipment_count > 0:
        messages.error(request, f"Cannot delete category '{category.name}' because it has {equipment_count} equipment(s).")
        return redirect(reverse('equipmentmanagementsystem:view_category'))
        
    else:
        category.delete()
        messages.success(request, "Category deleted successfully.")

    return redirect(reverse('equipmentmanagementsystem:view_category'))


# def deleteRoom(request, room_id):
#     room = Room.objects.get(id=room_id)
#     room.delete()
#     return HttpResponseRedirect("/view_rooms")   




def deleteRoom(request, room_id):
    room = Room.objects.get(id=room_id)
    equipment_count = Equipment.objects.filter(room_id=room_id).count()

    if equipment_count > 0:
        messages.error(request, f"Cannot delete room '{room.name}' because it has equipment(s).")
        return redirect(reverse('equipmentmanagementsystem:view_rooms'))
        
    else:
        room.delete()
        messages.success(request, "Room deleted successfully.")

    return redirect(reverse('equipmentmanagementsystem:view_rooms'))

   



# def addNewInventory(request):
#     # Récupérer tous les équipements de la base de données, triés par ordre décroissant de la date de création
#     equipments = Equipment.objects.order_by('-created_at')
#     categories = Category.objects.all().values_list('name', flat=True).distinct()
#     types = Equipment.objects.all().values_list('type', flat=True).distinct()
#     models = Equipment.objects.all().values_list('model', flat=True).distinct()
#     brands = Equipment.objects.all().values_list('brand', flat=True).distinct()
#     rooms = Room.objects.all().values_list('name', flat=True).distinct()

#     context = {
#         'categories': categories,
#         'types': types,
#         'models': models,
#         'brands': brands,
#         'rooms': rooms,
#         'equipments': equipments,
#     }

#     return render(request, 'adminhod_templates/view_inventory.html', context)



def addNewInventory(request):
    
    category = request.GET.get('category')
    type = request.GET.get('type')
    model = request.GET.get('model')
    brand = request.GET.get('brand')
    room = request.GET.get('room')

  
    equipments = Equipment.objects.all().order_by('-created_at')
    if category:
        equipments = equipments.filter(category_id__name=category)
    if type:
        equipments = equipments.filter(type=type)
    if model:
        equipments = equipments.filter(model=model)
    if brand:
        equipments = equipments.filter(brand=brand)
    if room:
        equipments = equipments.filter(room_id__name=room)

    categories = Category.objects.all().values_list('name', flat=True).distinct()
    types = Equipment.objects.all().values_list('type', flat=True).distinct()
    models = Equipment.objects.all().values_list('model', flat=True).distinct()
    brands = Equipment.objects.all().values_list('brand', flat=True).distinct()
    rooms = Room.objects.all().values_list('name', flat=True).distinct()

    context = {
        'categories': categories,
        'types': types,
        'models': models,
        'brands': brands,
        'rooms': rooms,
        'equipments': equipments,
    }

    return render(request, 'adminhod_templates/view_inventory.html', context)

def searchInventory(request):
    query = request.GET.get('query')

    # Effectuer la recherche dans la base de données
    equipments = Equipment.objects.filter(name__icontains=query)

    context = {
        'equipments': equipments,
        'query': query,
        'search_results': True
    }

    return render(request, 'adminhod_templates/view_inventory.html', context)    














def exportInventory(request):
    if request.method == 'POST':
        file_format = request.POST.get('format')
        equipments = Equipment.objects.all()  
        
    
        
        if file_format == 'csv':
            # Générer le fichier CSV
            response = HttpResponse(content_type='text/csv')
            filename = 'inventory.csv'  # Nom de fichier par défaut
            filepath = os.path.join('inventaires', filename)  # Emplacement par défaut
            
            # Récupérer le nom de fichier personnalisé depuis la requête
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.csv'
                filepath = os.path.join('inventaires', filename)
            
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            writer = csv.writer(response)
            writer.writerow(['Id','Serialnumber','Code', 'Name', 'Category', 'Brand', 'Model', 'Quantity','Room', 'Added in' ])
            for equipment in equipments:
                writer.writerow([equipment.id, equipment.serialnumber, equipment.code, equipment.category_id.name, equipment.brand, equipment.model,  equipment.totalnumber, equipment.room_id.name, equipment.created_at])
            
            return response
        
        elif file_format == 'pdf':
            # Récupérer le nom de fichier personnalisé depuis la requête
            custom_filename = request.POST.get('filename')
            if custom_filename:
                filename = f'{custom_filename}.pdf'
            else:
                filename = 'inventory.pdf'  # Nom de fichier par défaut

            filepath = os.path.join('inventaires', filename)  # Emplacement par défaut

            
            # Créer les données du tableau
            data = [['Id','Serialnumber','Code', 'Name', 'Category', 'Brand', 'Model', 'Quantity','Room', 'Added in' ]]
            for equipment in equipments:
                data.append([equipment.id, equipment.serialnumber, equipment.code,equipment.name, equipment.category_id.name, equipment.brand, equipment.model,  equipment.totalnumber, equipment.room_id.name, equipment.created_at])
            
            # Créer le document PDF
            doc = SimpleDocTemplate(filepath, pagesize=landscape(letter))

            # Style du tableau
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
            # Ajouter des bordures
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
                filename = 'inventory.xls'  # Nom de fichier par défaut
            
            filepath = os.path.join('inventaires', filename)  # Emplacement par défaut
            
            # Code pour générer le fichier XLS en utilisant la bibliothèque xlwt
            wb = xlwt.Workbook()
            sheet = wb.add_sheet('Inventory')
            sheet.write(0, 0, 'Id')
            sheet.write(0, 1, 'Serialnumber')
            sheet.write(0, 2, 'Code')
            sheet.write(0, 3, 'Name')
            sheet.write(0, 4, 'Category')
            sheet.write(0, 5, 'Brand')
            sheet.write(0, 6, 'Model')
            sheet.write(0, 7, 'Quantity')
            sheet.write(0, 8, 'Room')
            sheet.write(0, 9, 'Added in')

            row = 1
            for equipment in equipments:
                sheet.write(row, 0, equipment.id)
                sheet.write(row, 1, equipment.serialnumber)
                sheet.write(row, 2, equipment.code)
                sheet.write(row, 3, equipment.name)
                sheet.write(row, 4, equipment.category_id.name)
                sheet.write(row, 5, equipment.brand)
                sheet.write(row, 6, equipment.model)
                sheet.write(row, 7, equipment.totalnumber)
                sheet.write(row, 8, equipment.room_id.name)
                formatted_date = equipment.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime to string
                sheet.write(row, 9, formatted_date)
                row += 1
            wb.save(filepath)
            
            with open(filepath, 'rb') as xls_file:
                response = HttpResponse(xls_file.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            return response
    
    return render(request, 'template.html', {'equipments': equipments, 'template_content': template.render({'equipments': equipments})})  



def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    admin = AdminHOD.objects.get(admin=user)
    return render(request, "adminhod_templates/admin_profile.html", {"user": user, "admin": admin})




def admin_profile_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("admin_profile"))
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

            admin= AdminHOD.objects.get(admin=customuser.id)
            admin.fullname = fullname
            admin.phonenumber = phonenumber
            admin.save()

            if password_changed:
                messages.success(request, "Successfully Updated password !")
                return redirect('equipmentmanagementsystem:show_login')
            else:
                messages.success(request, "Successfully Updated Profile !")
                return redirect('equipmentmanagementsystem:admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('equipmentmanagementsystem:admin_profile !')   
        

def viewManagers(request):
    manager = ManagerHOD.objects.all()
    return render(request, 'adminhod_templates/view_managers.html', {"managers": manager}) 


def viewAllocators(request):
    allocator = AllocatorHOD.objects.all()
    return render(request, 'adminhod_templates/view_allocators.html', {"allocators": allocator})  

def viewCategories(request):
    category = Category.objects.all()
    return render(request, 'adminhod_templates/view_categories.html', {"categories": category})

def viewEquipments(request):
    equipment = Equipment.objects.all()
    return render(request, 'adminhod_templates/view_equipments.html', {"equipments": equipment})





