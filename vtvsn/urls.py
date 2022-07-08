from django.contrib import admin
from django.urls import path
from vtvsn import views 
from django.urls import re_path as url



urlpatterns = [

    url(r'^donorlist/$', views.donorpageList, name='donorlist/'),
    url(r'^(\d+)/showPage/', views.showPage, name='showPage/'),
    url(r'^(\d+)/(\d+)/addDonation/', views.addDonation, name='addDonation/'),
    url(r'^(\d+)/summary/', views.summaryPage, name='summary/'),
    url(r'^None/summary/', views.summaryPageII, name='summary/'),
    url(r'^(\d+)/canceldonation/', views.cancelDonation, name='canceldonation/'),
    url(r'^edit/(\d+)', views.editDonorInfo, name='edit/'),
    url(r'^edit/update/(\d+)', views.updateDonorInfo, name='update/'),

    
    # path('donorpage/',views.donorpage, name='donorpage/'),


#otherpages
    # path('Homepage/', views.Homepage, name='Homepage/'),
    path('Donation/', views.Donation_, name='Donation/'),
    path('Homepage/', views.Homepage, name='Homepage/'),
    path('About/', views.About, name='About/'),
    path('History/', views.History, name='History/'),
    path('History2/', views.History2, name='History2/'),
    path('History3/', views.History3, name='History3/'),
    path('History4/', views.History4, name='History4/'),
    path('History5/', views.History5, name='History5/'),
    path('ElectionAndDemocracy/', views.ElectionAndDemocracy, name='ElectionAndDemocracy/'),
    path('ElectionAndDemocracy2/', views.ElectionAndDemocracy2, name='ElectionAndDemocracy2/'),
    path('ElectionAndDemocracy3/', views.ElectionAndDemocracy3, name='ElectionAndDemocracy3/'),
    path('ElectionAndDemocracy4/', views.ElectionAndDemocracy4, name='ElectionAndDemocracy4/'),
    path('ElectionAndDemocracy5/', views. ElectionAndDemocracy5, name='ElectionAndDemocracy5/'),
    path('RightOfSuffrage/', views.RightOfSuffrage, name='RightOfSuffrage/'),
    path('RightOfSuffrage2/', views.RightOfSuffrage2,name='RightOfSuffrage2/'),
    path('RightOfSuffrage3/', views.RightOfSuffrage3, name='RightOfSuffrage3/'),
    path('RightOfSuffrage4/', views.RightOfSuffrage4, name='RightOfSuffrage4/'),
    path('RightOfSuffrage5/', views.RightOfSuffrage5, name='RightOfSuffrage5/'),
    path('RightOfSuffrage6/', views.RightOfSuffrage6, name='RightOfSuffrage6/'),
    path('Guides/', views.Guides, name='Guides/'),
    path('Guides2/', views.Guides2, name='Guides2/'),
    path('SP/', views.SP, name='SP/'),
    path('SP2/', views.SP2,name='SP2/'),
    path('Step1/', views.Step1, name='Step1/'),
    path('Step2/', views.Step2, name='Step2/'),
    path('Step3/', views.Step3, name='Step3/'),
    path('Step3II/', views.Step3II, name='Step3II/'),
    path('Step4/', views.Step4, name='Step4/'),
    path('Step4II/', views.Step4II, name='Step4II/')
]


