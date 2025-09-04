
# from django.urls import include, path
# from equipmentmanagementsystem import views, adminhodviews, managerhodviews, allocatorhodviews

# app_name = "equipmentmanagementsystem"

# urlpatterns = [

    
# #     path('demo/', views.showDemoPage, name="demo "),
#     # path('get_user_details', views.GetUserDetails , name='getuserdetails'),
#     path('logout', views.logOut, name="logout"),
#     #path('dologin', views.dologin, name="dologin"),
#     path('admin_home', adminhodviews.showAdminPage, name="admin_home"),
    
#     path('add_category', adminhodviews.addCategory, name="add_category"),
#     path('add_inventory', adminhodviews.addNewInventory, name="add_inventory"),
#     path('add_room', adminhodviews.addRoom, name="add_room"),
#     path('add_manager', adminhodviews.addManager, name="add_manager"),
#     path('save_add_manager', adminhodviews.saveAddManager, name="save_add_manager"),
#     path('save_add_category', adminhodviews.saveAddCategory, name="save_add_category"),
# #     path('save_add_inventory', adminhodviews.saveAddInventory, name="save_add_inventory"),
#     path('save_add_room', adminhodviews.saveAddRoom, name="save_add_room"),
#     path('add_equipment', managerhodviews.addEquipment, name="add_equipment"),
#     path('add_allocator', managerhodviews.addAllocator, name="add_allocator"),
#     path('save_add_equipment', managerhodviews.saveAddEquipment, name="save_add_equipment"),
#     path('save_add_allocator', managerhodviews.saveAddAllocator, name="save_add_allocator"),
#     path('view_manager', adminhodviews.viewManager, name="view_manager"),
#     path('view_categories', adminhodviews.viewCategory, name="view_categories"),
# #     path('view_inventories', adminhodviews.viewInventories, name="view_inventories"),
#     path('search_inventory', adminhodviews.searchInventory, name='search_inventory'),
# #     path('filter_inventory', adminhodviews.filterInventory, name='filter_inventory'),
# #     path('view_inventory/<str:inventory_id>', adminhodviews.viewInventory, name="view_inventory"),
# #     path('view_inventory_template', adminhodviews.viewInventoryTemplate, name="view_inventory_template"),
#     path('add_new_inventory', adminhodviews.addNewInventory, name="add_new_inventory"),
#     # path('export_inventory', adminhodviews.exportInventory, name="export_inventory"),
# #     path('equipment_planning_management/', managerhodviews.equipment_planning_management, name='equipment_planning_management'),
# #     path('create_plan/<int:equipment_id>/', managerhodviews.create_plan, name='create_plan'),
#     #path('plan_detail/<int:plan_id>/', managerhodviews.plan_detail, name='plan_detail'),
# #     path('restore_inventory', adminhodviews.restoreInventory, name="restore_inventory"),
#     path('view_rooms', adminhodviews.viewRoom, name="view_rooms"),
# #     path('inventory_save_form', adminhodviews.save_form, name="inventory_save_form"),
# #     path('save_inventory_submit', adminhodviews.save_inventory_submit, name="save_inventory_submit"),
#     path('view_allocator', managerhodviews.viewAllocator, name="view_allocator"),
#     path('view_equipment', managerhodviews.viewEquipment, name="view_equipment"),
#     path('edit_category/<str:category_id>', adminhodviews.editCategory, name="edit_category"),
#     path('edit_room/<str:room_id>', adminhodviews.editRoom, name="edit_room"),
#     path('edit_manager/<str:manager_id>', adminhodviews.editManager, name="edit_manager"),
#     path('save_edit_manager', adminhodviews.saveEditManager, name="save_edit_manager"),
#     path('save_edit_category', adminhodviews.saveEditCategory, name="save_edit_category"),
#     path('save_edit_room', adminhodviews.saveEditRoom, name="save_edit_room"),
#     path('edit_equipment/<str:equipment_id>', managerhodviews.editEquipment, name="edit_equipment"),
#     path('edit_allocator/<str:allocator_id>', managerhodviews.editAllocator, name="edit_allocator"),
#     path('save_edit_allocator', managerhodviews.saveEditAllocator, name="save_edit_allocator"),
#     path('save_edit_equipment', managerhodviews.saveEditEquipment, name="save_edit_equipment"),
#     path('delete_category/<int:category_id>', adminhodviews.deleteCategory, name="delete_category"),
# #     path('delete_inventory/<int:inventory_id>', adminhodviews.deleteInventory, name="delete_inventory"),
#     path('delete_room/<int:room_id>', adminhodviews.deleteRoom, name="delete_room"),
#     path('delete_manager/<int:manager_id>', adminhodviews.deleteManager, name="delete_manager"),
#     path('delete_equipment/<int:equipment_id>', managerhodviews.deleteEquipment,
#          name="delete_equipment"),
#     path('delete_allocator/<int:allocator_id>', managerhodviews.deleteAllocator,
#          name="delete_allocator"),
# #     path('allocator_home', allocatorhodviews.showAllocatorPage, name="allocator_home"),
# #                       path('demo', views.showDemoPage, name="demo"),
#     path('', views.showLoginPage, name="show_login"),
#     path('doLogin', views.doLogin, name="doLogin"),
#     path('get_user_details', views.GetUserDetails),
#     path('logout_user', views.logout_user, name="logout"),
#     path('signup/', views.signaction, name='signaction'),
#     path('manager_home', managerhodviews.showManagerPage, name="manager_home"),
#     path('admin_profile', adminhodviews.admin_profile,name="admin_profile"),
#     path('admin_profile_save', adminhodviews.admin_profile_save,name="admin_profile_save"),
#     path('manager_profile', managerhodviews.manager_profile,name="manager_profile"),
#     path('manager_profile_save', managerhodviews.manager_profile_save,name="manager_profile_save"),

