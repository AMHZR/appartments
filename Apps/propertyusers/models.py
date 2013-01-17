__author__ = 'aamirhussain'
from django.db import models
from property.models import properties

from django.contrib.admin.models import User


class user(User):
    user_type  = models.CharField(max_length=30,default='Individual_User',verbose_name='User Type')
    created_by = models.ForeignKey(User,related_name='owned by')



class company_account(models.Model):
    company_name   = models.CharField(max_length=100,unique=True)
    description    = models.TextField(blank=True)
    address        = models.TextField(blank=True)
    website        = models.CharField(max_length=100)
    created_date   = models.DateTimeField(auto_now_add=True)
    contact_email  = models.EmailField()
    contact_number = models.CharField(max_length=20)
    company_admin  = models.ForeignKey(user)

    class Meta:
        verbose_name = 'Company Account'
        verbose_name_plural = 'Company Accounts'

    def __unicode__(self):
        return self.company_name


class company_users(models.Model):
    company = models.ForeignKey(company_account)
    users   = models.ForeignKey(user)

    def __unicode__(self):
        return self.users.username

class company_properties(models.Model):
    company  = models.ForeignKey(company_account)
    property = models.ForeignKey(properties)

    def __unicode__(self):
        return self.property.title

class property_owners(models.Model):
    property = models.ForeignKey(properties)
    user = models.ForeignKey(user)
    def __unicode__(self):
        return self.property.title