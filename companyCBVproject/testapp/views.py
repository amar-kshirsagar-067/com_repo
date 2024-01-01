from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
from django.urls import reverse_lazy


class CompanyListView(ListView):   #reading data in view.py in adminstration
    model=Company
    #defult template name is :company_list.html
    #default context object name is : company_list


class CompanyDetailView(DetailView):  #display a perticular company details in views.py
    model=Company
    #default template file name is:company_detail.html
    #default context object name : company or object.

class CompanyCreateView(CreateView):
    model=Company
    fields = '__all__'
    #default template file name= company_form.html
    #default context object name : company_form

class CompanyUpdateView(UpdateView):
    model=Company
    fields = ['location','ceo']
    #default template file name : company_form.html

class CompanyDeleteView(DeleteView):
    model=Company
    success_url = reverse_lazy('list')

