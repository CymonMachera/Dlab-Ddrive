from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
        def create_user(self, email, first_name, last_name,designation, password):
            if not email:
                raise ValueError('user Must have an email')
            if not first_name:
                raise ValueError('User must have first name')
            if not last_name:
                raise ValueError('User Must have lasr name')

            user = self.model(
                email = self.normalize_email(email=email),
                first_name = first_name,
                last_name = last_name,
                designation = designation
            )
            user.set_password(raw_password=password)  
            user.save(using=self._db)     

            return user
        def create_superuser(self, email, first_name, last_name, password):
            user = self.create_user(
                email = email,
                first_name = first_name,
                last_name = last_name,
                password = password,
            )
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
        

            user.save(using=self._db)

            return user
    