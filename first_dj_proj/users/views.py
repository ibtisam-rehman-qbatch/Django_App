from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
    myUsers = User.objects.all().values
    allUsers_template = loader.get_template('all_users.html')

    context = {
        'myUsers' : myUsers,
    }

    return HttpResponse(allUsers_template.render(context, request))
    # return render(request,'first.html')
    
def details(request, id):
    myUser = User.objects.get(id=id)
    details_template = loader.get_template('userDetails.html')

    context = {
        'myUser' : myUser,
    }

    return HttpResponse(details_template.render(context, request))


def main(request):
    index_template = loader.get_template('main.html')

    return HttpResponse(index_template.render() )

# Create your views here.
