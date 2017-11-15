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

def index(request):
    #return HttpResponse("Patient Login")
	return render(request,'PatientPortal/index.html',{})
# Create your views here.

def logina(request):
	context = RequestContext(request)
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email,password=password)
		try:
			p=patient.objects.get(user=user)
		except patient.DoesNotExist:
			p=None
		if empl:
			if user.is_active and p.validated :
				login(request,user)
				return HttpResponse("success")
				#return redirect(home)
			else:
				return HttpResponse("DISABLED")
		else:
			#HttpResponse("invaild")
			return redirect(tryagain)#redirect to invaild  username password url
	else:
		return redirect(patient_login)#redirect if not post request was send


@login_required
def register(request):
	context = RequestContext(request)
	if request.method == 'POST':
		email 		= request.POST['email']
		password 	= request.POST['password']
		fname 		= request.POST['fname']
		lname		= request.POST['lname']
		phno		= request.POST['phno']
		age 		= request.POST['age']
		user = User.objects.create_user(username=email,
                                 		email=email,
                                 		password=email)
		p=patient(user=user,
				  fname=fname,
				  lname=lname,
				  phno=phno,
				  age=age)
		sendOTP()
		#
		#return render(request,'PatientPortal/otp.html',{})
