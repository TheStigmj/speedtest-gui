# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.views import generic
from result.models import Result

import logging
	
class HomePageView(generic.TemplateView):
	template_name = 'speedsite/index.html'
		
	def get_context_data(self, **kwargs):
		context = super(generic.TemplateView, self).get_context_data(**kwargs)
		results = Result.objects.order_by().values('hostname').distinct()
		context['hostnames'] = results
		return context
		