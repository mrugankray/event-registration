from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import os
from rest_framework.response import Response
from rest_framework import status


class Registration(models.Model):
    id = models.AutoField(primary_key=True, unique=True)  # registration id
    full_name = models.CharField(max_length=25, blank=False)
    mobile = PhoneNumberField(blank=False, unique=True, null=False)
    id_card = models.ImageField(upload_to='id_card')
    reg_type = models.CharField(max_length=9)
    num_of_tickets = models.IntegerField()
    reg_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        file_name, ext = os.path.splitext(self.id_card.path)

        accepted_ext = {'.png': True, '.jpeg': True}
        accepted_reg_type = {'self': True, 'group': True, 'corporate': True, 'others': True}
        if accepted_ext.get(ext, False):
            reg_type_lower_case = self.reg_type.lower()
            if accepted_reg_type.get(reg_type_lower_case, False):
                self.reg_type = reg_type_lower_case
                super().save()
            else:
                return Response({
                    "msg": "Registration Type should be of 4 types i.e. Self, Group, Corporate, Others."
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "msg": "Image format should be in png or jpeg format."
            }, status=status.HTTP_400_BAD_REQUEST)
