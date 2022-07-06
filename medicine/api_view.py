from django.shortcuts import render, redirect
from .models import Profile, Supplier, Medicine, Donating, Purchasing, Prescription
from .serializer import ProfileSerializer, SupplierSerializer, MedicineSerializer, DonatingSerializer, PurchasingSerializer, PrescriptionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ProfileList(APIView):
		def get(self, request, format=None):
				profile = Profile.get_all_profiles()
				serializers = ProfileSerializer(profile, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = ProfileSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class SupplierList(APIView):
		def get(self, request, format=None):
				suppliers = Supplier.get_all_suppliers()
				serializers = SupplierSerializer(suppliers, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = SupplierSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class MedicineList(APIView):
		def get(self, request, format=None):
				medicines = Medicine.get_all_medicines()
				serializers = MedicineSerializer(medicines, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = MedicineSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class DonatingList(APIView):
		def get(self, request, format=None):
				donations = Donating.get_all_donations()
				serializers = DonatingSerializer(donations, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = DonatingSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class PurchasingList(APIView):
		def get(self, request, format=None):
				purchase = Purchasing.get_all_purchases()
				serializers = PurchasingSerializer(purchase, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = PurchasingSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class PrescriptionList(APIView):
		def get(self, request, format=None):
				prescription = Prescription.get_all_prescriptions()
				serializers = PrescriptionSerializer(prescription, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = PrescriptionSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
