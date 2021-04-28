from app2.views import *
from first.urls import path

urlpatterns = [
    path("number/<int:num>/", num),
    path("string/<str:st>/", string1),
    # path("welcome/<slug:well/>", slug1)
]
