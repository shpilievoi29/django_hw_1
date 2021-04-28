from django.http import HttpResponse


def num(request, num="num"):
    return HttpResponse(f"resource and slug is {num}")


def string1(request, st="stri"):
    return HttpResponse(f"resource and slug is {st}")


def slug1(request, num1="num1"):
    return HttpResponse(f"resource and slug is {num1}")
