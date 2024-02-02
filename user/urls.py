from django.urls import path
from user import views

urlpatterns = [
    path('signup',views.SignUpView.as_view(),name='sign-up'),
    path('home/',views.UserBookListView.as_view(),name='user-bk-home')
]
