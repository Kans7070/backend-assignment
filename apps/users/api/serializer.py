from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','age','company_name','city','state','web','password','zip']
        extra_kwargs = {
            'password':{'write_only':True},
        }
    def update_user(self,data):
        for key in data.keys():
            if key == 'password':
                try:
                    self.instance.set_password(data['password'])
                except:
                    pass
            else:
                try:
                    self.instance.__dict__[key] = data[key]
                except:
                    pass
        self.instance.save()