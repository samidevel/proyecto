from django.shortcuts import render
from erp.models import Category

#from django.http 	import HttpResponse


def category_list(request):
	data = {
		'title': 'listado categorias',
		'categories': Category.objects.all()

	}
	return render(request, 'category/list.html', data)