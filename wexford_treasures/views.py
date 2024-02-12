from django.core.exceptions import PermissionDenied
from django.shortcuts import render

'''
Error Handling
'''


def handler404(request, exception):
    '''
    Render 404 page
    '''
    return render(request, '404.html', status=404)