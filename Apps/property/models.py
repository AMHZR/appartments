from django.db import models




class properties (models.Model):

    name             = models.CharField(max_length=150,verbose_name='Project Name')
    title            = models.CharField(max_length=200,verbose_name='Display title')


    min_bathrooms    = models.IntegerField(default=1,verbose_name='Min Number of bathrooms')
    max_bathrooms    = models.IntegerField(default=1,verbose_name='Max Number of bathrooms')

    min_rooms    = models.IntegerField(default=1,verbose_name='Min Number of Rooms')
    max_rooms    = models.IntegerField(default=1,verbose_name='Max Number of Rooms')

    min_price        = models.IntegerField(verbose_name='Min Price')
    max_price        = models.IntegerField(verbose_name='Max Price')

    description      = models.TextField(verbose_name='More About Project')

    address1         = models.CharField(max_length=200,verbose_name='Address1')
    address2         = models.CharField(max_length=200,verbose_name='Address2')
    city             = models.CharField(max_length=30,verbose_name='City')
    state            = models.CharField(max_length=15,verbose_name='State')
    zip              = models.CharField(max_length=20,verbose_name='Zip')

    website          = models.URLField(verbose_name='Official Website')
    facebook         = models.URLField(verbose_name='Official FaceBook Page')
    twitter          = models.URLField(verbose_name='Official Twitter Page')
    phone_office     = models.CharField(max_length=20,verbose_name='Office Phone Number')

    started_on       = models.DateField(verbose_name='Build Date')

    created_on       = models.DateTimeField(auto_now_add=True)

    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name='Property'
        verbose_name_plural = 'Properties'
        get_latest_by = 'created_on'

class amenities(models.Model):
    property = models.ForeignKey(properties,verbose_name='Property Amenity')
    name     = models.CharField(max_length=150,verbose_name='Amenities Name',help_text='e.g Garden,playArea,security etc etc')

    class Meta:
        verbose_name= 'Amenities'
        verbose_name_plural = 'Amenities'
    def __unicode__(self):
        return self.name