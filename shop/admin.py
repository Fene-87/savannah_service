from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm, AdminPasswordChangeForm, UserCreationForm
# from shop.forms import CustomAuthenticationForm
# from shop.models import CustomUser
#
#
# class CustomUserAdmin(UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     change_password_form = AdminPasswordChangeForm
#     list_display = ('email', 'is_staff', 'is_superuser')
#     list_filter = ('is_staff', 'is_superuser')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser'),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     login_form = CustomAuthenticationForm
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
