import os
import secrets

from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.forms import  DodajDruzyne, DodajZawodnika, DodajMecz, WyszukajMecz1, WyszukajMecz2, WpiszZawodnika, WpiszWynik
from flask_login import login_user, current_user, logout_user, login_required

from flaskblog.models import User, Role, UserRoles
from flaskblog.models import Rozegrane_Mecze, Druzyny, Zawodnicy, Wyniki, Sklad_1, Sklad_2

@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
@app.route("/home")
def home():
    Mecze1 = Rozegrane_Mecze.query.order_by(Rozegrane_Mecze.date).all()
    druzyny = Druzyny.query.order_by(Druzyny.nazwa).all()

    
       
    return render_template('home.html',Mecze1=Mecze1, druzyny = druzyny)


@app.route("/mecz/<int:mecz_id>")
def mecz(mecz_id):
    mecz = Rozegrane_Mecze.query.get_or_404(mecz_id)
    if Sklad_1.query.filter_by(id_mecz=mecz_id).first() and Sklad_2.query.filter_by(id_mecz=mecz_id).first():
        zaw11 = Zawodnicy.query.filter_by(id = Sklad_1.query.filter_by(id_mecz=mecz_id).first().Zawodnik_1).first()
        zaw12 = Zawodnicy.query.filter_by(id = Sklad_1.query.filter_by(id_mecz=mecz_id).first().Zawodnik_2).first()
        zaw13 = Zawodnicy.query.filter_by(id = Sklad_1.query.filter_by(id_mecz=mecz_id).first().Zawodnik_3).first()
        zaw14 = Zawodnicy.query.filter_by(id = Sklad_1.query.filter_by(id_mecz=mecz_id).first().Zawodnik_4).first()
        zaw15 = Zawodnicy.query.filter_by(id = Sklad_1.query.filter_by(id_mecz=mecz_id).first().Zawodnik_5).first()

    
        zaw21 = Zawodnicy.query.filter_by(id = Sklad_2.query.filter_by(id_mecz=mecz_id).first().Zawodnik_1).first()
        zaw22 = Zawodnicy.query.filter_by(id = Sklad_2.query.filter_by(id_mecz=mecz_id).first().Zawodnik_2).first()
        zaw23 = Zawodnicy.query.filter_by(id = Sklad_2.query.filter_by(id_mecz=mecz_id).first().Zawodnik_3).first()
        zaw24 = Zawodnicy.query.filter_by(id = Sklad_2.query.filter_by(id_mecz=mecz_id).first().Zawodnik_4).first()
        zaw25 = Zawodnicy.query.filter_by(id = Sklad_2.query.filter_by(id_mecz=mecz_id).first().Zawodnik_5).first()

        test = 0
        if Wyniki.query.filter_by(id_mecz = mecz_id).first():
            Wynik1 = 0
            Wynik2 = 0
            Wynik = Wyniki.query.filter_by(id_mecz = mecz_id).first()
            set1_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set1_team1
            set2_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set2_team1
            set3_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set3_team1
            set4_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set4_team1
            set5_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set5_team1

            set1_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set1_team2
            set2_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set2_team2
            set3_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set3_team2
            set4_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set4_team2
            set5_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set5_team2

            if set1_team1 > set1_team2:
                Wynik1 += 1
            else:
                Wynik2+=1
            if set2_team1 > set2_team2:
                Wynik1 += 1
            else:
                Wynik2+=1
            if set3_team1 > set3_team2:
                Wynik1 += 1
            else:
                Wynik2+=1
            
            
            
            if Wynik1 >2 or Wynik2 > 2:
                None
            else:                         
                
                if set4_team1 > set4_team2:
                    Wynik1 += 1
                    test+=1
                else:
                    Wynik2+=1
                    test+=1
                    
                if Wynik1 >2 or Wynik2 > 2:
                    None
                else:
                    if set5_team1 > set5_team2:
                        Wynik1 += 1
                        test+=1
                    else:
                        Wynik2+=1
                        test+=1
            return render_template('mecz.html', mecz=mecz, wynik1 = Wynik1, wynik2 = Wynik2, wynik=Wynik, test=test,
                    zaw11=zaw11,zaw12=zaw12,zaw13=zaw13,zaw14=zaw14,zaw15=zaw15,zaw21=zaw21,zaw22=zaw22,zaw23=zaw23,zaw24=zaw24,zaw25=zaw25 )
        

        return render_template('mecz.html', mecz=mecz, 
                    zaw11=zaw11,zaw12=zaw12,zaw13=zaw13,zaw14=zaw14,zaw15=zaw15,zaw21=zaw21,zaw22=zaw22,zaw23=zaw23,zaw24=zaw24,zaw25=zaw25, test=test )
    elif Wyniki.query.filter_by(id_mecz = mecz_id).first():
        test = 0
        Wynik1 = 0
        Wynik2 = 0
        Wynik = Wyniki.query.filter_by(id_mecz = mecz_id).first()
        set1_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set1_team1
        set2_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set2_team1
        set3_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set3_team1
        set4_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set4_team1
        set5_team1 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set5_team1

        set1_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set1_team2
        set2_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set2_team2
        set3_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set3_team2
        set4_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set4_team2
        set5_team2 = Wyniki.query.filter_by(id_mecz = mecz_id).first().set5_team2

        if set1_team1 > set1_team2:
            Wynik1 += 1
        else:
            Wynik2+=1
        if set2_team1 > set2_team2:
            Wynik1 += 1
        else:
            Wynik2+=1
        if set3_team1 > set3_team2:
            Wynik1 += 1
        else:
            Wynik2+=1
        
        
        
        if Wynik1 >2 or Wynik2 > 2:
            None
        else:                         
            
            if set4_team1 > set4_team2:
                Wynik1 += 1
                test+=1
            else:
                Wynik2+=1
                test+=1
                
            if Wynik1 >2 or Wynik2 > 2:
                None
            else:
                if set5_team1 > set5_team2:
                    Wynik1 += 1
                    test+=1
                else:
                    Wynik2+=1
                    test+=1
        return render_template('mecz.html', mecz=mecz, wynik1 = Wynik1, wynik2 = Wynik2, wynik=Wynik, test=test)
    else:
         return render_template('mecz.html', mecz=mecz,)

