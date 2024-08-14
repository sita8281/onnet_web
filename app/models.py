from app import db


class Kv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    base_url = db.Column(db.String(150), unique=True)
    metrica_html = db.Column(db.String(300))
    zone_html = db.Column(db.String(300))
    header_html = db.Column(db.String(300))
    tariffs = db.Column(db.String(300))


class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    base_url = db.Column(db.String(150), unique=True)
    metrica_html = db.Column(db.String(300))
    zone_html = db.Column(db.String(300))
    header_html = db.Column(db.String(300))
    tariffs = db.Column(db.String(300))


class Busines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    base_url = db.Column(db.String(150), unique=True)
    metrica_html = db.Column(db.String(300))
    zone_html = db.Column(db.String(300))
    header_html = db.Column(db.String(300))
    label = db.Column(db.String(100))
    info = db.Column(db.String(300))
    img = db.Column(db.LargeBinary)


class StaticInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    base_url = db.Column(db.String(150), unique=True)
    info = db.Column(db.String(300))


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100))
    label = db.Column(db.String(100))
    info = db.Column(db.String(300))
    img = db.Column(db.LargeBinary)


class Advanced(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    price = db.Column(db.String(50))


class Baners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary)


class SuportInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(100))
    view = db.Column(db.String(50))


class TemplateBaner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    label = db.Column(db.String(100))
    check1 = db.Column(db.String(100))
    check2 = db.Column(db.String(100))
    check3 = db.Column(db.String(100))
    check4 = db.Column(db.String(100))
    label_tarif = db.Column(db.String(100))
    label_zone = db.Column(db.String(100))


class ConnectConditions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100))
    info = db.Column(db.String(300))
    img = db.Column(db.LargeBinary)


class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(50))
    name = db.Column(db.String(100))
    info = db.Column(db.String(300))
    params = db.Column(db.String(300))
    img = db.Column(db.LargeBinary)


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100))
    url = db.Column(db.String(200))
    name_url = db.Column(db.String(100))
    info = db.Column(db.String(300))


class MainPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label1 = db.Column(db.String(100))
    label2 = db.Column(db.String(100))
    html_header = db.Column(db.Text)
    html_zone = db.Column(db.Text)


class Statements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(150))
    address = db.Column(db.String(150))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    info = db.Column(db.String(200))
    date = db.Column(db.String(50))


class NavMenuMobile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(200))


class NavMenuDesktop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(200))


class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    passw = db.Column(db.Text)








