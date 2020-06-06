from rest_framework import serializers
from .models import Registration
import os


class RegistrationSerializer(serializers.ModelSerializer):
    def validate(self, data):
        file_name, ext = os.path.splitext(str(data['id_card']))
        print(ext)

        accepted_ext = {'.png': True, '.jpeg': True}
        accepted_reg_type = {'self': True, 'group': True, 'corporate': True, 'others': True}

        reg_type_lower_case = data['reg_type'].lower()
        if accepted_reg_type.get(reg_type_lower_case, False):
            data['reg_type'] = reg_type_lower_case
            if accepted_ext.get(ext, False):
                return data
            else:
                raise serializers.ValidationError("Image format should be in png or jpeg format.")
        else:
            raise serializers.ValidationError("Registration Type should be of 4 types i.e. Self, Group"
                                              ", Corporate, Others.")

    class Meta:
        model = Registration
        fields = '__all__'
