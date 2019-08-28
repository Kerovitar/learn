from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from . import models


def enrich_context_data(cd):
    cd ["contact"] = models.Contact.objects.first()


class MainListView(ListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enrich_context_data(context)
        return context
    
    
class MainView(TemplateView):
    template_name = "core/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enrich_context_data(context)
        return context


class PoolsView(MainListView):
    model = models.Pool
    

class PoolMaterialView(MainListView):
    model = models.PoolMaterial
    
    
class PoolView(MainListView):
    model = models.Pool
    
    
class FountainsView(MainListView):
    model = models.Fountain
    

class BathView(MainListView):
    model = models.Bath
         
       
class SPAView(MainListView):
    model = models.SPA      
       
       
class HummumTypeView(MainListView):
    model = models.HummumType
    
    
class HummumView(MainListView):
    model = models.Hummum 


class AutowatView(MainListView):
    model = models.Autowat