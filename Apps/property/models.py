from django.db import models
from django.contrib.auth.models import User

class localities(models.Model):
    name = models.CharField(max_length=150,verbose_name='Locality Name')
    class Meta:
        verbose_name= 'Locality'
        verbose_name_plural = 'Localities'
    def __unicode__(self):
        return  self.name

class parking(models.Model):
    type             = models.CharField(max_length=100,verbose_name='For Vehical Type')
    how_many         = models.IntegerField(default=1,verbose_name='How Many')
    parking_type     = models.CharField(max_length=20,verbose_name='Parking Type',help_text='e.g shared.uncovered etc etc')

    class Meta:
        verbose_name= 'Parking'
        verbose_name_plural = 'Parking'

    def __unicode__(self):
        return  self.type

class amenities(models.Model):
    name             = models.CharField(max_length=150,verbose_name='Amenities Name',help_text='e.g Garden,playArea,security etc etc')

    class Meta:
        verbose_name= 'Amenities'
        verbose_name_plural = 'Amenities'
    def __unicode__(self):
        return self.name

class contacts(models.Model):
    name             = models.CharField(max_length=150,verbose_name='Contact Name')
    contact_person   = models.CharField(max_length=100,verbose_name='Contact Person')
    phone_office     = models.CharField(max_length=20,verbose_name='Office Phone Number')
    website          = models.URLField(verbose_name='Official Website')
    facebook         = models.URLField(verbose_name='Official FaceBook Page')
    twitter          = models.URLField(verbose_name='Official Twitter Page')
    office_hours     = models.CharField(max_length=100,verbose_name='Office Hours')#Denormalize it

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name= 'Contact'
        verbose_name_plural = 'Contacts'

class projects(models.Model):
    name             = models.CharField(max_length=150,verbose_name='Project Name')
    title            = models.CharField(max_length=200,verbose_name='Display title')


    floor_plans      = models.CharField(max_length=150,verbose_name='Floor Plan images')#Put it in gallery
    min_bathrooms    = models.IntegerField(default=1,verbose_name='Min Number of bathrooms')
    max_bathrooms    = models.IntegerField(default=1,verbose_name='Max Number of bathrooms')
    min_price        = models.IntegerField(verbose_name='Min Price')
    max_price        = models.IntegerField(verbose_name='Max Price')

    description      = models.TextField(verbose_name='More About Project')
    amenities        = models.ManyToManyField(amenities,verbose_name='Amenities of project')

    contacts         = models.ForeignKey(contacts,verbose_name='Contacts For Properties')


    address1         = models.CharField(max_length=200,verbose_name='Address1')
    address2         = models.CharField(max_length=200,verbose_name='Address2')
    city             = models.CharField(max_length=30,verbose_name='City')
    state            = models.CharField(max_length=15,verbose_name='State')
    zip              = models.CharField(max_length=20,verbose_name='Zip')



    started_on       = models.DateField(verbose_name='Project Stated Date')
    created_on       = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name='Project'
        get_latest_by = 'created_on'


class property(models.Model):

    name             = models.CharField(max_length=150,verbose_name='Property Name')
    title            = models.CharField(max_length=200,verbose_name='Display Tite')
    available_from   = models.DateField(blank=True,verbose_name='Available From')

    sale_type        = models.CharField(max_length=20,verbose_name='Sale Type',help_text='E.g New,Resale etc etc')
    constructed_on   = models.DateField(verbose_name='Property Constructed Date')
    project_name     = models.ForeignKey(projects,verbose_name='Project Name',blank=True,null=True)
    locality         = models.ForeignKey(localities,verbose_name='Property Localitys')

    bath_no          = models.IntegerField(default=1,verbose_name='Number Of Bathrooms')
    room_no          = models.IntegerField(default=1,verbose_name='Number Of Rooms')
    built_up_area    = models.CharField(max_length=100,verbose_name='Build Up Area')
    carpet_area      = models.CharField(max_length=100,verbose_name='Carpet Area')
    on_floor         = models.CharField(max_length=20,verbose_name='Property on which Floor')
    balconies        = models.IntegerField(default=0,verbose_name='Balconies/Sitouts')
    parking          = models.ForeignKey(parking,verbose_name="Parking's for this property")
    direction_facing = models.CharField(max_length=30,verbose_name='Directions Facing')
    flooring         = models.CharField(max_length=100,verbose_name='Flooring',help_text='e.g Tilled,Wooden ')
    owner_ship       = models.CharField(max_length=50,verbose_name='Owner Ship Type')
    address          = models.TextField(verbose_name='Address')
    description      = models.TextField(verbose_name='Description of property')
    value            = models.FloatField(verbose_name='Property Value',help_text='e.g 1000,2000,3000')
    negotiable       = models.NullBooleanField(default=False,verbose_name='Price Negotiable')

    credit_score     = models.FloatField(verbose_name='Credit Score for property')

    posted_on        = models.DateTimeField(auto_now_add=True,verbose_name='Created Date')
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Properties'
        verbose_name='Property'