from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contect",views.contect,name='contect'),
    path("new_adm",views.new_adm,name="new_adm"),
    path("collage_infra",views.collage_infra,name='collage_infra'),
    path("branch",views.branch,name='branch'),
    path("alu_con",views.alu_con,name='alu_con')
]