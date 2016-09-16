#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import app,Bottle,route,run,request,template,static_file,redirect
import requests
import sesion
#from lxml import etree
from beaker.middleware import SessionMiddleware
import funciones

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



		return template("pass3.tpl",user=username,idproyecto=idproyecto,nombreproyecto=nombreproyecto,grupos=grupos,usuarios=usuarios)

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
        sesion.set("alumnos",alumnos)
        # Categorias
        r=requests.get(url_base+'/projects/'+idproyecto+'/issue_categories.json',auth=(username,password),verify=False)
        if r.status_code == 200:
        	doc=r.json()
        	categorias=doc["issue_categories"]
        
        
        if opcion=="grupo":
        	r=requests.get(url_base+'groups/'+grupo+'.json?include=users',auth=(username,password),verify=False)
        	if r.status_code == 200:
        		doc=r.json()
        		alumnos=[]
        		for user in doc["group"]["users"]:
        			alumnos.append(str(user["id"]))
        info={"tittle":"","desc":"","categoria":"-1","fecha2":"dd/mm/aaaa"}
        return template("pass4.tpl",user=username,idproyecto=idproyecto,nombreproyecto=nombreproyecto,categorias=categorias,error={},info=info)
        
@route('/step4',method="post") 
def step4():
	if not sesion.islogin():
		redirect("/")
	else:
		info={}
		username=sesion.get("user")
        password=sesion.get("pass")
        idproyecto=sesion.get("idproyecto")
        nombreproyecto=sesion.get("nombreproyecto")
        info["tittle"]=request.forms.get("tittle")
        info["desc"]=request.forms.get("desc")
        info["categoria"]=request.forms.get("categoria")
        info["fecha2"]=request.forms.get("fecha2")
        error={}
        
        #Comprobamos errores
        if info["tittle"]=="":
        	error["tittle"]="Debes indicar el título de la tarea."
        if info["desc"]=="":
        	error["desc"]="Debes indicar la descripción de la tarea."
        if info["fecha2"]=="dd/mm/aaaa":
        	info["fecha2"]=""
        else:
        	if not validateDateEs(info["fecha2"]):
        		error["fecha2"]="Debes indicar una fecha corecta"
        		info["fecha2"]=""
        	
        if len(error)>0:
        	return template("pass4.tpl",user=username,idproyecto=idproyecto,nombreproyecto=nombreproyecto,categorias=categorias,error=error,info=info)        

@route('/step2',method="get")
@route('/step3',method="get")
@route('/step4',method="get")
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

#import json
#import requests
#payload = {
#        'issue': {
#            'project_id': 24,
#            'subject': 'Prueba api',
#            'description': 'Prueba redmine api',
#            'category_id': 3,
#            'assigned_to_id': 85,
#            'due_date':'2016-09-29'#

#        }
#    }#

#parameters_json = json.dumps(payload)
#headers = {'Content-Type': 'application/json'}
#r = requests.post(url_base+'issues.json', auth=(username,password), data=parameters_json, headers=headers,verify=False)
#print r.status