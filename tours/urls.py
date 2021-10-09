from django.urls import path
from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', views.index, name="index"),
    path('api/graphql/', GraphQLView.as_view(graphiql=True)),
]
