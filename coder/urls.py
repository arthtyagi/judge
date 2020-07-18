from django.urls import path
from .import views
from .views import CoderListView, CoderDetailView, CoderCreateView
app_name = 'coder'

urlpatterns = [
    path('', CoderListView.as_view(), name='home'),
    path('question/<int:pk>/', CoderDetailView.as_view(), name='detail'),
    path('<int:qid>/answer/', CoderCreateView.as_view(), name= 'submit')
]
