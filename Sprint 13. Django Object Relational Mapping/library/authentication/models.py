from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
import pytz
import datetime
from django.core.validators import EmailValidator

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)


class CustomUser(AbstractBaseUser):
    """
        This class represents a basic user. \n
        Attributes:
        -----------
        param first_name: Describes first name of the user
        type first_name: str max length=20
        param last_name: Describes last name of the user
        type last_name: str max length=20
        param middle_name: Describes middle name of the user
        type middle_name: str max length=20
        param email: Describes the email of the user
        type email: str, unique, max length=100
        param password: Describes the password of the user
        type password: str
        param created_at: Describes the date when the user was created. Can't be changed.
        type created_at: int (timestamp)
        param updated_at: Describes the date when the user was modified
        type updated_at: int (timestamp)
        param role: user role, default role (0, 'visitor')
        type updated_at: int (choices)
        param is_active: user role, default value False
        type updated_at: bool

    """
    # primary_key=True, unique=True
    id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(default = None, max_length=20)
    last_name = models.CharField(default = None, max_length=20)
    middle_name = models.CharField(default = None, max_length=20)
    email = models.EmailField(default = None, unique=True, max_length=100)
    password = models.CharField(default = None, max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.PositiveSmallIntegerField(default=0, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at,
                 user role, user is_active
        """
        s=(self.created_at - datetime.datetime(1970,1,1, tzinfo=pytz.utc)).total_seconds()
        d=(self.updated_at - datetime.datetime(1970,1,1, tzinfo=pytz.utc)).total_seconds()
        
        upd = ('%f' % d).rstrip('0').rstrip('.')
        cre = ('%f' % s).rstrip('0').rstrip('.')
        return f"'id': {self.id}, 'first_name': '{self.first_name}', 'middle_name': '{self.middle_name}', 'last_name': '{self.last_name}', 'email': '{self.email}', 'created_at': {cre}, 'updated_at': {upd}, 'role': {self.role}, 'is_active': {self.is_active}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of CustomUser object.
        :return: class, id
        """
        return '{}(id={})'.format('CustomUser', self.id)
    @staticmethod
    def get_by_id(user_id):
        """
        :param user_id: SERIAL: the id of a user to be found in the DB
        :return: user object or None if a user with such ID does not exist
        """
        id = user_id
        try:
           user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
           user = None
        # id = user_id
        # one_entry = CustomUser.objects.get(pk=id)
        return user
    @staticmethod
    def get_by_email(email):
        """
        Returns user by email
        :param email: email by which we need to find the user
        :type email: str
        :return: user object or None if a user with such ID does not exist
        """
        try:
            user = CustomUser.objects.get(email=email)
        except Exception:
            user = None
        return user
    @staticmethod
    def delete_by_id(user_id):
        """
        :param user_id: an id of a user to be deleted
        :type user_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        id = user_id
        try:
            user = CustomUser.objects.get(id=id)
            user.delete()
            return True
        except CustomUser.DoesNotExist:
            return False

            

    @staticmethod
    def create(email, password, first_name=None, middle_name=None, last_name=None):
        """
        :param first_name: first name of a user
        :type first_name: str
        :param middle_name: middle name of a user
        :type middle_name: str
        :param last_name: last name of a user
        :type last_name: str
        :param email: email of a user
        :type email: str
        :param password: password of a user
        :type password: str
        :return: a new user object which is also written into the DB
        """
        
    

        try:
            validator = EmailValidator()
            validator(email)
            user = CustomUser.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, email=email, password=password)
            user.save()
            return user
        except Exception:
            return None

        # return user
    def to_dict(self):
        """
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at, user is_active
        :Example:
        | {
        |   'id': 8,
        |   'first_name': 'fn',
        |   'middle_name': 'mn',
        |   'last_name': 'ln',
        |   'email': 'ln@mail.com',
        |   'created_at': 1509393504,
        |   'updated_at': 1509402866,
        |   'role': 0
        |   'is_active:' True
        | }
        """
        
        user = CustomUser.objects.get(pk=self.id)
        s=(self.created_at - datetime.datetime(1970,1,1, tzinfo=pytz.utc)).total_seconds()
        d=(self.updated_at - datetime.datetime(1970,1,1, tzinfo=pytz.utc)).total_seconds()
        
        upd = ('%f' % d).rstrip('0').rstrip('.')
        cre = ('%f' % s).rstrip('0').rstrip('.')
        dictionary = {}
        dictionary["id"] = user.id
        dictionary["first_name"] = user.first_name
        dictionary["middle_name"] = user.middle_name
        dictionary["last_name"] = user.last_name
        dictionary["email"] = user.email
        dictionary["created_at"] =  int(cre)
        dictionary["updated_at"] = int(upd)
        dictionary["role"] = user.role
        dictionary["is_active"] = user.is_active
        return dictionary
        # return CustomUser.objects.filter(pk=self.id).values()[0]


    def update(self,
               first_name=None,
               last_name=None,
               middle_name=None,
               password=None,
               role=None,
               is_active=None):
        """
        Updates user profile in the database with the specified parameters.\n
        :param first_name: first name of a user
        :type first_name: str
        :param middle_name: middle name of a user
        :type middle_name: str
        :param last_name: last name of a user
        :type last_name: str
        :param password: password of a user
        :type password: str
        :param role: role id
        :type role: int
        :param is_active: activation state
        :type is_active: bool
        :return: None
        """
        user = CustomUser.objects.get(pk=self.id)
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.password = password
        self.role = role
        self.is_active = is_active
        user.save()
    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all users
        """
        return list(CustomUser.objects.all())

    def get_role_name(self):
        """
        returns str role name
        """
        return '{}'.format(CustomUser.get_role_display(self))