@app.route("/druzyna/<int:druzyna_id>")
def druzyna(druzyna_id):
    druzyna = Druzyny.query.get_or_404(druzyna_id)
    czlonkowie = Zawodnicy.query.filter_by(id_druzyny = druzyna_id)
    nazwa_druzyny = Druzyny.query.filter_by(id = druzyna_id).first().nazwa

    Mecze1 = Rozegrane_Mecze.query.filter_by(druzyna1=nazwa_druzyny)
    Mecze2 = Rozegrane_Mecze.query.filter_by(druzyna2=nazwa_druzyny)


       

    return render_template('druzyna.html', druzyna=druzyna, czlonkowie=czlonkowie, mecze1 = Mecze1, mecze2 = Mecze2)
    #mecze1=Mecze1, mecze2=Mecze2)


@app.route("/zawodnik/<int:zawodnik_id>")
def zawodnik(zawodnik_id):
    zawodnik = Zawodnicy.query.get_or_404(zawodnik_id)
    idzaw = zawodnik.id_druzyny
    team = Druzyny.query.filter_by(id = idzaw).first().nazwa

    return render_template('zawodnik.html', zawodnik = zawodnik, team=team)



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)#.decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Nie udało się, sprawdź login i hasło', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))




@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)



###########################################################
##########      Dodawanie druzyn i meczu        ###########
###########################################################

