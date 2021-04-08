from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


##########################################################
###########         Użytkownicy         ##################
##########################################################


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


#########################################################################
#############       Baza danych informacji na stronę        #############
#########################################################################


class Druzyny(db.Model):
    __tablename__ = 'druzyny'
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Druzyny('{self.nazwa}')"

class Rozegrane_Mecze(db.Model):
    __tablename__ = 'rozegrane_mecze'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    druzyna1 = db.Column(db.String(20), db.ForeignKey('druzyny.id'), nullable=False)
    druzyna2 = db.Column(db.String(20), db.ForeignKey('druzyny.id'), nullable=False)

    def __repr__(self):
        return f"Rozegrane_Mecze('{self.date}', '{self.druzyna1}', '{self.druzyna2}')"



class Zawodnicy(db.Model):
    __tablename__ = 'zawodnicy'
    id = db.Column(db.Integer, primary_key=True)
    imie  = db.Column(db.String(50), unique=False)
    nazwisko = db.Column(db.String(50), unique=False)
    id_druzyny = db.Column(db.Integer, db.ForeignKey('druzyny.id'))

    def __repr__(self):
        return f"Zawodnicy('{self.imie}', '{self.nazwisko}', '{self.id_druzyny}')"

class Wyniki(db.Model):
    __tablename__ = 'wyniki'
    id = db.Column(db.Integer, primary_key=True)
    id_mecz = db.Column(db.Integer, db.ForeignKey('rozegrane_mecze.id'))

    set1_team1 = db.Column(db.Integer)
    set2_team1 = db.Column(db.Integer)
    set3_team1 = db.Column(db.Integer)
    set4_team1 = db.Column(db.Integer)
    set5_team1 = db.Column(db.Integer)

    set1_team2 = db.Column(db.Integer)
    set2_team2 = db.Column(db.Integer)
    set3_team2 = db.Column(db.Integer)
    set4_team2 = db.Column(db.Integer)
    set5_team2 = db.Column(db.Integer)

    def __repr__(self):
        return f"Wyniki('{self.set1_team1}','{self.set2_team1}','{self.set3_team1}','{self.set4_team1}','{self.set5_team1}','{self.set1_team2}','{self.set2_team2}',{self.set3_team2}',{self.set4_team2}','{self.set5_team2}')"

class Sklad_1(db.Model):
    __tablename__ = 'sklad_1'
    id = db.Column(db.Integer, primary_key=True)
    id_mecz = db.Column(db.Integer, db.ForeignKey('rozegrane_mecze.id'))
    id_druzyny = db.Column(db.Integer, db.ForeignKey('druzyny.id'))

    Zawodnik_1 = db.Column(db.Integer, nullable=False)
    Zawodnik_2 = db.Column(db.Integer, nullable=False) 
    Zawodnik_3 = db.Column(db.Integer, nullable=False) 
    Zawodnik_4 = db.Column(db.Integer, nullable=False) 
    Zawodnik_5 = db.Column(db.Integer, nullable=False) 

    def __repr__(self):
        return f"Sklad_1('{self.id_druzyny}', '{self.Zawodnik_1}', '{self.Zawodnik_2}', '{self.Zawodnik_3}','{self.Zawodnik_4}', '{self.Zawodnik_5}')"

class Sklad_2(db.Model):
    __tablename__ = 'sklad_2'
    id = db.Column(db.Integer, primary_key=True)
    id_mecz = db.Column(db.Integer, db.ForeignKey('rozegrane_mecze.id'))
    id_druzyny = db.Column(db.Integer, db.ForeignKey('druzyny.id'))

    Zawodnik_1 = db.Column(db.Integer, nullable=False)
    Zawodnik_2 = db.Column(db.Integer, nullable=False) 
    Zawodnik_3 = db.Column(db.Integer, nullable=False) 
    Zawodnik_4 = db.Column(db.Integer, nullable=False) 
    Zawodnik_5 = db.Column(db.Integer, nullable=False) 

    def __repr__(self):
        return f"Sklad_1('{self.id_druzyny}', '{self.Zawodnik_1}', '{self.Zawodnik_2}', '{self.Zawodnik_3}'','{self.Zawodnik_4}', '{self.Zawodnik_5}')"

