from rest_framework import serializers
from .models import Profile, Supplier, Medicine, Donating, Purchasing, Prescription


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model = Profile
      fields = ('password', 'email', 'user', 'phone_number','category')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
      model = Supplier
      fields = ('name', 'email', 'location', 'phone_number','category','profile_pic','bio','password')

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
      model = Medicine
      fields = ('name', 'disease', 'price', 'description', 'picture')

class DonatingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Donating
      fields = ('Amount', 'donor', 'medicine')

class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Purchasing
      fields = ('Units', 'buyer', 'medicine')

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
      model = Prescription
      fields = ('picture', 'buyer', 'medicine')
