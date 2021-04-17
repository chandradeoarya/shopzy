from django.urls import path, include

from product import views

urlpatterns=[
    path('latest-products/', views.LatestProductList.as_view())
]