from django.db import models
from django.db.utils import DataError

class Author(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes last name of the author
        type surname: str max_length=20
        param patronymic: Describes middle name of the author
        type patronymic: str max_length=20

    """
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(default = None, max_length=20)
    surname = models.CharField(default = None, max_length=20)
    patronymic = models.CharField(default = None, max_length=20)
   

    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """
        return f"'id': {self.id}, 'name': '{self.name}', 'surname': '{self.surname}', 'patronymic': '{self.patronymic}'"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """
        return '{}(id={})'.format('Author', self.id)

    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """
        id = author_id
        try:
           author = Author.objects.get(id=id)
        except Author.DoesNotExist:
           author = None
        return author
    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a author to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        id = author_id
        try:
            author = Author.objects.get(id=id)
            author.delete()
            return True
        except Author.DoesNotExist:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: a new author object which is also written into the DB
        """
        try:
            author = Author.objects.create(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author
        except Exception:
            return None

    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """
        author = Author.objects.get(pk=self.id)
        dictionary = {}
        dictionary["id"] = author.id
        dictionary["name"] = author.name
        dictionary["surname"] = author.surname
        dictionary["patronymic"] = author.patronymic
        return dictionary
    

    def update(self,
               name=None,
               surname=None,
               patronymic=None):
        """
        Updates author in the database with the specified parameters.\n
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: None
        """
        author = Author.objects.get(pk=self.id)
    
        try:
            # author = Author.objects.get(pk=self.id)
            if name != None and len(name) <= 20:
                author.name = name
            if surname != None and len(surname) <= 20:
                author.surname = surname
            if patronymic != None and len(patronymic) <= 20:
                author.patronymic = patronymic
            author.save()
        except Exception:
            author = Author.objects.get(pk=self.id)

            
        
        


    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """       
        return list(Author.objects.all())
