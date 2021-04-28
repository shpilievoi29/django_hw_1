from app1.views import home, about, foo
from first.urls import path

urlpatterns = [
    path("", home),
    path("home/", home),
    path("about/", about),
    path("foobar/<foo>/", foo),
]
