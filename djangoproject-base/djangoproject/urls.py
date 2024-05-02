
from django.contrib import admin
from django.urls import path
from posting.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("category/", category, name="category"),
    path("myskills/", myskills, name="myskills"),

]
