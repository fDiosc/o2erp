from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastros", views.cadastros, name="cadastros"),
    path("diarias", views.diarias, name="diarias"),
    path("pessoafisica", views.pessoafisica, name="pessoafisica"),
    path("pessoajuridica", views.pessoajuridica, name="pessoajuridica"),
    path("contrato", views.contrato, name="contrato"),
    path("servico", views.servico, name="servico"),
    path("update/<int:item_id>", views.update, name="update"),
    # User and login urls
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]