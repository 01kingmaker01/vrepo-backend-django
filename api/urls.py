from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('posts/',views.PostCreate.as_view()),
    path('posts/<int:id>',views.PostView.as_view()),
    path('update/<int:id>',views.PostUpdateDelete.as_view()),
    
]