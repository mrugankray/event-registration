from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Registration(models.Model):
    id = models.AutoField(primary_key=True, unique=True)  # registration id
    mobile = PhoneNumberField(blank=False, unique=True, null=False)
    id_card = models.ImageField(default='default.png', upload_to='id_card')
    reg_type = models.CharField(max_length=9)
    num_of_tickets = models.IntegerField()
    reg_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
