from app import app, auth, db, models, basedir
from flask import render_template, request, redirect, url_for, send_file
from werkzeug.security import generate_password_hash
import sqlalchemy.exc as db_exc
import json
import io
import base64


@app.route('/admin_panel')
@auth.login_required
def admin_panel():
    return render_template('admin_panel/menu.html')


@app.route('/admin_panel/kv/list')
@auth.login_required
def kv_list():

    # костыльный преобразователь json строки
    def replace(s):
        db_s = s
        t = json.loads(s.tariffs)
        db_s.tariffs = t
        return db_s
    kv_lst = db.session.query(models.Kv).all()
    lst = list(map(replace, kv_lst))

    return render_template('admin_panel/kv_list.html', kv_list=lst,)


@app.route('/admin_panel/kv/add', methods=['post', 'get'])
@auth.login_required
def kv_add():
    if request.method == 'POST':
        form = request.json
        try:
            db.session.add(
                models.Kv(
                    name=form['name'],
                    base_url=form['url'],
                    metrica_html=form['metric'],
                    zone_html=form['zone'],
                    header_html=form['header'],
                    tariffs=json.dumps(form['tarif'])
                )
            )
            db.session.flush()
            db.session.commit()
            return 'Новая страница успешно добавлена'
        except db_exc.IntegrityError:
            db.session.rollback()
            return 'Такая ссылка уже существует!'
        except db_exc.SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка БД'
    else:
        return render_template('admin_panel/kv_form_add.html')


@app.route('/admin_panel/kv/update/<int:iid>', methods=['post', 'get'])
@auth.login_required
def kv_update(iid: int):
    obj = db.session.query(models.Kv).get_or_404(iid)
    if request.method == 'POST':
        form = request.json
        if form.get('tarifs'):
            return obj.tariffs
        try:
            obj.name = form['name']
            obj.base_url = form['url']
            obj.metrica_html = form['metric']
            obj.zone_html = form['zone']
            obj.header_html = form['header']
            obj.tariffs = json.dumps(form['tarif'])
            db.session.flush()
            db.session.commit()
            return 'Данные успешно изменены'
        except db_exc.IntegrityError:
            db.session.rollback()
            return 'Такая ссылка уже существует!'
        except db_exc.SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка БД'
    else:
        obj.tariffs = json.loads(obj.tariffs)
        return render_template('admin_panel/kv_form_update.html', data=obj)


@app.route('/admin_panel/kv/del/<int:iid>', methods=['get'])
@auth.login_required
def kv_del(iid: int):
    page = db.session.query(models.Kv).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('kv_list'))


@app.route('/admin_panel/home/list')
@auth.login_required
def home_list():

    # костыльный преобразователь json строки
    def replace(s):
        db_s = s
        t = json.loads(s.tariffs)
        db_s.tariffs = t
        return db_s
    home_lst = db.session.query(models.Home).all()
    lst = list(map(replace, home_lst))

    return render_template('admin_panel/home_list.html', home_list=lst,)


@app.route('/admin_panel/home/add', methods=['post', 'get'])
@auth.login_required
def home_add():
    if request.method == 'POST':
        form = request.json
        try:
            db.session.add(
                models.Home(
                    name=form['name'],
                    base_url=form['url'],
                    metrica_html=form['metric'],
                    zone_html=form['zone'],
                    header_html=form['header'],
                    tariffs=json.dumps(form['tarif'])
                )
            )
            db.session.flush()
            db.session.commit()
            return 'Новая страница успешно добавлена'
        except db_exc.IntegrityError:
            db.session.rollback()
            return 'Такая ссылка уже существует!'
        except db_exc.SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка БД'
    else:
        return render_template('admin_panel/home_form_add.html')


