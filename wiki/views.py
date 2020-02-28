from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from wiki.models import Page
from wiki.forms import PageForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy



class PageListView(ListView):
  """ Renders a list of all Pages. """
  model = Page

  def get(self, request):
      """ GET a list of Pages. """
      pages = self.get_queryset().all()
      return render(request, 'list.html', {
        'pages': pages
      })

class PageDetailView(DetailView):
  """ Renders a specific page based on it's slug."""
  model = Page

  def get(self, request, slug):
      """ Returns a specific wiki page by slug. """
      page = self.get_queryset().get(slug__iexact=slug)
      return render(request, 'page.html', {
        'page': page
      })

class PageCreateView(CreateView):
  
  
  def get(self, request):
    context = {'form':PageForm(request.POST)}
    return render(request, 'new_page.html', context)


  def post(self, request, *args, **kwargs):
    form = PageForm(request.POST)
    if form.is_valid():
      new_wiki_page = form.save()
      return HttpResponseRedirect(reverse_lazy('wiki:wiki-details-page', args=[new_wiki_page.slug]))
    return render(request, 'new_page.html', {'form':form})

  #   if request.method == "POST":
  #     form = PageForm(request.POST)
  #     print("_____ form ___________")

  #     print(request.POST.get('slug', ''))


  #     if form.is_valid():
  #       wiki.title  = request.POST.get('title', '')
  #       wiki.slug = request.POST.get('slug', '')
  #       wiki.content = request.POST.get('content', '')
  #       wiki.modified = request.POST.get('modified', '')
  #       wiki.created = request.POST.get('created', '')
  #       wiki.author = User.objects.get(id=request.user.id)
  #       wiki.save()
      
  #       return HttpResponseRedirect(reverse('wiki:wiki-details-page', kwargs={'slug': wiki.slug}))


  #     else:

  #         errors = " Wiki was not updated"
  #         # messages.error(request, errors, extra_tags='alert')
  #         print("________________")
  #         print(errors)
  #   else:
  #       form = PageForm(instance=wiki)
  #       print("________________")
  #       print("Not a post request")
      
    
  #   wiki = Page()

  #   context = {'wiki_pages_detail': wiki,'form': form}

  #   return render(request, 'new_page.html', context)

  

