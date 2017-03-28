#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import app,Bottle,route,run,request,template,static_file,redirect
import requests
import sesion
#from lxml import etree
from beaker.middleware import SessionMiddleware
import json

url_base="https://dit.gonzalonazareno.org/redmine/"

session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 300,
    #'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)


@route('/')
@route('/login',method="get")
def index():
    return template("pass1.tpl")

@route('/login',method="post") 
def login():
	username=request.forms.get("user_name")
	password=request.forms.get("user_password")
	r=requests.get(url_base+'projects.json',auth=(username,password),verify=False)
	if r.status_code == 200:
		doc=r.json()
		if len(doc["projects"])==1:
			return template('pass1.tpl',error=True)			
		else:
			sesion.set("user",username) 
        	sesion.set("pass",password)
        	return template("pass2.tpl",user=username,proyectos=doc["projects"])

@route('/step2',method="post") 
def step2():
	if not sesion.islogin():
		redirect("/")
	else:
		idproyecto=request.forms.get("proyecto")
		username=sesion.get("user")
		password=sesion.get("pass")
		sesion.set("idproyecto",idproyecto)
		#Nombre del proyecto
		r=requests.get(url_base+'projects/'+idproyecto+'.json',auth=(username,password),verify=False)
		if r.status_code == 200:
			doc=r.json()
			nombreproyecto=doc["project"]["name"]
			sesion.set("nombreproyecto",nombreproyecto)
		#Lista de grupos
		r=requests.get(url_base+'groups.json',auth=(username,password),verify=False)
		if r.status_code == 200:
			doc=r.json()
			grupos=doc["groups"]
		#Lista de usuarios del proyecto
		r=requests.get(url_base+'projects/'+idproyecto+'/memberships.json',auth=(username,password),verify=False)
		if r.status_code == 200:
			doc=r.json()
			usuarios=doc["memberships"]
		#Lista Categorias

        r=requests.get(url_base+'/projects/'+idproyecto+'/issue_categories.json',auth=(username,password),verify=False)
        if r.status_code == 200:
        	doc=r.json()
        	categorias=doc["issue_categories"]


		return template("pass3.tpl",user=username,idproyecto=idproyecto,nombreproyecto=nombreproyecto,grupos=grupos,usuarios=usuarios,categorias=categorias)

@route('/step3',method="post") 
def step3():
	if not sesion.islogin():
		redirect("/")
	else:
		opcion=request.forms.get("opcion")
		grupo=request.forms.get("grupo")
		alumnos=request.forms.getall("alumnos")
		username=sesion.get("user")
        password=sesion.get("pass")
        idproyecto=sesion.get("idproyecto")
        nombreproyecto=sesion.get("nombreproyecto")
        tittle=request.forms.get("tittle")
        desc=request.forms.get("desc")
        categoria=request.forms.get("categoria")
        fecha2=request.forms.get("fecha2")
        resultado=""
       
        if fecha2<>"":
        	lfecha=fecha2.split("/")
	        if len(lfecha[1])==1:
	        	lfecha[1]='0'+lfecha[1]
	        if len(lfecha[0])==1:
	        	lfecha[0]='0'+lfecha[0]
	        fecha2=lfecha[2]+"-"+lfecha[1]+"-"+lfecha[0]


        if opcion=="grupo":
        	r=requests.get(url_base+'groups/'+grupo+'.json?include=users',auth=(username,password),verify=False)
        	if r.status_code == 200:
        		doc=r.json()
        		alumnos=[]
        		for user in doc["group"]["users"]:
        			alumnos.append(str(user["id"]))
        

        resultado=""
        for alum in alumnos:
        	r=requests.get(url_base+'/users/'+alum+'.json',auth=(username,password),verify=False)
        	if r.status_code==200:
        		doc=r.json()
        		nombre=doc["user"]["firstname"]+" "+doc["user"]["lastname"]
        	payload = {'issue': {'project_id': idproyecto,'subject': tittle,'description': desc,'category_id': int(categoria),'assigned_to_id': int(alum),'due_date':fecha2}}
		print payload
        	parameters_json = json.dumps(payload)
        	headers = {'Content-Type': 'application/json'}
        	r = requests.post(url_base+'issues.json', auth=(username,password), data=parameters_json, headers=headers,verify=False)
        	resultado=resultado+nombre+":"+r.reason+"<br/>"
        return template("pass4.tpl",user=username,idproyecto=idproyecto,nombreproyecto=nombreproyecto,resultado=resultado)
 
       
@route('/step2',method="get")
@route('/step3',method="get")

def error():
	redirect("/login")

@route('/logout')
def do_logout():
    
    sesion.delete()
    redirect('/')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(app=app,host='localhost', port=8080,reloader=True)
