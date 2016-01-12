from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from App.models import UserData
from Libs.User import UserLib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
def UserLogin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/panel/')
            else:
                return HttpResponseRedirect('?error=LoginError')
    return render_to_response('login.html', {}, context_instance=RequestContext(request))


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

            UserLib.CreateUser(request, {'Username': username,
                                         'Name': 'null',
                                         'Descriptions': 'null',
                                         'Photos': 'null',
                                         'Location': 'null',
                                         'Sex': 'null',
                                         'SexWant': 'null',
                                         'RadiusWant': 0 })
    return render_to_response('register.html', {}, context_instance=RequestContext(request))


def UserEdit(request):
    if request.POST:
        name = request.POST['name']
        description = request.POST['description']
        photos = request.POST['photos']
        location = request.POST['location']
        sex = request.POST['sex']
        sexwant = request.POST['sexwant']
        radiuswant = request.POST['radiuswant']

        UserLib.SetUserData(request, request.user.username,{'Name': name,
                                                            'Description': description,
                                                            'Photos': photos,
                                                            'Location': location,
                                                            'Sex': sex,
                                                            'SexWant': sexwant,
                                                            'RadiusWant': radiuswant })

    return render_to_response('edit.html', { 'Name': 'Patrycja' }, context_instance=RequestContext(request))



def UserLogout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/UserLogin')
    else:
        return HttpResponseRedirect('/UserLogin')


def UserProfile(request):
    objects = UserLib()
    name = objects.GetUserData(request.user.username, "Email")
    location = objects.GetUserData(request.user.username, "Location")
    sex = objects.GetUserData(request.user.username, "Sex")
    sexwant = objects.GetUserData(request.user.username, "SexWant")
    radiuswant = objects.GetUserData(request.user.username, "RadiusWant")
    description  = objects.GetUserData(request.user.username, "Description")
    return render_to_response('profile.html', {'Name':name}, context_instance = RequestContext(request))
