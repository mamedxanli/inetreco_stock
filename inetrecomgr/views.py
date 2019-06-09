#Django native imports
from django.views import generic
from django.shortcuts import render, render_to_response

# Python imports
from itertools import chain

# Import from our apps
from netdev.models import Netdev

class HomePage(generic.TemplateView):
    template_name = "inetrecomgr/index.html"
    context_object_name = 'context'

    def get_context_data(self,**kwargs):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        context = super().get_context_data(**kwargs)
        context['netdevs_all'] = Netdev.objects.all()
        return context

