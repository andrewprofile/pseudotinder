from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from App.models import UserData
from Libs.User import UserLib
from django.contrib.auth.models import User

def UserLogin(request):
    if request.POST:
        print("post")
    return render_to_response('register.html', {}, context_instance=RequestContext(request))


#GÓRE IGNORUJ, PATRZ NA USER REGISTER
def UserRegister(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        error = False

        if not email or not username or not password:
            error = True
        if email and User.objects.filter(email=email).count() or username and User.objects.filter(username=username).count() > 0:
            error = True

        if error is False:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

    return render_to_response('register.html', {}, context_instance=RequestContext(request))


def UserEdit(request):

    return render_to_response('home.html', { 'Name': 'Patrycja' }, context_instance=RequestContext(request))
