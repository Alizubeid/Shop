from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CreateUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("email not validated")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(blank=True, default=timezone.now)
    date_login = models.DateTimeField(null=True)
    USERNAME_FIELD = "email"
    EMIAL_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CreateUserManager()


class Profile(models.Model):
    """
    any User can have profile details
    """

    class Demography:
        """
        people category
        """

        class AgeCategory(models.TextChoices):
            A = "A", "3 to 7"
            B = "B", "7 to 12"
            C = "C", "12 to 18"
            D = "D", "18 to 30"
            E = "E", "30 to 40"
            F = "F", "40 to 60"
            G = "G", "+60"

        class Gender(models.TextChoices):
            M = "M", "Male"
            F = "F", "Female"

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=13)
    birth = models.DateField()
    gender = models.CharField(choices=Demography.Gender.choices, max_length=1)

    @property
    def age(self):
        return timezone.now().year - self.birth.year

    @property
    def age_category_checker(self, categoires=Demography.AgeCategory):
        age = self.age
        if 3 >= age > 7:
            return categoires.A
        elif 7 >= age > 12:
            return categoires.B
        elif 12 >= age > 18:
            return categoires.C
        elif 18 >= age > 30:
            return categoires.D
        elif 30 >= age > 40:
            return categoires.E
        elif 40 >= age > 60:
            return categoires.F
        elif 60 > age:
            return categoires.G

    age_category = models.CharField(
        max_length=1,
        choices=Demography.AgeCategory.choices,
        default=age_category_checker,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)


class Address(models.Model):
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    zip_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
