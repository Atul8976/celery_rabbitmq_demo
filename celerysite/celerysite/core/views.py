from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

# Create your views here.

class UsersListView(ListView):
    template_name = 'users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self,form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request,'We are generating your random user! wait a moment and refresh this page.')
        return redirect('users_list')