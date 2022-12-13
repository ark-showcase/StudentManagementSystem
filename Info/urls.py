from django.urls import path
from Info import views

app_name = "info"

urlpatterns = [
    path('',views.index, name = "index"),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('add_student/', views.student_form, name = "student_form"),
    path('add_address/', views.address_form, name = "address_form"),
    path('update_student/<int:id>/', views.update_student, name="update_student"),
    path('address/', views.address_list, name = "address_list"),
    path('address_detail/<int:address_id>/', views.address_detail, name='address_detail'),
    path('update_address/<int:id>/', views.update_address, name="update_address"),
    path('delete_address/<int:id>/', views.delete_address, name="delete_address"),
    path('delete_student/<int:id>/', views.delete_student, name="delete_student")
]