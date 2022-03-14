import imp
from turtle import color
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from .forms import  Reg_marriage_Form
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.db.models import Sum, Count, Case, When
from django.contrib import messages
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter


def home(request):
	return render(request, "base.html")
@login_required(login_url='/login/')
def reg_home(request):
	#current_user=request.user
	
	data = Reg_marriage.objects.values()
	print(type(data))
	print(data)
	#contex ={"data":data}
	#contex0 ={"data":data}
	data ={"data":data}
	if request.method == 'GET':
		search_term0 = request.GET.get('p')
		search_term = request.GET.get('q')
		single_person = public.objects.all().filter(nid=search_term) 
		single_person0 = public.objects.all().filter(nid=search_term0) 
		contex ={"sp":single_person,'sp0':single_person0}
		return render(request,'mainapp/reg_home.html', data)
	else:
		return render(request, "mainapp/reg_home.html",data)



@login_required(login_url='/login/')  
def reg_mar(request):
	if request.method == "POST":
		g_nid = request.POST['groom_nid']
		b_nid = request.POST['bride_nid']
		data = Reg_marriage_Form(request.POST)
		if data.is_valid():
			public.objects.filter(nid = g_nid).update(status = "married")
			public.objects.filter(nid = b_nid).update(status = "married")
			data.save()
		return redirect("/reg_home/")
	else: 
		data= Reg_marriage_Form()
	
	return render(request, "mainapp/reg_marriage.html", {"forms": data})


def sorry(request):
	return render(request, "mainapp/sorry.html")


def searchbar(request):
	data ={}
	if request.method == 'GET':
		search_term = request.GET.get('q')
		single_person= public.objects.all().filter(nid=search_term) 
		data ={"single_person":single_person}
		print(data)
		return render(request,'mainapp/searchbar.html', data)
	else :
		return render(request,'mainapp/notfound.html')

def detail(request,pk):
	mar_id = Reg_marriage.objects.get(registration_num=pk)
	context = {
		'mar_id':mar_id
	}
	print(context)
	return render(request,'mainapp/detail.html',context)



def reg_sign_in(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(reg_home)
			else:
				messages.error(request, messages.INFO,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"mainapp/login.html",{"login_form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")

def c_pdf(request,pk):
	buf = io.BytesIO()
	c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
	c.setStrokeColor(colors.green)
	c.setFillColor(colors.green)
	c.rect(0,0,900,100,stroke=1,fill=1)
	x = c._pagesize[0] / 2
	textobj = c.beginText()
	textobj.setTextOrigin(x-200,300)
	textobj.setFont("Helvetica",14)
	lines=[]
	mar_id = Reg_marriage.objects.get(registration_num=pk)
	
	lines.append("Registration Num: "+str(mar_id.registration_num))
	lines.append("Groom Name: "+str(mar_id.groom_name))
	lines.append("Groom's Nid: "+str(mar_id.groom_nid))
	lines.append("Bride Name: "+str(mar_id.bride_name))
	lines.append("Bride's Nid: "+str(mar_id.bride_nid))
	lines.append("Marriage Date & Time: "+str(mar_id.marriage_date))
	lines.append("Marriage Fee: "+str(mar_id.marriage_fee))
	lines.append(" ")
	for line in lines:
		textobj.textLine(line)
	c.drawText(textobj)
	c.showPage()
	c.save()
	buf.seek(0)
	 
	return FileResponse(buf,as_attachment=True,filename='certificate.pdf')