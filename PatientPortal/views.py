from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from PatientPortal.models import patient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import logout
import random
import way2sms

def index(request):
    #return HttpResponse("Patient Login")
	return render(request,'PatientPortal/index.html',{})
# Create your views here.

def logina(request):
	context = RequestContext(request)
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email,password=password)
		try:
			p=patient.objects.get(user=user)
		except patient.DoesNotExist:
			p=None
		if user:
			if user.is_active and p :
				login(request,user)
				return redirect(home)
				#return redirect(home)
			else:
				return render(request,'PatientPortal/otpfail.html',{}) 
		else:
			#HttpResponse("invaild")
			return render(request,'PatientPortal/loginfail.html',{}) #redirect to invaild  username password url
	else:
		return redirect(index)#redirect if not post request was send



@login_required
def home(request):
	return render(request,'PatientPortal/home.html',{})




@csrf_exempt
def register(request):
	context = RequestContext(request)
	if request.method == 'POST':
		email 		= request.POST['email']
		password 	= request.POST['password']
		fname 		= request.POST['fname']
		lname		= request.POST['lname']
		phno		= request.POST['phno']
		user = User.objects.create_user(username=email,
                                 		email=email,
                                 		password=password)
		user.save()
		rnum=random.randint(1000,9999)
		p=patient(user=user,
				  fname=fname,
				  lname=lname,
				  otp=rnum,
				  phno=phno)
		p.save()
		message="OTP"
		message+=str(rnum)
		q=way2sms.sms(8891821262,"way2sms3131")
		q.send(8075785481,message)
		n=q.msgSentToday()
		q.logout()
		return render(request,'PatientPortal/otp.html',{'phno':phno})
		#
		#return render(request,'PatientPortal/otp.html',{})
	return redirect(logina)

def otpverify(request):
	context = RequestContext(request)

	if request.method == 'POST':
		phno= request.POST['phno']
		otp= request.POST['otp']
		try:
			p=patient.objects.get(phno=phno,otp=otp)
		except patient.DoesNotExist:
			p=None
		if p:
			p.validate=True
			return render(request,'PatientPortal/otpsuc.html',{}) 
		else:
			return render(request,'PatientPortal/otpfail.html',{}) 
	else:
		return redirect(logina)
