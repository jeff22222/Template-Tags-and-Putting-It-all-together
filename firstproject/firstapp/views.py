from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from firstapp.models import Blog
from firstapp.forms import BlogForm
# Create your views here.
class BlogListView(ListView):
    model = Blog

    # Delivers/Look
    # looks for template firstapp/blog_list.html
    # Delivers list blog_list/object_list = Blog.object.all

# users in put data
class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # fields=['title','author','message']

    # Delivers/looks for
    # looks for template firstapp/blog_form.html
    # Delivers list form = BlogForm()

class BlogDetailView(DetailView):
    model = Blog


    # Delivers/looks for
    # looks for template firstapp/blog_detail.html
    # Delivers list blog/object = Blog.object.get(pk=pk)

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    # fields=['title','author','message']

    # Delivers/looks for
    # looks for template firstapp/blog_form.html
    # Delivers list form = BlogForm()

class BlogDeleteView(DeleteView):
    model = Blog
    
    # Delivers/looks for
    # looks for template firstapp/blog_confirm_delete.html
    # Delivers list blog/object = Blog.object.get(pk=pk)

    success_url = reverse_lazy('firstapp:blog_list')