@app.route('/admin_panel/home/update/<int:iid>', methods=['post', 'get'])
@auth.login_required
def home_update(iid: int):
    obj = db.session.query(models.Home).get_or_404(iid)
    if request.method == 'POST':
        form = request.json
        if form.get('tarifs'):
            return obj.tariffs
        try:
            obj.name = form['name']
            obj.base_url = form['url']
            obj.metrica_html = form['metric']
            obj.zone_html = form['zone']
            obj.header_html = form['header']
            obj.tariffs = json.dumps(form['tarif'])
            db.session.flush()
            db.session.commit()
            return 'Данные успешно изменены'
        except db_exc.IntegrityError:
            db.session.rollback()
            return 'Такая ссылка уже существует!'
        except db_exc.SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка БД'
    else:
        obj.tariffs = json.loads(obj.tariffs)
        return render_template('admin_panel/home_form_update.html', data=obj)


@app.route('/admin_panel/home/del/<int:iid>', methods=['get'])
@auth.login_required
def home_del(iid: int):
    page = db.session.query(models.Home).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('home_list'))


@app.route('/admin_panel/adv/list', methods=['get'])
@auth.login_required
def adv_list():
    """Получить список доп.услуг"""

    all_adv = db.session.query(models.Advanced).all()
    return render_template('admin_panel/adv_list.html', lst=all_adv)


@app.route('/admin_panel/adv/add', methods=['post'])
@auth.login_required
def adv_add():
    """Добавить новую доп.услугу"""
    try:
        db.session.add(
            models.Advanced(
                name=request.form['name'],
                price=request.form['price']
            )
        )
        db.session.flush()
        db.session.commit()
        return redirect(url_for('adv_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('adv_list'))


@app.route('/admin_panel/adv/del/<int:iid>', methods=['get'])
@auth.login_required
def adv_del(iid: int):
    """Удалить доп.услугу"""

    page = db.session.query(models.Advanced).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('adv_list'))


@app.route('/admin_panel/busines/list')
@auth.login_required
def busines_list():
    busines_lst = db.session.query(models.Busines).all()
    return render_template('admin_panel/busines_list.html', busines_list=busines_lst,)


@app.route('/admin_panel/busines/img/<int:iid>')
@auth.login_required
def busines_img(iid: int):
    image = db.session.query(models.Busines).get_or_404(iid)
    return send_file(io.BytesIO(image.img), download_name=str(iid))


@app.route('/admin_panel/busines/add', methods=['post', 'get'])
@auth.login_required
def busines_add():
    if request.method == 'POST':
        form = request.json
        try:
            db.session.add(
                models.Busines(
                    name=form['name'],
                    base_url=form['url'],
                    metrica_html=form['metric'],
                    zone_html=form['zone'],
                    info=form['info'],
                    label=form['label'],
                    img=base64.b64decode(form['img'].split(',')[1]),
                    header_html=form['header']
                )
            )
            db.session.flush()
            db.session.commit()
            return 'Новая страница успешно добавлена'
        except db_exc.IntegrityError:
            db.session.rollback()
            return 'Такая ссылка уже существует!'
        except db_exc.SQLAlchemyError as e:
            db.session.rollback()
            return 'Ошибка БД'
    else:
        return render_template('admin_panel/busines_form_add.html')


@app.route('/admin_panel/busines/update/<int:iid>', methods=['post', 'get'])
@auth.login_required
def busines_update(iid: int):
    obj = db.session.query(models.Busines).get_or_404(iid)
    if request.method == 'POST':
        form = request.json
        try:
            obj.name = form['name']
            obj.base_url = form['url']
            obj.metrica_html = form['metric']
            obj.zone_html = form['zone']
            obj.header_html = form['header']
            obj.label = form['label']
            obj.info = form['info']
            if form['img']:
                obj.img = base64.b64decode(form['img'].split(',')[1])
            db.session.flush()
            db.session.commit()
            return 'Данные успешно изменены'
        except db_exc.IntegrityError:
            db.session.rollback()
            return 'Такая ссылка уже существует!'
        except db_exc.SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка БД'
    else:
        return render_template('admin_panel/busines_form_update.html', data=obj)


@app.route('/admin_panel/busines/del/<int:iid>', methods=['get'])
@auth.login_required
def busines_del(iid: int):
    page = db.session.query(models.Busines).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('busines_list'))


