from django.db import models

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
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(blank = True, max_length=20)
    books = models.ManyToManyField(book.models.Book, related_name='authors')



    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """

        return f'{self.name} {self.patronymic} {self.surname}'

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """
        return f"Author(id={self.pk})"
    
    def get_books(self):
        return ', '.join([str(book) for book in self.books.all()])
            

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





