import json
from app import app, db, models, basedir
import sqlalchemy.exc as db_exc
from flask import render_template, request, redirect, url_for, flash, session, jsonify, abort, send_file
import io
from datetime import datetime


def get_support_info():
    return db.session.query(models.SuportInfo).all()


def get_nav_urls():
    return db.session.query(models.NavMenuMobile).all()


@app.route('/', methods=['get'])
def main():
    baners_id = db.session.query(models.Baners).with_entities(models.Baners.id).all()
    data = db.session.query(models.MainPage).get_or_404(1)
    news = db.session.query(models.News).with_entities(
        models.News.id,
        models.News.label,
        models.News.info,
        models.News.date
    ).all()[::-1][:3]
    return render_template('main.html', support=get_support_info(), baners=baners_id, data=data, news=news,
                           nav=get_nav_urls())


@app.route('/favicon.ico', methods=['get'])
def favicon():
    return redirect(location='/static/images/favicon32.ico', code=301)


@app.route('/connect', methods=['get'])
def connect_internet():
    return render_template('internet.html', support=get_support_info(), nav=get_nav_urls())


@app.route('/connect_statement', methods=['post'])
def connect_form():
    form = request.form
    for val in form.values():
        if len(val) > 5:
            break
    else:
        return render_template('success.html', support=get_support_info(), nav=get_nav_urls())
    try:
        db.session.add(
            models.Statements(
                area=form.get('area'),
                address=form.get('address'),
                name=form.get('name'),
                email=form.get('email'),
                phone=form.get('phone'),
                info=form.get('info'),
                date=datetime.now().strftime("%d-%m-%Y %H:%M")
            )
        )
        db.session.flush()
        db.session.commit()
        return render_template('success.html', support=get_support_info(), nav=get_nav_urls())

    except db_exc.SQLAlchemyError:
        db.session.rollback()
        return render_template('error.html', support=get_support_info(), nav=get_nav_urls())


@app.route('/kv/<path>', methods=['get'])
def internet_kv(path):
    page_data = db.session.query(models.Kv).filter(models.Kv.base_url == path).first()
    if not page_data:
        return redirect(url_for('main'))
    tarifs = list(map(lambda x: x, enumerate(json.loads(page_data.tariffs))))

    return render_template(
        'kv_connect_page.html', data=page_data, tarifs=tarifs, support=get_support_info(),
        templ=db.session.query(models.TemplateBaner).get(1), nav=get_nav_urls()
    )


@app.route('/home/<path>', methods=['get'])
def internet_home(path):
    page_data = db.session.query(models.Home).filter(models.Home.base_url == path).first()
    if not page_data:
        return redirect(url_for('main'))
    tarifs = list(map(lambda x: x, enumerate(json.loads(page_data.tariffs))))

    return render_template(
        'home_connect_page.html', data=page_data, tarifs=tarifs, support=get_support_info(),
        templ=db.session.query(models.TemplateBaner).get(2), nav=get_nav_urls()
    )


@app.route('/busines/<path>', methods=['get'])
def internet_busines(path):
    page_data = db.session.query(models.Busines).filter(models.Busines.base_url == path).first()
    if not page_data:
        return redirect(url_for('main'))

    return render_template(
        'busines_connect_page.html', data=page_data, support=get_support_info(),
        templ=db.session.query(models.TemplateBaner).get(3), nav=get_nav_urls()
    )


@app.route('/devices', methods=['get'])
def devices():
    devices_list = db.session.query(models.Devices).all()
    redir = request.args.get('url_redirect')
    return render_template('devices.html', support=get_support_info(), url_to_internet=redir, lst=devices_list,
                           nav=get_nav_urls())


@app.route('/conditions', methods=['get'])
def conditions():
    redir = request.args.get('url_redirect')
    cond = db.session.query(models.ConnectConditions).all()
    return render_template('conditions.html', support=get_support_info(), url_to_internet=redir, lst=cond,
                           nav=get_nav_urls())


@app.route('/advanced', methods=['get'])
def advanced():
    redir = request.args.get('url_redirect')
    adv_lst = db.session.query(models.Advanced).all()
    return render_template('advanced.html', support=get_support_info(), url_to_internet=redir, lst=adv_lst,
                           nav=get_nav_urls())


@app.route('/info', methods=['get'])
def info():
    info_blocks = db.session.query(models.Info).all()
    return render_template('info.html', support=get_support_info(), lst=info_blocks, nav=get_nav_urls())


@app.route('/kv/list', methods=['post'])
def ajax_list_kv():
    lst = []
    for page in db.session.query(models.Kv).all():
        lst.append({'name': page.name, 'url': f'/kv/{page.base_url}'})
    return jsonify(lst)


@app.route('/home/list', methods=['post'])
def ajax_list_home():
    lst = []
    for page in db.session.query(models.Home).all():
        lst.append({'name': page.name, 'url': f'/home/{page.base_url}'})
    return jsonify(lst)


@app.route('/busines/list', methods=['post'])
def ajax_list_busines():
    lst = []
    for page in db.session.query(models.Busines).all():
        lst.append({'name': page.name, 'url': f'/busines/{page.base_url}'})
    return jsonify(lst)


@app.route('/nav/list', methods=['post'])
def ajax_list_navigator():
    lst = []
    for nav in db.session.query(models.NavMenuMobile).all():
        if nav.name:
            lst.append({'name': nav.name, 'url': f'{nav.url}'})
    return jsonify(lst)


@app.route('/nav_desktop/list', methods=['post'])
def ajax_list_navigator_desktop():
    lst = []
    for nav in db.session.query(models.NavMenuDesktop).all():
        if nav.name:
            lst.append({'name': nav.name, 'url': f'{nav.url}'})
    return jsonify(lst)


@app.route('/ajax/<endpoint>', methods=['post'])
def ajax_get(endpoint: str):
    db_id = int(request.form['iid'])

    # отдаёт характеристики роутеров
    if endpoint == 'devices_list':
        res = db.session.query(models.Devices).get_or_404(db_id)
        return res.params.replace('\n', '<br>')

    abort(404)


@app.route('/img_baner/<int:iid>', methods=['get'])
def send_img_baner(iid):
    img = db.session.query(models.Baners).get_or_404(iid).img
    return send_file(io.BytesIO(img), download_name=f'baner_{iid}.png')


@app.route('/img_device/<int:iid>', methods=['get'])
def send_img_device(iid):
    img = db.session.query(models.Devices).get_or_404(iid).img
    return send_file(io.BytesIO(img), download_name=f'device_{iid}.png')


@app.route('/img_baner_business/<int:iid>', methods=['get'])
def send_img_business(iid):
    img = db.session.query(models.Busines).get_or_404(iid).img
    return send_file(io.BytesIO(img), download_name=f'baner_{iid}.png')


@app.route('/img_news/<int:iid>', methods=['get'])
def send_img_news(iid):
    img = db.session.query(models.News).get_or_404(iid).img
    return send_file(io.BytesIO(img), download_name=f'new_{iid}.png')










