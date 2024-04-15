from django.shortcuts import render


# Render the index.html template as a response to the request
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
