from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flaskblog.models import User, Druzyny, Zawodnicy

from wtforms.fields.html5 import  DateField


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Pamiętaj mnie')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Nazwa uzytkownika',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')



class DodajDruzyne(FlaskForm):
    nazwa = StringField('Nazwa', validators=[DataRequired()])
    submit = SubmitField('Dodaj')

class DodajZawodnika(FlaskForm):
    imie = StringField('Imie', validators=[DataRequired()])
    nazwisko = StringField('Nazwisko', validators=[DataRequired()])
    nazwa_druzyny = StringField('Nazwa druzyny', validators=[DataRequired()])
    submit = SubmitField('Dodaj')

    def validate_nazwa_druzyny(self, nazwa_druzyny):
        druzyna = Druzyny.query.filter_by(nazwa=nazwa_druzyny.data).first()
        if druzyna:
            None
        else:
            raise ValidationError('Nie ma takiej druzyny wpisz poprawną')

class DodajMecz(FlaskForm):
    date = DateField('Data', validators=[DataRequired()])
    druzyna1 = StringField('Druzyna1', validators=[DataRequired()])
    druzyna2 = StringField('Druzyna2', validators=[DataRequired()])
    submit = SubmitField('Dodaj')

    def validate_druzyna1(self, druzyna1):
        druzyna = Druzyny.query.filter_by(nazwa=druzyna1.data).first()
        if druzyna:
            None
        else:
            raise ValidationError('Nie ma takiej druzyny wpisz poprawną')

    def validate_druzyna2(self, druzyna2):
        druzyna = Druzyny.query.filter_by(nazwa=druzyna2.data).first()
        if druzyna:
            None
        else:
            raise ValidationError('Nie ma takiej drużyny wpisz poprawną')




class WyszukajMecz1(FlaskForm):
    druzyna = StringField('Druzyna')

    submit = SubmitField('Szukaj')

    def validate_druzyna1(self, druzyna):
        druzyna = Druzyny.query.filter_by(nazwa=druzyna1.data).first()
        if druzyna:
            None
        else:
            raise ValidationError('Nie ma takiej druzyny wpisz poprawną')

class WyszukajMecz2(FlaskForm):
    imie = StringField('Imię')
    nazwisko = StringField('Nazwisko')

    submit = SubmitField('Szukaj')
    
    def validate_imie(self, imie):
        zawodnicy = Zawodnicy.query.filter_by(imie=imie.data).first()
        if zawodnicy:
            None
        else:
            raise ValidationError('Nie ma zawodnika z takim imieniem')

    def validate_nazwisko(self, nazwisko):
        zawodnicy = Zawodnicy.query.filter_by(nazwisko=nazwisko.data).first()
        if zawodnicy:
            None
        else:
            raise ValidationError('Nie ma zawodnika z takim nazwiskiem')

class WpiszZawodnika(FlaskForm):
    id_mecz = IntegerField('Id Meczu')
    druzyna = SelectField('Druzyna', coerce=int,choices=[(0, 'Gospodarze'), (1, 'Goscie')])
    id_zaw1 = IntegerField('Id zawodnika',
                           validators=[DataRequired()])
    id_zaw2 = IntegerField('Id zawodnika',
                           validators=[DataRequired()])
    id_zaw3 = IntegerField('Id zawodnika',
                           validators=[DataRequired()])
    id_zaw4 = IntegerField('Id zawodnika',
                           validators=[DataRequired()])
    id_zaw5 = IntegerField('Id zawodnika',
                           validators=[DataRequired()])
    


    submit = SubmitField('Dodaj')

    
class WpiszWynik(FlaskForm):
    id_mecz = IntegerField('Id Meczu', validators=[DataRequired()])

    set1_team1 = IntegerField('Wynik 1 setu gospodarzy', validators=[DataRequired(),NumberRange(0,21,'Wynik jest między 0 a 21')])
    set2_team1 = IntegerField('Wynik 2 setu gospodarzy', validators=[DataRequired(),NumberRange(0,21,'Wynik jest między 0 a 21')])
    set3_team1 = IntegerField('Wynik 3 setu gospodarzy', validators=[DataRequired(),NumberRange(0,21,'Wynik jest między 0 a 21')])
    set4_team1 = IntegerField('Wynik 4 setu gospodarzy')
    set5_team1 = IntegerField('Wynik 5 setu gospodarzy')
                           

    set1_team2 = IntegerField('Wynik 1 setnu gości', validators=[NumberRange(0,21,'Wynik jest między 0 a 21')])
    set2_team2 = IntegerField('Wynik 2 setnu gości', validators=[NumberRange(0,21,'Wynik jest między 0 a 21')])
    set3_team2 = IntegerField('Wynik 3 setnu gości', validators=[NumberRange(0,21,'Wynik jest między 0 a 21')])
    set4_team2 = IntegerField('Wynik 4 setnu gości')
    set5_team2 = IntegerField('Wynik 5 setnu gości')






    submit = SubmitField('Dodaj')

    