#
#
#
# работа с банерными картинками в БД
#


@app.route('/admin_panel/baner/list', methods=['get'])
@auth.login_required
def baner_list():
    """Получить список картинок"""

    images_list = db.session.query(models.Baners).with_entities(models.Baners.id).all()
    return render_template('admin_panel/baner_list.html', lst=list(images_list))


@app.route('/admin_panel/baner/<int:iid>', methods=['get'])
@auth.login_required
def baner_get(iid: int):
    """Получить список картинок"""

    image = db.session.query(models.Baners).get_or_404(iid)
    return send_file(io.BytesIO(image.img), download_name=str(iid))


@app.route('/admin_panel/baner/add', methods=['post'])
@auth.login_required
def baner_add():
    """Добавить новую картинку"""
    file = request.files.get('file')
    try:
        db.session.add(
            models.Baners(
                img=file.stream.read()
            )
        )
        db.session.flush()
        db.session.commit()
        return redirect(url_for('baner_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('baner_list'))


@app.route('/admin_panel/baner/del/<int:iid>', methods=['get'])
@auth.login_required
def baner_del(iid: int):
    """Удалить картинку"""

    page = db.session.query(models.Baners).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('baner_list'))


#
#
# изменение статичных данных: телефон, почта, телега, вотсап
#

@app.route('/admin_panel/support', methods=['get', 'post'])
@auth.login_required
def admin_panel_support():
    rows = db.session.query(models.SuportInfo).all()

    if request.method == 'POST':
        form = request.form

        try:
            rows[0].url = form['url_phone']
            rows[0].view = form['phone']
            rows[1].url = form['url_mail']
            rows[1].view = form['mail']
            rows[2].url = form['url_telegram']
            rows[2].view = form['telegram']
            rows[3].url = form['url_whatsapp']
            rows[3].view = form['whatsapp']

            db.session.flush()
            db.session.commit()

        except db_exc.SQLAlchemyError:
            db.session.rollback()

        return redirect(url_for('admin_panel_support'))

    support_list = db.session.query(models.SuportInfo).all()
    return render_template('/admin_panel/support_list.html', lst=support_list)

#
#
# изменение шаблонов банеров страниц подключений
#


@app.route('/admin_panel/temp_baners', methods=['get', 'post'])
@auth.login_required
def admin_panel_temp_baners():
    rows = db.session.query(models.TemplateBaner).all()

    if request.method == 'POST':
        form = request.form

        try:
            row = rows[int(form['ident'])-1]
            row.label = form['label']
            row.check1 = form['check1']
            row.check2 = form['check2']
            row.check3 = form['check3']
            row.check4 = form['check4']
            row.label_tarif = form['label_tarif']
            row.label_zone = form['label_zone']

            db.session.flush()
            db.session.commit()

        except db_exc.SQLAlchemyError:
            db.session.rollback()

        return redirect(url_for('admin_panel_temp_baners'))

    support_list = db.session.query(models.TemplateBaner).all()
    return render_template('/admin_panel/temp_baners.html', lst=rows)


#
#
# изменение данных на главной странице
#

@app.route('/admin_panel/templ_main', methods=['get', 'post'])
@auth.login_required
def templ_main():
    data = db.session.query(models.MainPage).get_or_404(1)

    if request.method == 'POST':
        form = request.form

        try:
            data.label1 = form['label-1']
            data.label2 = form['label-2']
            data.html_header = form['html_header']
            data.html_zone = form['html_zone']

            db.session.flush()
            db.session.commit()

        except db_exc.SQLAlchemyError:
            db.session.rollback()

        return redirect(url_for('templ_main'))

    return render_template('/admin_panel/templ_main.html', data=data)

#
#
#
# работа с новостями
#


@app.route('/admin_panel/news/list', methods=['get'])
@auth.login_required
def news_list():
    """Получить список новостей"""

    news = db.session.query(models.Baners).with_entities(
        models.News.id,
        models.News.label,
        models.News.info,
    ).all()
    return render_template('admin_panel/news_list.html', lst=news)


@app.route('/admin_panel/news/img/<int:iid>', methods=['get'])
@auth.login_required
def news_get_img(iid: int):
    """Получить картинку из нововсти"""

    news = db.session.query(models.News).get_or_404(iid)
    return send_file(io.BytesIO(news.img), download_name=str(iid))


@app.route('/admin_panel/news/add', methods=['post'])
@auth.login_required
def news_add():
    """Добавить новость"""
    file = request.files.get('file').stream.read()
    if not file:
        with open(file=basedir + '\\static\\images\\empty_img.png', mode='rb') as f:
            file = f.read()
    form = request.form
    try:
        db.session.add(
            models.News(
                label=form['label'],
                info=form['info'],
                date=form['date'],
                img=file
            )
        )
        db.session.flush()
        db.session.commit()
        return redirect(url_for('news_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('news_list'))


@app.route('/admin_panel/news/del/<int:iid>', methods=['get'])
@auth.login_required
def news_del(iid: int):
    """Удалить новость"""

    page = db.session.query(models.News).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('news_list'))


#
#
#
# работа со списком роутеров


@app.route('/admin_panel/device/list', methods=['get'])
@auth.login_required
def device_list():
    """Получить список роутеров"""

    devices = db.session.query(models.Devices).with_entities(
        models.Devices.id,
        models.Devices.price,
        models.Devices.info,
        models.Devices.name,
        models.Devices.params,
        models.Devices.img,
    ).all()
    return render_template('admin_panel/device_list.html', lst=devices)


@app.route('/admin_panel/device/img/<int:iid>', methods=['get'])
@auth.login_required
def device_get_img(iid: int):
    """Получить картинку роутера"""
    device = db.session.query(models.Devices).get_or_404(iid)
    return send_file(io.BytesIO(device.img), download_name=str(iid))


@app.route('/admin_panel/device/add', methods=['post'])
@auth.login_required
def device_add():
    """Добавить роутер"""
    file = request.files.get('file')
    form = request.form
    try:
        db.session.add(
            models.Devices(
                price=form['price'],
                name=form['name'],
                info=form['info'],
                params=form['params'],
                img=file.stream.read()
            )
        )
        db.session.flush()
        db.session.commit()
        return redirect(url_for('device_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('device_list'))


@app.route('/admin_panel/device/del/<int:iid>', methods=['get'])
@auth.login_required
def device_del(iid: int):
    """Удалить роутер"""

    device = db.session.query(models.Devices).get_or_404(iid)
    try:
        db.session.delete(device)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('device_list'))


#
#
#
# работа с условиями подключения


@app.route('/admin_panel/conditions/list', methods=['get'])
@auth.login_required
def conditions_list():
    """Получить список с условиями"""

    conditions = db.session.query(models.ConnectConditions).with_entities(
        models.ConnectConditions.id,
        models.ConnectConditions.label,
        models.ConnectConditions.info,
    ).all()
    return render_template('admin_panel/conditions_list.html', lst=conditions)


@app.route('/admin_panel/conditions/add', methods=['post'])
@auth.login_required
def conditions_add():
    """Добавить условие"""
    form = request.form
    try:
        db.session.add(
            models.ConnectConditions(
                label=form['label'],
                info=form['info'],
            )
        )
        db.session.flush()
        db.session.commit()
        return redirect(url_for('conditions_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('conditions_list'))


@app.route('/admin_panel/conditions/del/<int:iid>', methods=['get'])
@auth.login_required
def conditions_del(iid: int):
    """Удалить условие"""

    cond = db.session.query(models.ConnectConditions).get_or_404(iid)
    try:
        db.session.delete(cond)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('conditions_list'))


#
#
#
# редактирование информации
#

@app.route('/admin_panel/info/list', methods=['get'])
@auth.login_required
def info_list():
    """Получить список блоков инфы"""

    all_info = db.session.query(models.Info).all()
    return render_template('admin_panel/info_list.html', lst=all_info)


@app.route('/admin_panel/info/add', methods=['post'])
@auth.login_required
def info_add():
    """Добавить блок информации"""
    try:
        db.session.add(
            models.Info(
                label=request.form['label'],
                info=request.form['info'],
                url=request.form['html_code']
            )
        )
        db.session.flush()
        db.session.commit()
        return redirect(url_for('info_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('info_list'))


@app.route('/admin_panel/info/del/<int:iid>', methods=['get'])
@auth.login_required
def info_del(iid: int):
    """Удалить блок информации"""

    page = db.session.query(models.Info).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('info_list'))


#
#
#
# редактирование заявок
#

@app.route('/admin_panel/statements/list', methods=['get'])
@auth.login_required
def statements_list():
    """Получить список заявок"""

    all_info = db.session.query(models.Statements).all()
    return render_template('admin_panel/statements.html', lst=all_info)


@app.route('/admin_panel/statements/del/<int:iid>', methods=['get'])
@auth.login_required
def statement_del(iid: int):
    """Удалить заявку"""

    page = db.session.query(models.Statements).get_or_404(iid)
    try:
        db.session.delete(page)
        db.session.commit()
    except db_exc.SQLAlchemyError:
        pass
    return redirect(url_for('statements_list'))


#
#
# NAV-bar list Mobile
#

@app.route('/admin_panel/nav/list', methods=['get'])
@auth.login_required
def nav_list():
    """Получить список ссылок"""

    all_adv = db.session.query(models.NavMenuMobile).all()
    return render_template('admin_panel/nav_bar_list.html', lst=all_adv)


@app.route('/admin_panel/nav/add', methods=['post'])
@auth.login_required
def nav_add():
    """Добавить новую ссылку"""

    form = request.form

    try:
        for i in range(1, 10):
            nav = db.session.query(models.NavMenuMobile).get(i)
            nav.name = form.get(f'name-{i}')
            nav.url = form.get(f'url-{i}')
        db.session.flush()
        db.session.commit()
        return redirect(url_for('nav_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('nav_list'))


#
#
# NAV-bar list Desktop
#

@app.route('/admin_panel/nav_desktop/list', methods=['get'])
@auth.login_required
def nav_desktop_list():
    """Получить список ссылок"""

    all_adv = db.session.query(models.NavMenuDesktop).all()
    return render_template('admin_panel/nav_bar_desktop_list.html', lst=all_adv)


@app.route('/admin_panel/nav_desktop/add', methods=['post'])
@auth.login_required
def nav_desktop_add():
    """Добавить новую ссылку"""

    form = request.form

    try:
        for i in range(1, 10):
            nav = db.session.query(models.NavMenuDesktop).get(i)
            nav.name = form.get(f'name-{i}')
            nav.url = form.get(f'url-{i}')
        db.session.flush()
        db.session.commit()
        return redirect(url_for('nav_desktop_list'))
    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return redirect(url_for('nav_desktop_list'))


@app.route('/admin_panel/users', methods=['GET'])
@auth.login_required
def users_list():
    users = db.session.query(models.AdminUser).all()
    return render_template('admin_panel/users.html', users=users)


@app.route('/admin_panel/add_user', methods=['POST'])
@auth.login_required
def add_user():
    name = request.form.get('username')
    passw = request.form.get('password')
    if all([name, passw]):
        db.session.add(
            models.AdminUser(
                name=name,
                passw=generate_password_hash(passw)
            )
        )
        try:
            db.session.flush()
            db.session.commit()
        except db_exc.SQLAlchemyError:
            db.session.rollback()
            return f'Не удалось создать нового пользователя с именем: <{name}>'
    return redirect(url_for('users_list'))


@app.route('/admin_panel/del_user/<int:id>', methods=['GET'])
@auth.login_required
def del_user(id: int):
    user = db.session.query(models.AdminUser).get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
    finally:
        return redirect(url_for('users_list'))
    
