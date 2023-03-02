from django.urls import path


from users.views import user

urlpatterns = [
    path('', user.UserListView.as_view()),
    path('<int:pk>/', user.UserDetailView.as_view()),
    path('create/', user.UserCreateView.as_view()),
    path('<int:pk>/update/', user.UserUpdateView.as_view()),
    path('<int:pk>/delete/', user.UserDeleteView.as_view()),

]