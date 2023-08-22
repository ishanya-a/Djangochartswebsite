from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.dashboard, name='dashboard'),
    path('tables', view=views.tables, name='tables'),
    path('billing', view=views.billing, name='billing'),
    path('documentation', view=views.documentation, name='documentation'),
    path('icons', view=views.icons, name='icons'),
    path('map', view=views.map, name='map'),
    path('notifications', view=views.notifications, name='notifications'),
    path('profile', view=views.profile, name='profile'),
    path('rtl', view=views.rtl, name='rtl'),
    path('template', view=views.template, name='template'),
    path('typography', view=views.typography, name='typography'),
    path('virtualreality', view=views.virtualreality, name='virtualreality'),
    path('signup', view=views.signup, name='signup'),
    path('signin', view=views.signin, name='signin'),
    path('logout', view=views.logout, name='logout'),
    path('api/chart1_data/', views.chart1_data, name='chart1_data_api'),
    path('api/chart2_data/', views.chart2_data, name='chart2_data_api'),
    path('api/chart3_data/', views.chart3_data, name='chart3_data_api'),
]