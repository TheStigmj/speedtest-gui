# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.views import generic
from result.models import Result
	
class IndexView(generic.ListView):
	template_name = 'result/index.html'

	def get_queryset(self):
		queryset = None
		queryset = Result.objects.all()

		return queryset
