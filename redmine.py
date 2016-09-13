from bottle import app,Bottle,route,run,request,template,static_file,redirect
import requests
import sesion
#from lxml import etree
from beaker.middleware import SessionMiddleware

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
	r=requests.get('https://dit.gonzalonazareno.org/redmine/projects.json',auth=(username,password),verify=False)
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
		r=requests.get('https://dit.gonzalonazareno.org/redmine/projects/'+idproyecto+'.json',auth=(username,password),verify=False)
		if r.status_code == 200:
			doc=r.json()
			nombreproyecto=doc["project"]["name"]
		#Lista de grupos
		r=requests.get('https://dit.gonzalonazareno.org/redmine/groups.json',auth=(username,password),verify=False)
		if r.status_code == 200:
			doc=r.json()
			grupos=doc["groups"]
		#Lista de usuarios del proyecto
		r=requests.get('https://dit.gonzalonazareno.org/redmine/projects/'+idproyecto+'/memberships.json',auth=(username,password),verify=False)
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

		return alumnos

@route('/logout')
def do_logout():
    
    sesion.delete()
    redirect('/')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

run(app=app,host='localhost', port=8080,reloader=True)
