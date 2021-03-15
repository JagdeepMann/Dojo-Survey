from django.shortcuts import render, redirect

def index(request):
    return render(request,"index.html")


def create_user(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comments = request.POST['description']
    
    context = {
        "name_on_template" : name_from_form,
        "location_template" : location_from_form,
        "language_template" : language_from_form,
        "comments" : comments,
    }
    return render(request, 'result.html', context)

