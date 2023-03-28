from django.http import HttpResponse
from django.shortcuts import render
import blog
from blog.models import About, Contact, Post
from django.views.generic import ListView  ,DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CommentForm, ContactForm
from django.contrib import messages

# views.py

# class HomeListView(ListView):
#     model = Post
#     template_name = 'blog/full-article.html'

class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html' # name of your home template
    paginate_by=3

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/full-article.html'
    form_class = CommentForm
    success_url = reverse_lazy('full-article')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your Comment has been sent. Thank you!')
        return super().form_valid(form)
    # context_object_name = 'post'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(slug=self.kwargs['slug'])    

class AboutListView(ListView):
    model = About
    template_name = 'blog/about.html' # name of your about template
    context_object_name = 'about page description articles' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_blog'] = About.objects.values_list('about_blog', flat=True).first()
        return context
    

# class ContactListView(ListView):
#     model = Contact
#     template_name = 'blog/contact.html' # name of your about template
#     context_object_name = 'contact page'

    
class ContactView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent. Thank you!')
        return super().form_valid(form)

    
        

# def home(request):
#     posts = Post.objects.all().order_by('-created')
#     context = {'post': posts}
#     return render(request, 'blog/home.html', context)



# def about(request):
#     return render(request, 'blog/about.html')


def post(request):
    return render(request, 'blog/full-article.html')


# def contact(request):
#     return render(request, 'blog/contact.html')


