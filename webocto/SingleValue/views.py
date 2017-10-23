from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class testView(TemplateView):
	"""test view"""
	template_name = 'SingleValue/test.html'
	context_object_name = 'test'
	page = -1

	def get_context_data(self, **kwargs):
		context = {}
		return context

