from django.db import models
from django.core.exceptions import ValidationError


def is_real(num):
    if int(num)<0:
        raise ValidationError('Count should be real number')
    else:
        return num
    
class Book(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
    """
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10,validators=[is_real])

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return self.name

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f"Book(id={self.id})"

    
    
    def get_authors(self):
        output=''
        for author in self.authors.all():
            output+=str(author)+', '
        return output[:-2]