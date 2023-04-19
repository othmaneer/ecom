from django.urls import path, reverse
from .views import *
urlpatterns = [
    path('', list_produit, name='list_produit'),
    path('createUser/', create_user, name='createuser'),
    path('ReverserUser/', create_user, name='reverserUser'),
    path('loginUser/', login_user, name='loginuser'),
    path('createProduct/',create_product,name='AddProduct')



    #path('.createUser/', create_user, name='createuser'),
]