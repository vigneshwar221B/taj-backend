from django.urls import path
from .import views
urlpatterns = [
    path('items/', views.ItemView.as_view()),
    path('order/', views.OrderView.as_view()),
    path('customers/',views.CustomerSearchView.as_view()),
    path('daily/',views.DailyItemView.as_view()),
    path('subitems/',views.SubItemsView.as_view())
]
