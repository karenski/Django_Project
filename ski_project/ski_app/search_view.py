from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from ski_app.models import Category, Ski_Page

def search(request,category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_',' ')
    context_dict = {'category_name': category_name}

    filter_dict = {}
    
    brand = request.GET.get("brand")
    intended_usage = request.GET.get("intended_usage")
    if brand:
        filter_dict["brand"] = brand
    if intended_usage:
        filter_dict["intended_usage"] = intended_usage

    pages = Ski_Page.objects.filter(**filter_dict)

    for page in pages:
			page.url = page.model_name.replace(' ','_')

    return render_to_response('ski_app/category.html',context_dict, context)