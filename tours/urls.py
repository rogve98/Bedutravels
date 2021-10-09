from django.urls import path
from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login"), 
    path('api/graphql/', GraphQLView.as_view(graphiql=True)),
]
