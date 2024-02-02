from django.urls import path
from books import views


urlpatterns = [
    path('home',views.IndexView.as_view(),name='home'),
    path('addbk/',views.BookCreateView.as_view(),name='bk-add'),
    path('<int:pk>/detail',views.BookDetailView.as_view(),name="bk-view"),
    path('<int:pk>/update',views.BookUpdateView.as_view(),name="bk-update"),
    path('<int:pk>/delete',views.BookDeleteView.as_view(),name='bk-delete'),
    path('',views.SignInView.as_view(),name='sign-in'),
    path('signout',views.LogOutView.as_view(),name="logout")
]
