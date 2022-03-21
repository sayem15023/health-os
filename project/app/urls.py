from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppView.index, name='index'),
    path('customer_registration/', views.AppView.customer_registration, name='customer_registration'),
    path('withdwaw_money/<int:pk>/', views.AppView.withdwaw_money, name='withdwaw_money'),
    path('update_user_plan/<int:pk>/', views.AppView.update_user_plan, name='update_user_plan'),

    # Additional for project
    path('get_all_user/', views.AppViewAdditional.get_all_user, name='get_all_user'),

    # Prerequisite for project
    path('save_company/', views.AppViewPrerequisite.save_company, name='save_company'),
    path('save_plan/', views.AppViewPrerequisite.save_plan, name='save_plan'),
    path('save_phone/', views.AppViewPrerequisite.save_phone, name='save_phone'),
    path('save_payment/', views.AppViewPrerequisite.save_payment, name='save_payment')
]
