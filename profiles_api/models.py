from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    # Used to manipulate objects of UserProfile type
    def create_user(self, email, name, password=None):
        """creates a user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        # normalizing an email takes the email provider and lowers it. BP
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)  # to encrypt the set_password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user profile"""
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True    # Part of PermissionsMixin
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    name = models.CharField(max_length=255)
    email =models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)  # So when it's created is act
    is_staff = models.BooleanField(default=False)

     # because we'll replace the default name with email
    objects = UserProfileManager()

    # Minimum required fiedls
    USERNAME_FIELD = 'email'    # overrides defaul field with our email
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Returns the string representation of the user model"""
        # this is not mandatory but recomended for django models
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    # - You need foreign keys to link one model to another
    # - Use AUTH_USER_MODEL to ensure that if the data changes,
    # only the settings need to be changed
    # - on_delete=models.CASCADE, if user is deleted, so are the feed items
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
