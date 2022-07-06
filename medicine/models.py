from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# People models

class Profile(models.Model):
		user = models.ForeignKey(User, on_delete=models.CASCADE)
		password = models.CharField(max_length =300)
		email = models.EmailField()
		phone_number  = models.IntegerField()
		category = models.CharField(max_length =30, default="user")

		def __str__(self):
			return str(self.id)

		@classmethod
		def get_all_profiles(cls):
			table = Profile.objects.all()
			return table


class Supplier(models.Model):
		name = models.CharField(max_length =30)
		password = models.CharField(max_length =30)
		location = models.CharField(max_length =30)
		bio = models.TextField(max_length =300)
		email = models.EmailField()
		phone_number  = models.IntegerField()
		profile_pic = models.ImageField(upload_to = 'articles/')
		category = models.CharField(max_length =30, default="supplier")

		def __str__(self):
				return self.name

		@classmethod
		def get_all_suppliers(cls):
			table = Supplier.objects.all()
			return table



# Products
class Medicine(models.Model):
		name = models.CharField(max_length =30)
		disease = models.CharField(max_length =30)
		price  = models.IntegerField()
		description = models.TextField(max_length =300)
		picture = models.ImageField(upload_to = 'articles/')

		def __str__(self):
				return self.name

		@classmethod
		def get_all_medicines(cls):
			table = Medicine.objects.all()
			return table


# Actions models

class  Donating(models.Model):
		amount  = models.IntegerField()
		donor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
		medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

		def __str__(self):
			return str(self.id)

		@classmethod
		def get_all_donations(cls):
			table = Donating.objects.all()
			return table

	
class  Purchasing(models.Model):
		units  = models.IntegerField()
		buyer = models.ForeignKey(User, on_delete=models.CASCADE)
		medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

		def __str__(self):
			return str(self.id)

		@classmethod
		def get_all_purchases(cls):
			table = Purchasing.objects.all()
			return table

class  Prescription(models.Model):
		picture = models.ImageField(upload_to = 'prescription/')
		buyer = models.ForeignKey(User, on_delete=models.CASCADE)
		medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

		def __str__(self):
			return str(self.id)

		@classmethod
		def get_all_prescriptions(cls):
			table = Prescription.objects.all()
			return table