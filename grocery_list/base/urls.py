from django.urls import path
from .views import ItemList, ItemDetail, ItemCreate, ItemUpdate, DeleteView, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', ItemList.as_view(), name='items'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item'),
    path('item-create/', ItemCreate.as_view(), name='item-create'),
    path('item-update/<int:pk>/', ItemUpdate.as_view(), name='item-update'),
    path('item-delete/<int:pk>/', DeleteView.as_view(), name='item-delete'),
    # path('item-put-in-basket/<int:pk>/',  name='item-put-in-basket')
]