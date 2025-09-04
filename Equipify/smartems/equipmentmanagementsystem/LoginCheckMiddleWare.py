# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.utils.deprecation import MiddlewareMixin



# class LoginCheckMiddleWare(MiddlewareMixin):

#     def process_view(self,request,view_func,view_args,view_kwargs):
#         modulename=view_func.__module__
#         user=request.user
#         if user.is_authenticated:
#             if user.user_type == "1":
#                 if modulename == "equipmentmanagementsystem.adminhodviews":
#                     pass
#                 elif modulename == "equipmentmanagementsystem.views":
#                     pass
#                 else:
#                     return HttpResponseRedirect(reverse("equipmentmanagementsystem:admin_home"))
#             elif user.user_type == "2":
#                 if modulename == "equipmentmanagementsystem.managerhodviews":
#                     pass
#                 elif modulename == "equipmentmanagementsystem.views":
#                     pass
#                 else:
#                     return HttpResponseRedirect(reverse("equipmentmanagementsystem:manager_home"))
#             elif user.user_type == "3":
#                 if user.allocatorhod.role == "researcher":
#                     if modulename == "equipmentmanagementsystem.researcherhodviews":
#                         pass
#                     elif modulename == "equipmentmanagementsystem.views":
#                         pass
#                     else:
#                         return HttpResponseRedirect(reverse("equipmentmanagementsystem:researcher_home"))
#                 elif user.allocatorhod.role == "student":
#                     if modulename == "equipmentmanagementsystem.studenthodviews":
#                         pass
#                     elif modulename == "equipmentmanagementsystem.views":
#                         pass
#                     else:
#                         return HttpResponseRedirect(reverse("equipmentmanagementsystem:student_home"))
#                 else:
#                     return HttpResponseRedirect(reverse("equipmentmanagementsystem:show_login"))
            
#         else:
#             if request.path == reverse("equipmentmanagementsystem:show_login") or request.path == reverse("equipmentmanagementsystem:doLogin") or modulename == "django.contrib.auth.views":
#                 pass
#             else:
#                 return HttpResponseRedirect(reverse("equipmentmanagementsystem:show_login"))



from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "equipmentmanagementsystem.adminhodviews":
                    pass
                elif modulename == "equipmentmanagementsystem.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("equipmentmanagementsystem:admin_home"))
            elif user.user_type == "2":
                if modulename == "equipmentmanagementsystem.managerhodviews":
                    pass
                elif modulename == "equipmentmanagementsystem.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("equipmentmanagementsystem:manager_home"))
            elif user.user_type == "3":
                if user.allocatorhod.role == "researcher":
                    if modulename == "equipmentmanagementsystem.researcherhodviews":
                        pass
                    elif modulename == "equipmentmanagementsystem.views":
                        pass
                    else:
                        return HttpResponseRedirect(reverse("equipmentmanagementsystem:researcher_home"))
                elif user.allocatorhod.role == "student":
                    if modulename == "equipmentmanagementsystem.studenthodviews":
                        pass
                    elif modulename == "equipmentmanagementsystem.views":
                        pass
                    else:
                        return HttpResponseRedirect(reverse("equipmentmanagementsystem:student_home"))
                else:
                    return HttpResponseRedirect(reverse("equipmentmanagementsystem:show_login"))
        else:
            if request.path == reverse("equipmentmanagementsystem:show_login") or request.path == reverse("equipmentmanagementsystem:doLogin") or request.path == reverse("equipmentmanagementsystem:signaction") or modulename == "django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("equipmentmanagementsystem:show_login"))
        
   
        
                        
        

        