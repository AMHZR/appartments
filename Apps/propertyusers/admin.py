__author__ = 'aamirhussain'


from django.contrib import admin
from models import *

class UsersInline(admin.StackedInline):
    model = company_users
    extra = 1
    verbose_name='Company User'
    verbose_name_plural = 'Company Users'

class CompanyUsersInline(admin.StackedInline):
    model = user
    extra = 1
    verbose_name = 'Property Company'
    verbose_name_plural = 'Property Companies'

class CompanyAdmin(admin.ModelAdmin):
    inlines = [UsersInline]
admin.site.register(company_account,CompanyAdmin)

class UserAdmin(admin.ModelAdmin):
    exclude = ['created_by']

    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        qs= self.model.objects.filter(created_by=request.user)
        return qs


    def save_model(self, request, obj, form, change):
        if not change:
            user = request.user
            obj.created_by = user
        obj.save()


admin.site.register(user,UserAdmin)

class CompanyPropertiesAdmin(admin.ModelAdmin):
    pass
admin.site.register(company_properties,CompanyPropertiesAdmin)

#class PropertyOwnersAdmin(admin.ModelAdmin):
##    inlines = [CompanyUsersInline]
#    pass
#admin.site.register(property_owners,PropertyOwnersAdmin)