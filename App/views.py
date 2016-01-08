from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from App.models import UserData
from Libs.User import UserLib

def UserEdit(request):

    UserLib.UserEdit(request)

    UserLib.SetUserData(request, {'Username': 'Pati', 'Sex': 'Woman', 'SexWant': 'Man'})


    newvar = UserData.objects.get(Username = "Pati")


    return render_to_response('home.html', { 'Name': newvar.Username, 'Location': newvar.Location }, context_instance=RequestContext(request))