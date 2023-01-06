from django.db import models
import django
from book.models import Book
from django.contrib.auth.models import User
import django.utils
import datetime


class Order(models.Model):
    """
           This class represents an Order. \n
           Attributes:
           -----------
           param book: foreign key Book
           type book: ForeignKey
           param user: foreign key CustomUser
           type user: ForeignKey
           param created_at: Describes the date when the order was created. Can't be changed.
           type created_at: int (timestamp)
           param end_at: Describes the actual return date of the book. (`None` if not returned)
           type end_at: int (timestamp)
           param plated_end_at: Describes the planned return period of the book (2 weeks from the moment of creation).
           type plated_end_at: int (timestamp)
       """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(blank=True,null=True)
    expected_end_at = models.DateTimeField(default=django.utils.timezone.now()+datetime.timedelta(weeks=2))

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return f'Order #{self.id}'
    
    @staticmethod
    def delete_by_id(order_id):
        try:
            order = Order.objects.get(pk=order_id)
        except:
            return False
        else:
            order.delete()
            return True