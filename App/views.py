from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from App.models import UserData


def UserEdit(request):


    count = UserData.objects.filter(Username = "Kamilek").count()

    if count is 0:
        data = UserData()
        data.Username = "Kamilek"
        data.Sex = "Man"
        data.SexWant = "Woman"
        data.Description = "Jestem Kamil i szukam ciekawych znajomosci"
        data.Location = "Kielce"
        data.Photos = "myphoto.png, phoo.jpg, selfie.jpg"
        data.Name = "Kamil"
        data.RadiusWant = "100"
        data.save()

    newvar = UserData.objects.get(Username = "Kamilek")


    return render_to_response('home.html', { 'Name': newvar.Name, 'Location': newvar.Location }, context_instance=RequestContext(request))