@app.route("/nowa_druzyna", methods=['GET', 'POST'])
@login_required
def dodaj_druzyne():
    form = DodajDruzyne()
    if form.validate_on_submit():
        druzyny = Druzyny(nazwa=form.nazwa.data)
        db.session.add(druzyny)
        db.session.commit()
        flash('Dodałeś druzynę!', 'success')
        return redirect(url_for('account'))
    return render_template('dodaj_druzyne.html', title='Dodaj druzyne',
                           form=form, legend='dodaj druzyne')

@app.route("/nowy_zawodnik", methods=['GET', 'POST'])
@login_required
def dodaj_zawodnika():
    form = DodajZawodnika()
    if form.validate_on_submit():
        team_id = Druzyny.query.filter_by(nazwa=form.nazwa_druzyny.data).first().id
        zawodnik = Zawodnicy(imie=form.imie.data, nazwisko=form.nazwisko.data, id_druzyny=team_id)
        db.session.add(zawodnik)
        db.session.commit()
        flash('Dodales zawodnika', 'success')
        return redirect(url_for('account'))
    return render_template('dodaj_zawodnika.html', title='Dodaj zawodnika',
                           form=form, legend='dodaj zawodnika')


@app.route("/DodajMecz", methods=['GET', 'POST'])
@login_required
def dodaj_mecz():
    form = DodajMecz()
    if form.validate_on_submit():
        mecz = Rozegrane_Mecze(date=form.date.data, druzyna1=form.druzyna1.data, druzyna2=form.druzyna2.data)
        db.session.add(mecz)
        db.session.commit()
        flash('Dodales mecz', 'success')
        return redirect(url_for('account'))
    return render_template('dodaj_mecz.html', title='Dodaj Mecz',
                           form=form, legend='dodaj mecz')

'''
Kopia 
@app.route("/DodajMecz", methods=['GET', 'POST'])
@login_required
def dodaj_mecz():
    form = DodajMecz()
    if form.validate_on_submit():
        nazwa1 = form.druzyna1.data
        nazwa2 = form.druzyna2.data
        team_id1 = Druzyny.query.filter_by(nazwa = nazwa1).first().id
        team_id2 = Druzyny.query.filter_by(nazwa = nazwa2).first().id
        mecz = Rozegrane_Mecze(date=form.date.data, druzyna1=team_id1, druzyna2=team_id2)
        db.session.add(mecz)
        db.session.commit()
        flash('Dodales mecz', 'success')
        return redirect(url_for('account'))
    return render_template('dodaj_mecz.html', title='Dodaj Mecz',
                           form=form, legend='dodaj mecz')
'''

##################################################
##########      wyświetlanie        ##############
##################################################









@app.route('/dodajsklad', methods=['GET','POST'])
@login_required
def dodaj_sklad():
    form = WpiszZawodnika()
    if form.validate_on_submit():
        temp = form.druzyna.data
        
        if temp == 0:
            team_name = Rozegrane_Mecze.query.filter_by(id = form.id_mecz.data).first().druzyna1
            team_id = Druzyny.query.filter_by(nazwa=team_name).first().id
            zawodnicy = Sklad_1(id_mecz=form.id_mecz.data, id_druzyny=team_id,Zawodnik_1=form.id_zaw1.data, Zawodnik_2=form.id_zaw2.data,Zawodnik_3=form.id_zaw3.data,Zawodnik_4=form.id_zaw4.data,Zawodnik_5=form.id_zaw5.data)
            db.session.add(zawodnicy)
            db.session.commit()
            flash('Dodałeś zawodnikow!', 'success')
            return redirect(url_for('account'))
                

        else:

            team_name = Rozegrane_Mecze.query.filter_by(id = form.id_mecz.data).first().druzyna2
            team_id = Druzyny.query.filter_by(nazwa=team_name).first().id
            zawodnicy = Sklad_2(id_mecz=form.id_mecz.data, id_druzyny=team_id,Zawodnik_1=form.id_zaw1.data, Zawodnik_2=form.id_zaw2.data,Zawodnik_3=form.id_zaw3.data,Zawodnik_4=form.id_zaw4.data,Zawodnik_5=form.id_zaw5.data)
            db.session.add(zawodnicy)
            db.session.commit()
            flash('Dodałeś zawodnikow!', 'success')
            return redirect(url_for('account'))
    return render_template('dodaj_sklad.html', title='Dodaj druzyne',
                           form=form, legend='dodaj druzyne')

