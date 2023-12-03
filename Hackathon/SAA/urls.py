from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('model/',views.model,name = 'model'),
    path('model2/',views.model2,name = 'model2'),
    path('report/',views.report,name = 'report'),
    path('contacts/',views.contacts,name = 'contacts'),
]