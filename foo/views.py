# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Article
from forms import ArticleForm

class ArticleListView(ListView):
    model = Article

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        messages.success(self.request, "Article created.")
        return super(ArticleCreateView, self).form_valid(form)

class ArticleDetailView(DetailView):
    model = Article

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        messages.success(self.request, "Article updated.")
        return super(ArticleUpdateView, self).form_valid(form)

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article-list')

    def get(self, *args, **kwargs):
        """ Skip confirmation page """
        return self.delete(self.request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Article removed.")
        return super(ArticleDeleteView, self).delete(*args, **kwargs)        

