
from django.urls import path

from . import views

app_name="crickapp"
urlpatterns = [

    path('',views.index,name='index'),
    path('cricketers/<int:cricketers_id>/',views.detail,name='detail'),
    path('add/',views.add_cricketers,name='add_cricketers'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]
