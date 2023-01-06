
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from .models import Author
from .forms import AuthorCreationForm
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from book.views import is_admin

class AuthorListView(LoginRequiredMixin,ListView):
    model = Author

class AuthorDetailView(LoginRequiredMixin,DetailView):
    model = Author 

@login_required
@user_passes_test(is_admin)
def get_create_author(request):
    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        try:
            Author.objects.get(name=request.POST.get('name'),surname=request.POST.get('surname'),patronymic=request.POST.get('patronymic'))
            return render(request, 'author/dublicate_author.html')
        except ObjectDoesNotExist:
            if form.is_valid():
                form.save()
                return redirect('authors')
    else:
        form = AuthorCreationForm()
        return render(request, 'author/create_author.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def get_delete_author(request, id):
    Author.delete_by_id(id)
    return redirect('authors')