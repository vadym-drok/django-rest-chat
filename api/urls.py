from django.urls import path
from .views import (MessageDetailView,
                    MessageCreateView,
                    MessageList,
                    )

urlpatterns = [
    path('messages/single/<int:pk>/', MessageDetailView.as_view(), name='detail'),
    path('messages/list/<int:pk>/', MessageList, name='list'),
    path('messages/create/', MessageCreateView.as_view(), name='create'),
]
