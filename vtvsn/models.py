from django.db import models


class Donor(models.Model):
	donor_name = models.CharField(max_length=80)
	contact_no = models.CharField(max_length=11)
	donor_email = models.EmailField(max_length=80)
	donor_address=models.CharField(max_length=200)

class meta:
	db_table = "DonorTable"

class Donation(models.Model):
	donor = models.ForeignKey(Donor, on_delete = models.CASCADE)
	donation_date = models.DateField(auto_now_add = True)
	# designation_choices= (
	# 	('FTC', 'Feed the Children'),
	# 	('FFTH', 'Food for the Hungry'),
	# 	('WFP', 'World Food Programme'),
	# 	('AAH', 'Action Against Hunger'),
	# 	('RAHP', 'Rise Against Hunger Philippines'),
	# 	('O', 'Others')
	# 	)
	donation_designation = models.CharField(max_length=100, null=True)
	donation_amount=models.CharField(max_length=99999)
	# services_choices= (
	# 	('GP', 'GrabPay'),
	# 	('GC', 'Gcash'),
	# 	('PMY', 'Paymaya'),
	# 	)
	payment_services = models.CharField(max_length=100, null=True)
	eWallet_number=models.CharField(max_length=11)

class meta:
	db_table = "DonationTable"

class Comment(models.Model):
	donor = models.ForeignKey(Donor, on_delete = models.CASCADE)
	donator_comment = models.TextField(max_length=200)




	# name = models.ForeignKey(Customer, on_delete = models.CASCADE)
	# timestamp = models.DateField(auto_now_add = True)
	# product = models.ForeignKey(Product, on_delete = models.CASCADE)
	# quantity = models.PositiveIntegerField()

# # Create your models here.
# class Donate(models.Model):
# 	# id=AutoField(primary_key=True)
# 	donor = models.CharField(max_length=80)
# 	donor_c = models.CharField(max_length=11)
# 	donor_email = models.EmailField(max_length=80)
# 	donor_address = models.TextField(blank = True)
# 	# donate_date = models.TextField(max_length=999)
# 	# amount = models.PositiveIntegerField()
# 	# ddesignation = (
# 	# 	('FTC', 'Feed the Children'),
# 	# 	('FFTH', 'Food for the Hungry'),
# 	# 	('WFP', 'World Food Programme'),
# 	# 	('AAH', 'Action Against Hunger'),
# 	# 	('RAHP', 'Rise Against Hunger Philippines'),
# 	# 	('O', 'Others')
# 	# 	)
# 	# designation= models.CharField(max_length=80, choices=ddesignation, null=True)
# 	# service = (	
# 	# 	('GP', 'GrabPay'),
# 	# 	('GC', 'Gcash'),
# 	# 	('PMY', 'Paymaya'),
# 	# 	)
# 	# service= models.CharField(max_length=80, choices=service, null=True)
# 	# eWallet = models.PositiveIntegerField()
# 	# dMessage = models.TextField(max_length=200)

# 	class meta:
# 		db_table = "DonationTable"




# from django.db import models

# class DonorInformation(models.Model):
# 	dname = models.TextField(blank = True)
# 	demail = models.TextField(blank = True)
# 	dcontacts = models.TextField(blank = True)
	
# class DonationPurpose(models.Model):
# 	ddesignation = models.TextField(blank = True)
# 	dtype = models.TextField(blank = True)

# class DonationInformation(models.Model):
# 	dreceiptnum = models.TextField(blank = True)
# 	ddate = models.TextField(blank = True)
# 	damount = models.TextField(blank = True)
# 	dpaymentmethod = models.TextField(blank = True)

# class PaymentInformation(models.Model):
# 	dcardtype = models.TextField(blank = True)
# 	dcardnum = models.TextField(blank = True)
# 	dexpirationdate = models.TextField(blank = True)
# 	dbillingaddress = models.TextField(blank = True)

# class DonationDedication(models.Model):
# 	dmessage = models.TextField(blank = True)
# 	designature = models.TextField(blank = True)
