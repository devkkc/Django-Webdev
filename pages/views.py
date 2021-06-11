from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    """
    View for the homepage of website
    :param request: url request
    """

    return HttpResponse("Hello World!")