@app.route('/wpisz_wynik', methods=['GET','POST'])
@login_required
def wpisz_wynik():
    form = WpiszWynik()
    if form.validate_on_submit():
        set1_team1 = form.set1_team1.data
        set2_team1 = form.set2_team1.data
        set3_team1 = form.set3_team1.data
        set4_team1 = form.set4_team1.data
        set5_team1 = form.set5_team1.data

        set1_team2 = form.set1_team2.data
        set2_team2 = form.set2_team2.data
        set3_team2 = form.set3_team2.data
        set4_team2 = form.set4_team2.data
        set5_team2 = form.set5_team2.data
        
        Wynik1 = 0
        Wynik2 = 0
        temp = 0
        #set1
        if (set1_team1 != set1_team2) and (set1_team1 > set1_team2):
            Wynik1 += 1
        elif (set1_team1 != set1_team2) and (set1_team1 < set1_team2):
            Wynik2 += 1
        else:
            flash("Remis jest błędnym wynikiem w secie 1",'danger')
            temp +=1

        #set2
        if (set2_team1 != set2_team2) and (set2_team1 > set2_team2):
            Wynik1 += 1
        elif (set2_team1 != set2_team2) and (set2_team1 < set2_team2):
            Wynik2 += 1
        else:
            flash("Remis jest błędnym wynikiem w secie 2",'danger')
            temp +=1

        #set3
        if (set3_team1 != set3_team2) and (set3_team1 > set3_team2):
            Wynik1 += 1
        elif (set3_team1 != set3_team2) and (set3_team1 < set3_team2):
            Wynik2 += 1
        else:
            flash("Remis jest błędnym wynikiem w secie 3",'danger')
            temp +=1
        
        #4 set
        if Wynik1>2 or Wynik2> 2:
            if set4_team1 or set4_team2 != 0:
                flash('Niemożliwy wynik Meczu w secie 4. Jedna z drużyn już wygrała mecz. Wisz poprawny wynik', 'danger')
                temp +=1
        else:                
            if (set4_team1 != set4_team2) and (set4_team1 > set4_team2):
                Wynik1 += 1
            elif (set4_team1 != set4_team2) and (set4_team1 < set4_team2):
                Wynik2 += 1
            else:
                flash("Remis jest błędnym wynikiem w secie 4",'danger')
                temp +=1
        #5 set
        if Wynik1 >2 or Wynik2 > 2:
            if set5_team1 or set5_team1 != 0:
                flash('Niemożliwy wynik Meczu w secie 5. Jedna z drużyn już wygrała mecz. Wpisz poprawny wynik', 'danger')
                temp +=1
        else:                
            if (set5_team1 != set5_team2) and (set5_team1 > set5_team2):
                Wynik1 += 1
            elif (set5_team1 != set5_team2) and (set5_team1 < set5_team2):
                Wynik2 += 1
            else:
                flash("Remis jest błędnym wynikiem w secie 5",'danger')
                temp +=1
        
        

        wynik = Wyniki(id_mecz=form.id_mecz.data, set1_team1=set1_team1, set2_team1=set2_team1,set3_team1=set3_team1,set4_team1=set4_team1,set5_team1=set5_team1,
                        set1_team2=set1_team2,set2_team2=set2_team2,set3_team2=set3_team2,set4_team2=set4_team2,set5_team2=set5_team2)
        if temp < 1:
            db.session.add(wynik)
            db.session.commit()
        else:
            return redirect(url_for('wpisz_wynik'))

            
        
        return redirect(url_for('account'))
    return render_template('dodaj_wynik.html', title='Dodaj wynik',
                           form=form, legend='dodaj wynik')



