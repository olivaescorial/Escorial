from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def donorpage(request):
	dnrlist = Donor.objects.all()
	return render(request,'Donation.html')

def showPage(request,donorId):
	adddnt =  Donor.objects.get(id=donorId)
	if request.method == 'POST':
		donation = Donation.objects.create(donor=adddnt,
			donation_date=request.POST['donation_date'],
			donation_designation=request.POST['donation_designation'],
			donation_amount=request.POST['donation_amount'],
			payment_services=request.POST['payment_services'],
			eWallet_number=request.POST['eWallet_number'])

		# donation.save()
		return redirect(f'/vtvsn/{adddnt.id}/{donation.id}/addDonation/')
	else:
		return render(request, 'storage.html',{'adddnt':adddnt})


def donorpageList(request):
	donor = request.POST['donor_name']
	contact = request.POST['contact_no']
	email = request.POST['donor_email']
	address = request.POST['donor_address']
	newDonor =  Donor.objects.create(donor_name=donor, contact_no=contact,donor_email=email,
		donor_address=address)
	return redirect(f'/vtvsn/{newDonor.id}/showPage/')


def addDonation(request,addntID, donorId):
	adddnt =  Donor.objects.get(id=addntID)
	#donation =  Donation.objects.get(id=donation_id)
	addDonation=Donation.objects.filter(donor=donorId)

	if request.method == 'POST':
		# Comment.objects.create(donor=donorId, 
		# 	donator_comment=request.POST['donator_comment'])
		return redirect(f'/vtvsn/{adddnt.id}/summary/')
	else:
		return render(request, 'Comments.html',{'adddnt':adddnt})

def summaryPage(request, donorId):
	adddnt =  Donor.objects.get(id=donorId)
	addDonation=Donation.objects.filter(donor=donorId)
	print (addDonation)
	# addComment = Comment.objects.filter(donor=adddnt)
	# print(addComment)
	return render(request, 'summary.html',{'adddnt':adddnt,'addDonation':addDonation})

def cancelDonation(request, donorId):
	adddnt =  Donor.objects.get(id=donorId)
	adddnt.delete()
	return redirect(f'/vtvsn/{None}/summary/')

def summaryPageII(request):
	return render(request, 'summary.html')

def editDonorInfo(request, donorId):
	adddnt = Donor.objects.get(id=donorId)	
	return render(request,'edit.html', {'adddnt':adddnt})

def updateDonorInfo(request, donorId):
	adddnt = Donor.objects.get(id=donorId)
	adddnt.donor_name = request.POST['donor_name']
	adddnt.donor_name = request.POST['donor_name']
	adddnt.donor_email = request.POST['donor_email']
	adddnt.donor_address = request.POST['donor_address']

	adddnt.save()
	# addDonation.save()
	# item.donation_designation = request.POST['donation_designation']
	# item.donation_amount = request.POST['donation_amount']
	# item.payment_services = request.POST['payment_services']
	# item.eWallet_number = request.POST['eWallet_number']

	# addDonation.save()

	return redirect(f'/vtvsn/{adddnt.id}/summary/')

def Donation_(request):
	return render(request, 'Donation.html')
def Homepage(request):
	return render(request, 'index.html')
def About(request):
	return render(request, 'About-VoteVision2.html')
def History(request):
	return render(request, 'HistoryOfElection.html')
def History2(request):
	return render(request, 'HistoryOfElection2.html')
def History3(request):
	return render(request, 'HistoryOfElection3.html')
def History4(request):
	return render(request, 'HistoryOfElection4.html')
def History5(request):
	return render(request, 'HistoryOfElection5.html')
def ElectionAndDemocracy(request):
	return render(request, 'ElectionAndDemocracy.html')
def ElectionAndDemocracy2(request):
	return render(request, 'ElectionAndDemocracy2.html')
def ElectionAndDemocracy3(request):
	return render(request, 'ElectionAndDemocracy3.html')
def ElectionAndDemocracy4(request):
	return render(request,'ElectionAndDemocracy4.html')
def ElectionAndDemocracy5(request):
	return render(request, 'ElectionAndDemocracy5.html')
def RightOfSuffrage(request):
	return render(request, 'RightOfSuffrage.html')
def RightOfSuffrage1(request):
	return render(request, 'RightOfSuffrage1.html')
def RightOfSuffrage2(request):
	return render(request, 'RightOfSuffrage2.html')
def RightOfSuffrage3(request):
	return render(request, 'RightOfSuffrage3.html')
def RightOfSuffrage4(request):
	return render(request, 'RightOfSuffrage4.html')
def RightOfSuffrage5(request):
	return render(request, 'RightOfSuffrage5.html')
def RightOfSuffrage6(request):
	return render(request, 'RightOfSuffrage6.html')
def Guides(request):
	return render(request, 'Guides-VoteVision2.html')
def Guides2(request):
	return render(request, 'Guides-VoteVision.html')
def SP(request):
	return render(request, 'SP.html')
def SP2(request):
	return render(request, 'SP2.html')
def Step1(request):
	return render(request, 'Step1.html')
def Step2(request):
	return render(request, 'Step2.html')
def Step3(request):
	return render(request, 'Step3.html')
def Step3II(request):
	return render(request, 'Step3II.html')
def Step4(request):
	return render(request, 'Step4.html')
def Step4II(request):
	return render(request, 'Step4II.html')


	# if request.method == "POST":
	# 	Feedback.objects.create(uname=request.POST['name'],
	# 		uemail=request.POST['e-mail'],
	# 		uchoices=request.POST['concerns'],
	# 		umessage=request.POST['message'])
	# 	return redirect('/')
	# Feedback_List = Feedback.objects.all()
	# return render(request, 'mainpage.html',{'registered_Contact_Info': Feedback_List})
		
	#if request.method == 'POST':
		#return HttpResponse (request.POST['attribute'])
