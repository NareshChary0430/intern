from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
 
# Register your models here.

admin.site.register(Locations)

   
 

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active')
#     ordering = ('email',)
#     search_fields = ('email', 'first_name', 'last_name')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important Dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)
