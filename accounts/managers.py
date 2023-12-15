from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """ make users
    Args:
    BaseUserManager (_type_): _description_
    """

    def create_user(self, phone_number, password, **extra_fields):
        """
        create normal user
        """
        if not phone_number:
            raise ValueError('user must have phone number')
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        user =  self.create_user(phone_number, password, **extra_fields)
        return user


