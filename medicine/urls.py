from django.urls import path, include
from . import views, api_view



urlpatterns = [
  path('', views.welcome,name = 'test'),
  path('api/profile/', api_view.ProfileList.as_view(), name = 'profile'),
  path('api/supplier/', api_view.SupplierList.as_view()),
  path('api/medicine/', api_view.MedicineList.as_view()),
  path('api/donation/', api_view.DonatingList.as_view()),
  path('api/purchase/', api_view.PurchasingList.as_view()),
  path('api/prescription/', api_view.PrescriptionList.as_view()),

]
