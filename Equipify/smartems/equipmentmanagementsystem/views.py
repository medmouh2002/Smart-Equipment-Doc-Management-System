# from django.db import IntegrityError
# from django.shortcuts import render, redirect, reverse
# from django.contrib import messages
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from equipmentmanagementsystem.EmailBackEnd import EmailBackEnd
# import mysql.connector as sql
# from equipmentmanagementsystem.models import CustomUser, AllocatorHOD

# from django.shortcuts import render


# def showDemoPage(request):
#     return render(request, 'demo.html')


# def showLoginPage(request):
#     return render(request, 'login_page.html')


# def doLogin(request):
#     if request.method != "POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
#                                          password=request.POST.get("password"))
#         if user != None:
#             login(request, user)
#             if user.user_type == "1":
#                 return HttpResponseRedirect('/admin_home')
#             elif user.user_type == "2":
#                 return HttpResponseRedirect(reverse('manager_home'))
#             else:
#                 return HttpResponseRedirect(reverse("/allocator_home"))
#         else:
#             messages.error(request, "Invalid Login Details")
#             return HttpResponseRedirect("/")


# def GetUserDetails(request):
#     if request.user != None:
#         return HttpResponse("User : " + request.user.email + " usertype : " + str(request.user.user_type))
#     else:
#         return HttpResponse("Please Login First")
    
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect("/")


# def signup(request):
#     return render(request, 'signup_page.html', {})

# def logOut(request):
#     logout(request)
#     return HttpResponseRedirect("/")



# def signaction(request):
#     if request.method == "POST":
#         m = sql.connect(host="localhost", user="root", passwd="Takwa27297", database='emsdb')
#         cursor = m.cursor()

#         fn = request.POST.get('fullname')
#         pn = request.POST.get('phonenumber')
#         em = request.POST.get('email')
#         pwd = request.POST.get('password')
#         role = request.POST.get('role')

#         c = "INSERT INTO allocator (fullname, phonenumber, email, password, role) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
#             fn, pn, em, pwd, role)
#         cursor.execute(c)
#         m.commit()

#     return render(request, 'signup_page.html')



from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from equipmentmanagementsystem.EmailBackEnd import EmailBackEnd
from django.db import IntegrityError
from django.contrib import messages
import mysql.connector as sql
from django.shortcuts import render, redirect
from equipmentmanagementsystem.models import CustomUser, AllocatorHOD
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth import get_user_model
from django.db.models import Q




def showLoginPage(request):
    return render(request, 'login_page.html')


# def doLogin(request):
#     if request.method != "POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
#                                          password=request.POST.get("password"))
#         if user != None:
#             login(request, user)
#             if user.user_type == "1":
#                 return HttpResponseRedirect('/admin_home')
#             elif user.user_type == "2":
#                 #return HttpResponseRedirect(reverse("/manager_home"))
#                 return HttpResponseRedirect('/manager_home')
#             else:
#                 try:
#                     allocator = AllocatorHOD.objects.get(admin=user)  # Récupérer l'objet Allocator correspondant à l'utilisateur
#                     if allocator.role == "student":  # Vérifier si l'allocateur a le rôle "student"
#                         return HttpResponseRedirect("/student_home") # Rediriger vers la page d'accueil de l'étudiant
#                     elif allocator.role == "researcher":  # Vérifier si l'allocateur a le rôle "researcher"
#                         return HttpResponseRedirect("/researcher_home") # Rediriger vers la page d'accueil du chercheur
#                     else:
#                         return HttpResponse("<h2>Invalid Role</h2>")  # Redirection pour un rôle invalide
#                 except AllocatorHOD.DoesNotExist:
#                     return HttpResponse("<h2>Allocator not found</h2>")  # Gérer le cas où l'allocateur n'existe pas pour cet utilisateur
#         else:
#             messages.error(request, "Invalid Login Details")
#             return HttpResponseRedirect("/")



