from django.http import HttpResponse


def home(request):
    return HttpResponse("You are at home")


def about(request):
    return HttpResponse("You are in about")


def foo(request, foo="foo"):
    return HttpResponse(f"resource and slug is {foo}")