#                   # path('signup_student',views.signup_student,name="signup_student"),
#                   # path('do_researcher_signup',views.do_researcher_signup,name="do_researcher_signup"),
#                   # path('signup_researcher',views.signup_researcher,name="signup_researcher"),
# ]



from django.urls import path
from equipmentmanagementsystem import views, adminhodviews, managerhodviews, researcherhodviews, studenthodviews
from django.urls import include

app_name = "equipmentmanagementsystem"

urlpatterns = [

    
    
    path('logout', views.logOut, name="logout"),
    path('', views.showLoginPage, name="show_login"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout_user"),
    path('admin_home', adminhodviews.showAdminPage, name="admin_home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('researcher_home', researcherhodviews.showResearcherPage, name="researcher_home"),
    path('signaction/', views.signaction, name="signaction"),
    #path('equipment_planning/<int:equipment_id>/', managerhodviews.equipment_planning, name='equipment_planning'),
    #path('equipment_list/', managerhodviews.equipment_list, name='equipment_list'),
    #path('equipment_planning_list/', managerhodviews.equipment_planning_list, name='equipment_planning_list'),
    #path('set_equipment_availability', managerhodviews.set_equipment_availability, name='set_equipment_availability'),
    path('manager_home', managerhodviews.showManagerPage, name="manager_home"),
    path('student_home', studenthodviews.showStudentPage, name="student_home"),
    # path('researcher_home', allocatorhodviews.showResearcherPage, name="researcher_home"),
    path('add_category', adminhodviews.addCategory, name="add_category"),
    #path('add_inventory', adminhodviews.addInventory, name="add_inventory"),
    path('add_room', adminhodviews.addRoom, name="add_room"),
    path('add_manager', adminhodviews.addManager, name="add_manager"),
    path('save_add_manager', adminhodviews.saveAddManager, name="save_add_manager"),
    path('save_add_category', adminhodviews.saveAddCategory, name="save_add_category"),
    #path('save_add_inventory', adminhodviews.saveAddInventory, name="save_add_inventory"),
    path('save_add_room', adminhodviews.saveAddRoom, name="save_add_room"),
    path('manager_home', managerhodviews.showManagerPage, name="manager_home"),
    path('add_equipment', managerhodviews.addEquipment, name="add_equipment"),
    path('add_allocator', managerhodviews.addAllocator, name="add_allocator"),
    path('save_add_equipment', managerhodviews.saveAddEquipment, name="save_add_equipment"),
    path('save_add_allocator', managerhodviews.saveAddAllocator, name="save_add_allocator"),
    path('view_manager', adminhodviews.viewManager, name="view_manager"),
#     path('view_categories', adminhodviews.viewCategory, name="view_categories"),
    #path('view_inventories', adminhodviews.viewInventories, name="view_inventories"),
    path('search_inventory', adminhodviews.searchInventory, name='search_inventory'),
    #path('filter_inventory', adminhodviews.filterInventory, name='filter_inventory'),
    #path('view_inventory/<str:inventory_id>', adminhodviews.viewInventory, name="view_inventory"),
    #path('view_inventory_template', adminhodviews.viewInventoryTemplate, name="view_inventory_template"),
    path('add_new_inventory', adminhodviews.addNewInventory, name="add_new_inventory"),
    path('export_inventory', adminhodviews.exportInventory, name="export_inventory"),
    #path('equipment_planning_management/', managerhodviews.equipment_planning_management, name='equipment_planning_management'),
    #path('create_plan/<int:equipment_id>/', managerhodviews.create_plan, name='create_plan'),
    #path('plan_detail/<int:plan_id>/', managerhodviews.plan_detail, name='plan_detail'),
    #path('restore_inventory', adminhodviews.restoreInventory, name="restore_inventory"),
    path('view_rooms', adminhodviews.viewRoom, name="view_rooms"),
    #path('inventory_save_form', adminhodviews.save_form, name="inventory_save_form"),
    #path('save_inventory_submit', adminhodviews.save_inventory_submit, name="save_inventory_submit"),
    path('view_allocator', managerhodviews.viewAllocator, name="view_allocator"),
    path('view_equipment', managerhodviews.viewEquipment, name="view_equipment"),
    path('edit_category/<str:category_id>', adminhodviews.editCategory, name="edit_category"),
    path('edit_room/<str:room_id>', adminhodviews.editRoom, name="edit_room"),
    path('edit_manager/<str:manager_id>', adminhodviews.editManager, name="edit_manager"),
    path('save_edit_manager', adminhodviews.saveEditManager, name="save_edit_manager"),
    path('save_edit_category', adminhodviews.saveEditCategory, name="save_edit_category"),
    path('save_edit_room', adminhodviews.saveEditRoom, name="save_edit_room"),
    path('edit_equipment/<str:equipment_id>', managerhodviews.editEquipment, name="edit_equipment"),
    path('edit_allocator/<str:allocator_id>', managerhodviews.editAllocator, name="edit_allocator"),
    path('save_edit_allocator', managerhodviews.saveEditAllocator, name="save_edit_allocator"),
    path('save_edit_equipment', managerhodviews.saveEditEquipment, name="save_edit_equipment"),
   path('delete_category/<int:category_id>/', adminhodviews.deleteCategory, name="delete_category"),
    #path('delete_inventory/<int:inventory_id>', adminhodviews.deleteInventory, name="delete_inventory"),
    path('delete_room/<int:room_id>', adminhodviews.deleteRoom, name="delete_room"),
    path('delete_manager/<int:manager_id>', adminhodviews.deleteManager, name="delete_manager"),
    path('delete_equipment/<int:equipment_id>', managerhodviews.deleteEquipment,
         name="delete_equipment"),
    path('delete_allocator/<int:allocator_id>', managerhodviews.deleteAllocator,
         name="delete_allocator"),
    #path('allocator_home', allocatorhodviews.showAllocatorPage, name="allocator_home"),
                     
    
    path('manager_home', managerhodviews.showManagerPage, name="manager_home"),
    path('admin_profile', adminhodviews.admin_profile,name="admin_profile"),
    path('admin_profile_save', adminhodviews.admin_profile_save,name="admin_profile_save"),
    path('manager_profile', managerhodviews.manager_profile,name="manager_profile"),
    path('manager_profile_save', managerhodviews.manager_profile_save,name="manager_profile_save"),
    path('researcher_profile', researcherhodviews.researcher_profile,name="researcher_profile"),
    path('researcher_profile_save', researcherhodviews.researcher_profile_save,name="researcher_profile_save"),
    path('student_profile', studenthodviews.student_profile,name="student_profile"),
    path('student_profile_save', studenthodviews.student_profile_save,name="student_profile_save"),
    #path('equipment_list', managerhodviews.equipment_list,name="equipment_list"),
    #path('create_equipment_planning', managerhodviews.create_equipment_planning,name="create_equipment_planning"),
    #path('signup_student',views.signup_student,name="signup_student"),
    #path('do_researcher_signup',views.do_researcher_signup,name="do_researcher_signup"),
    #path('signup_researcher',views.signup_researcher,name="signup_researcher"),

    path('view_manager', adminhodviews.viewManager, name="view_manager"),
    path('view_category', adminhodviews.viewCategory, name="view_category"),
    path('view_managers', adminhodviews.viewManagers, name="view_managers"),
    path('view_categories', adminhodviews.viewCategories, name="view_categories"),
    path('view_allocators', adminhodviews.viewAllocators, name="view_allocators"),
    path('view_equipments', adminhodviews.viewEquipments, name="view_equipments"),


    path('view_equipment_planning', managerhodviews.viewEquipmentPlanning, name="view_equipment_planning"),
    path('add_equipment_planning', managerhodviews.add_equipment_planning, name="add_equipment_planning"),
    path('edit_equipment_planning/<str:equipment_planning_id>', managerhodviews.editEquipmentPlanning, name="edit_equipment_planning"),
    path('edit_equipment_allocation/<str:equipment_allocation_id>', managerhodviews.editAllocation, name="edit_equipment_allocation"),
    path('save_edit_equipment_allocation', managerhodviews.saveEditEquipmentAllocation, name="save_edit_equipment_allocation"),
    path('save_edit_equipment_planning', managerhodviews.saveEditEquipmentPlanning, name="save_edit_equipment_planning"),
    path('delete_equipment_planning/<int:equipment_planning_id>', managerhodviews.deleteEquipmentPlanning,name="delete_equipment_planning"),
    path('delete_allocation/<int:equipment_allocation_id>', managerhodviews.deleteAllocation,name="delete_allocation"),
    path('view_allocations', managerhodviews.viewAllocation, name="view_allocations"),   
    path('add_allocation', managerhodviews.addAllocation, name="add_allocation"),     
    path('send_allocation_notification', managerhodviews.send_allocation_notification_from_manager,name="send_allocation_notification"),
    path('edit_allocation/<str:equipment_allocation_id>/', managerhodviews.editAllocation, name="edit_allocation"),
    
    path('send_allocation_notification', studenthodviews.send_allocation_notification,name="send_allocation_notification"),
    path('send_allocation_notification', researcherhodviews.send_allocation_notification,name="send_allocation_notification"),
    path('allocate_equipment_student', studenthodviews.allocate_equipment_student, name="allocate_equipment_student"),
    path('allocate_equipment_researcher', researcherhodviews.allocate_equipment_researcher, name="allocate_equipment_reseracher"),

    path('view_student_equipment_allocation', studenthodviews.viewStudentEquipmentAllocation, name="view_student_equipment_allocation"),
    path('view_researcher_equipment_allocation', researcherhodviews.viewResearcherEquipmentAllocation, name="view_researcher_equipment_allocation"),



    

    path('view_student_equipment_allocation', studenthodviews.viewStudentEquipmentAllocation, name="view_student_equipment_allocation"),
    path('view_researcher_equipment_allocation', researcherhodviews.viewResearcherEquipmentAllocation, name="view_researcher_equipment_allocation"),    
    path('view_students', managerhodviews.viewStudents, name="view_students"),
    path('view_researchers', managerhodviews.viewResearchers, name="view_researchers"),
    path('allocations', managerhodviews.viewAllocations, name="allocations"),
    path('equipments', managerhodviews.viewEquipments, name="equipments"),

     path('view_researcher_HPC_scheduling', researcherhodviews.viewResearchertHPCscheduling, name="view_researcher_HPC_scheduling"),  
     

     path('mark_notifications_as_read/', views.mark_notifications_as_read, name='mark_notifications_as_read'),
     path('get_notifications/', views.get_notifications, name='get_notifications'),
     path('send_allocation_notifications/', views.send_allocation_notifications, name='send_allocation_notifications'),  

     


     path('export_student_allocation', studenthodviews.exportStudentAllocation, name="export_student_allocation"),
     path('export_equipment', managerhodviews.exportEquipment, name="export_equipment"),
     path('export_planning', managerhodviews.exportEquipmentPlanning, name="export_planning"),
     path('export_researcher_allocation', researcherhodviews.exportResearcherAllocation, name="export_researcher_allocation"),


path('equipment/<int:equipment_id>/qr_code/', managerhodviews.generate_qr_code, name='qr_code'),
     path('researcher_about_us', researcherhodviews.showResearcherAboutUsPage, name="researcher_about_us"),   
     path('student_about_us', studenthodviews.showStudentAboutUsPage, name="student_about_us"), 




  
]


