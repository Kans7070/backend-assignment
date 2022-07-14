from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, company_name, age, city, state, zip, email, web, password):
        if not first_name:
            raise ValueError('name must be provided')

        if not email:
            raise ValueError('email must be provided')

        if not password:
            raise ValueError('password must be provided')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            age=age,
            city=city,
            state=state,
            zip=zip,
            email=email,
            web=web,
        )
        user.set_password(password)
        user.is_staff = False
        user.save()
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            return ValueError('Password must be provided')
        admin = self.model(
            email=email,
        )
        admin.set_password(password)
        admin.is_staff = True
        admin.save()
        return admin
