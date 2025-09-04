# """smartems URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # from django.conf.urls.static import static
# # from smartems import settings
# # from django.contrib import admin
# # from django.urls import path, include
# # from equipmentmanagementsystem import views
# # from equipmentmanagementsystem import managerhodviews
# # from equipmentmanagementsystem import adminhodviews

# # from django.urls import path, include
# # from django.contrib.auth import views as auth_views

# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
# from equipmentmanagementsystem import views, managerhodviews, adminhodviews
# from smartems import settings
# from equipmentmanagementsystem import views
# from equipmentmanagementsystem.views import signaction
# urlpatterns = [
#                   path("", include('equipmentmanagementsystem.urls', namespace='equipmentmanagementsystem')),
#                   path('admin/', admin.site.urls),
#                   path('manager_home', managerhodviews.showManagerPage, name="manager_home"),
#                   path('manager_profile', managerhodviews.manager_profile,name="manager_profile"),
#                   path('manager_profile_save', managerhodviews.manager_profile_save,name="manager_profile_save"),
                  
#                   path('admin_profile', adminhodviews.admin_profile,name="admin_profile"),
#                   path('admin_profile_save', adminhodviews.admin_profile_save,name="admin_profile_save"),
#                 #   path('accounts/', include('django.contrib.auth.urls')),
#                  path('export_inventory', adminhodviews.exportInventory, name="export_inventory"),

#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
#                                                                                          document_root=settings.STATIC_ROOT)



"""smartems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from smartems import settings
from django.contrib import admin
from django.urls import path, include
from equipmentmanagementsystem import views
from equipmentmanagementsystem import managerhodviews


urlpatterns = [
                  path("", include('equipmentmanagementsystem.urls', namespace='equipmentmanagementsystem')),
                  path('admin/', admin.site.urls),
                # path('equipment/<int:pk>/qr_code/', managerhodviews.generate_qr_code, name='qr_code'),
                  path('equipment/<int:pk>/qr_code/', managerhodviews.generate_qr_code, name='qr_code'),
              
                 
                path('accounts/',include('django.contrib.auth.urls')),
             
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)

