#######################
#####
##### Views code that allows for html pages to be rendered
#####
#######################


#imports needed functions
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import Exhibit, Email
from django.http import HttpResponse
from django.contrib import messages

#get link for exhibit pages created
def html_view(request, pk):
    html_page = get_object_or_404(Exhibit, pk=pk)
    return render(request, 'exhibit_template.html', {'html_page': html_page})

#gets link to homepage html
def homepage_view(request):
    html_pages = Exhibit.objects.all()  # Retrieve all HTMLPage objects from the database
    return render(request, 'homepage.html', {'html_pages': html_pages})

#gets link to exhibits html
def exhibits(request):
    html_pages = Exhibit.objects.all()  # Retrieve all HTMLPage objects from the database
    return render(request, 'exhibits.html', {'html_pages': html_pages})

#gets link to play html
def play(request):
    return render(request, 'play.html')

#gets link to moreinfo html
def moreinfo(request):
    return render(request, 'moreinfo.html')

#gets link to about html
def about(request):
    return render(request, 'about.html')

#gets link to feedback html
def feedback(request):
    return render(request, 'feedback.html')

#allows for email subimission
def submit_feedback(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Create and save the new feedback entry
        Email.objects.create(name=name, email=email)
        messages.success(request, 'Thank you for your feedback!')
        return render(request, 'homepage.html')
    else:
        return HttpResponse('Invalid request', status=400)
    