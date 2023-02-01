from django.urls import path
from links.views.factories import FactoriesCreateView, FactoriesListView

urlpatterns = [
    path("factory/create/", FactoriesCreateView.as_view()),
    path("factory/list/", FactoriesListView.as_view()),

]