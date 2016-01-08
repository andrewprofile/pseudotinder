from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

def UserEdit(request):
    return render_to_response('home.html', context_instance=RequestContext(request))