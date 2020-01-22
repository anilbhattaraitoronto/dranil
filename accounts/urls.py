from django.urls import path
from . import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('create_account', account_views.create_account, name="create_account"),
    path('login', account_views.login_view, name='login_view'),
    path('logout', account_views.logout_view, name='logout_view'),
    path('send_message', account_views.send_message, name='send_message'),
]
