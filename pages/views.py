from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World! You must know SebecJeanLuc!')
