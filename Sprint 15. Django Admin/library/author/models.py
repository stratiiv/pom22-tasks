from django.db import models, IntegrityError, DataError

import book.models



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
    name = models.CharField(blank = True, max_length=20)
    surname = models.CharField(blank = True, max_length=20)
    patronymic = models.CharField(blank = True, max_length=20)
    books = models.ManyToManyField(book.models.Book, related_name='authors')
    id = models.AutoField(primary_key=True)
    date_of_birth=models.DateField(default=None)
    date_of_death=models.DateField(default=None)


    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """
        # return ",".join([a for a in dir(self) if not a.startswith('__')])
        # return str(self.__dict__)
        return f"\'id\': {self.pk}, \'name\': \'{self.name}\'," \
               f" \'surname\': \'{self.surname}\', \'patronymic\': \'{self.patronymic}\'"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """
        return f"Author(id={self.pk})"


    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """
        # return Author.objects.filter(id=author_id)
        # return Author.get_by_id(author_id)
        # return  Author.get_object_or_404()
        try:
            return Author.objects.get(pk=author_id)
        except:
            return None


    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a author to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            a = Author.objects.get(pk=author_id)
        except:
            return False
        else:
            a.delete()
            return True



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
        # return Author(name=name, surname=surname, patronymic=patronymic)
        a = None
        if name and len(name) <= 20 and surname and len(surname) <= 20 and patronymic and len(patronymic) <= 20:
            a = Author(name=name, surname=surname, patronymic=patronymic)
            a.save()
        return a

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
        # return self.__dict__



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

        if name and len(name) <= 20:
            self.name = name
        if surname and len(surname) <= 20:
            self.surname = surname
        if patronymic and len(patronymic) <= 20:
            self.patronymic = patronymic
        self.save()




    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        return Author.objects.all()