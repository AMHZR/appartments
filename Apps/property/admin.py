__author__ = 'aamirhussain'

from django.contrib import admin
from models import *
from django.forms import ModelForm

from propertyusers.models import property_owners
from propertyusers.models import company_properties
from propertyusers.models import user

class AmenitiesInline(admin.StackedInline):
    model = amenities
    extra = 1
    verbose_name = 'Amenity'
    verbose_name_plural = 'Amenities'


class CompanyUsersInline(admin.StackedInline):
    model = property_owners
    extra = 1
    verbose_name = 'Property User'
    verbose_name_plural = 'Property Users'

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'user':
            print '^'*100
            print user.objects.filter(created_by = request.user)
            kwargs['queryset'] = user.objects.filter(created_by = request.user)
#            self.fields['user'].queryset = user.objects.filter(created_by = request.user)
        else:
            pass
        return super(CompanyUsersInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class PropertyAdmin(admin.ModelAdmin):
    search_fields = ['name','title']
    list_display = ('name','title')
    inlines = [CompanyUsersInline,AmenitiesInline]

#    prepopulated_fields = {"title": ("name",)}

#    def company_users(self,obj):
#        user =  self

    fieldsets = [
            (None,{'fields':('name','title')}),
#            ('Owner',{'fields':('belongs_to','who_can_edit')}),
            ('Property Details',{'fields':(('min_bathrooms','max_bathrooms'),('min_rooms','max_rooms'),'started_on')}),
            ('Property Value',{'fields':(('min_price','max_price'))}),
            ('Address',{'fields':('address1','address2',('city','state','zip'))}),
            ('Additional Details',{'fields':('description','website','facebook','twitter','phone_office')}),
        ]


    def company_user(self,request):
        user_company = request.user.company_users_set.all()
        if user_company:
            return True
        return False

    def company_admin(self,request):
        user_company = request.user.company_account_set.all()
        if user_company:
            return user_company
        return False

    def queryset(self, request):
        qs = super(PropertyAdmin, self).queryset(request)

        if request.user.is_superuser:
            return qs

        if self.company_admin(request):
            user_properties  = self.company_admin(request)
            company = user_properties[0]
            properties = company.company_properties_set.all().values_list('property')
            print '#'*100
            print qs.filter(pk__in=properties)
            return qs.filter(pk__in=properties)
        else:
            print 'Yupeee i am aa property owner'
            user_properties = request.user.property_owners_set.all()
            properties = user_properties.values_list('property')
            print '*'*100
            print qs.filter(pk__in=properties)
            return qs.filter(pk__in=properties)

    def save_model(self, request, obj, form, change):
        obj.save()

        if self.company_admin(request) and not change:
            user    = request.user
            company = self.company_admin(request)[0]
            company_property = company_properties()
            company_property.property = obj
            company_property.company  = company
            company_property.save()
        elif not request.user.is_superuser and not change:
            user = request.user
            user_property = property_owners()
            user_property.property = obj
            user_property.user = user
            user_property.save()



admin.site.register(properties,PropertyAdmin)

