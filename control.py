from SqlBaza import  Clan,Knjiga,Vrsta,Autor
from bottle import run, route, template,request,debug, get, request, redirect, post, static_file
import re
baza=Clan('baza.db')
baza1=Knjiga('baza.db')
baza2=Vrsta('baza.db')
baza3=Autor('baza.db')


@route('/')
def naslovna_stranica():
    return  template('pocetna')




@route('/login', method = "POST")
def login():
    email = request.forms.get('ime')
    pas = request.forms.get('pass')
    botun = request.forms.get('akcija')
    rb = request.forms.get('rb')
    global un
    Login.dodaj_tablicu(dbl.login_select())
    ispravan = Login.login_chek(username, password, rb)
    if ispravan:
        un = username
        if rb == 'A':
            return admin_izbornik()
        elif rb == 'N':
            return 'U izradi'
        else:
            return 'U izradi'

    else:
        un = None
        return "<p>Login failed.""</p>"
    if botun=='Prijava':

        return  redirect ('/moj_profil')
    else:
        return  redirect('/registracija')



@route('/moj_profil')
def profil_forma():
    return template('profil')


@route('/reg', method = "POST")
def reg():
    ime = request.forms.get('ime')
    prezime = request.forms.get('prezime')
    email = request.forms.get('email')
    pas = request.forms.get('password')
    password_conf=request.forms.get('password2')
    if(validacija_podataka(ime,prezime,email,pas,password_conf)):
        Clan.insert_Clan(ime,prezime,email,pas)
        redirect('/')
    else:
        return redirect('/registracija_losa')

def validacija_podataka(ime,prezime,email,pas,password_conf):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if  len(ime)<2:
        return False
    if not ime.isalpha():
        return False
    if len(prezime)<2:
        return  False
    if not prezime.isalpha():
        return  False
    if not re.search(regex,email):
        return False
    if password_conf!=pas:
        return False
    ime.title()
    prezime.title()
    return True


@route('/registracija')
def registracija_forma():
    return template('Regist')

@route('/registracija_losa')
def registracija_forma():
    return template('reg_losa')











if __name__=='__main__':
    run(reloader=True,port=8081)