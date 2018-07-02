# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.views import generic
from result.models import Result
import json
from django.utils.safestring import mark_safe
	
class IndexView(generic.ListView):
	template_name = 'result/index.html'

	def get_queryset(self):
		queryset = None
		queryset = Result.objects.all()

		return queryset

class DetailView(generic.DetailView):
	model = Result
	template_name = 'result/detail.html'
	dldata = {}
	uldata = {}
	pingdata = []
	jitterdata = []

	def parseLog(self):
		pingstart = 0
		dlstart = 0
		ulstart = 0
		firstul = True
		firstdl = True
		for line in self.object.log.splitlines():
			line = line.split(" ")
			tcode = line[0][:-1]
			if line[1] == "pingTest":
				# This is the start of the pingtest, record the timestamp for comparison
				pingstart = tcode
			elif line[1] == "PING:":
				#print "Found PING: " + line[2] + " at timecode " + tcode
				if line[2] == "":
					line[2] = "0.0"
				self.pingdata.append(line[2])
				if line[4] == "":
					line[4] = "0.0"
				self.jitterdata.append(line[4])
			elif line[1] == "dlTest":
				# This is the start of the dltest, record the timestamp for comparison
				dlstart = tcode
			elif line[1] == "DL:":
				if "(in" not in line:
					if line[2] == "":
						line[2] = "0.0"
					if not firstdl:
						self.dldata[int(tcode)-int(dlstart)] = line[2]
					else:
						dlstart = tcode
						firstdl = False
			elif line[1] == "ulTest":
				# This is the start of the ultest, record the timestamp for comparison
				ulstart = tcode
			elif line[1] == "UL:":
				if "(in" not in line:
					if line[2] == "":
						line[2] = "0.0"
					if not firstul:
						self.uldata[int(tcode)-int(ulstart)] = line[2]
					else:
						ulstart = tcode
						firstul = False
	
	def get_context_data(self, **kwargs):
		context = super(generic.DetailView, self).get_context_data(**kwargs)

		self.dldata = {}
		self.uldata = {}
		self.pingdata = []
		self.jitterdata = []		
		self.parseLog()
		
		context['dldata'] = mark_safe(json.dumps(self.dldata, sort_keys=True))
		context['uldata'] = mark_safe(json.dumps(self.uldata, sort_keys=True))
		context['pingdata'] = "["+",".join(self.pingdata)+"]"
		context['jitterdata'] = "["+",".join(self.jitterdata)+"]"
		return context
		