def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email_or_username = request.POST.get("email_or_username")
        password = request.POST.get("password")
        User = get_user_model()

        try:
            user = User.objects.get(Q(email=email_or_username) | Q(username=email_or_username))
            if user.check_password(password):
                login(request, user)
                if user.user_type == "1":
                    return HttpResponseRedirect('/admin_home')
                elif user.user_type == "2":
                    return HttpResponseRedirect('/manager_home')
                else:
                    try:
                        allocator = AllocatorHOD.objects.get(admin=user)
                        if allocator.role == "student":
                            return HttpResponseRedirect("/student_home")
                        elif allocator.role == "researcher":
                            return HttpResponseRedirect("/researcher_home")
                        else:
                            return HttpResponse("<h2>Invalid Role</h2>")
                    except AllocatorHOD.DoesNotExist:
                        return HttpResponse("<h2>Allocator not found</h2>")
                    except AllocatorHOD.MultipleObjectsReturned:
                        return HttpResponse("<h2>Multiple allocators found for the user</h2>")
            else:
                messages.error(request, "Invalid Login Details")
                return HttpResponseRedirect("/")
        except User.DoesNotExist:
            return HttpResponse("<h2>User not found</h2>")
        except User.MultipleObjectsReturned:
            return HttpResponse("<h2>Multiple users found with the same email or username</h2>")



def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email + " usertype : " + str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


# def signup(request):
#     return render(request, 'signup_page.html')








# #def signaction(request):
#     if request.method == "POST":
#         m = sql.connect(host="localhost", user="root", passwd="mounirbenhedjaz20111975", database='emsdb')
#         cursor = m.cursor()

#         fn = request.POST.get('fullname')
#         pn = request.POST.get('phonenumber')
#         em = request.POST.get('email')
#         pwd = request.POST.get('password')
#         role = request.POST.get('role')

#         c = "INSERT INTO allocator (fullname, phonenumber, email, password, role) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
#             fn, pn, em, pwd, role)
#         cursor.execute(c)
#         m.commit()

#     return render(request, 'signup_page.html')




#def signaction(request):
    # if request.method == "POST":
    #     fn = request.POST.get('fullname')
    #     pn = request.POST.get('phonenumber')
    #     em = request.POST.get('email')
    #     pwd = request.POST.get('password')
    #     role = request.POST.get('role')

    #     AllocatorHOD.objects.create(
    #         fullname=fn,
    #         phonenumber=pn,
    #         email=em,
    #         password=pwd,
    #         role=role
    #     )

    # return render(request, 'signup_page.html')


def signaction(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        role = request.POST.get('role')

        # Vérification d'unicité de l'email ou du nom d'utilisateur
        try:
            user = CustomUser.objects.create_user(email=email, username=username, password=password, user_type=3)
        except IntegrityError:
            return render(request, 'signup_page.html', {'error': 'Email or username already exists'})

        user.allocatorhod.fullname = fullname
        user.allocatorhod.phonenumber = phonenumber

        # Set the role of the AllocatorHod instance based on the user's choice
        if role == 'student':
            user.allocatorhod.role = 'student'
        elif role == 'researcher':
            user.allocatorhod.role = 'researcher'

        user.save()

        return render(request, 'signup_page.html')

    return render(request, 'signup_page.html')



def logOut(request):
    logout(request)
    return HttpResponseRedirect("/")


# #def GetUserDetails(request):
#     if request.user != None:
#         return HttpResponse("User : " + request.user.email + " usertype : " + str(request.user.user_type))
#     else:
#         return HttpResponse("Please Login First")   



from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Notification, EquipmentAllocation

@csrf_exempt
def get_notifications(request):
    notifications = Notification.objects.filter(admin=request.user).order_by('-created_at')
    notification_list = [{"message": notification.message} for notification in notifications]
    
    response = {
        "notifications": notification_list
    }
    
    return JsonResponse(response)


@csrf_exempt
def mark_notifications_as_read(request):
    Notification.objects.filter(admin=request.user, is_read=0).update(is_read=1)
    return JsonResponse({"success": True})
    

def send_allocation_notifications(request):
    current_date = datetime.now().date()

    allocations = EquipmentAllocation.objects.filter(end_datetime__date__gte=current_date)

    for allocation in allocations:
        if allocation.end_datetime.date() >= current_date:
            if allocation.manager is not None:
                admin_user_manager = allocation.manager.admin
                notification_manager = Notification(
                    admin=admin_user_manager, 
                    message = "Equipment allocation {} for {} ends at {}.".format(allocation.equipment.name, allocation.allocator.fullname, allocation.end_datetime.time()),
                    is_read=0
                )
                notification_manager.save()

            if allocation.allocator is not None:
                admin_user_allocator = allocation.allocator.admin
                notification_allocator = Notification(
                    admin=admin_user_allocator,
                    message = "Your allocation of equipment {} ends at {}.".format(allocation.equipment.name, allocation.end_datetime.strftime('%Y-%m-%d %H:%M')),
                    is_read=0
                )
                notification_allocator.save()
                return HttpResponse("Allocation completion notifications sent successfully.")
            return HttpResponse("no notifications sent")
        return HttpResponse("no notifications notifications sent")




    



