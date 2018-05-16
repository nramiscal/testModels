# from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Owner(models.Model):
    fname = models.CharField(max_length = 255)
    lname = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<Owner: {}|{} {}>".format(self.id, self.fname, self.lname)

class Pet(models.Model):
    name = models.CharField(max_length = 255)
    breed = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(Owner, related_name="pets")

    def __repr__(self):
        return "<Pet: {}|{} {}>".format(self.id, self.name, self.breed)
