from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from config.sqlalchemy_config import db_session, Jobs

app = Flask(__name__)
CORS().init_app(app)


# 展示信息
@app.route('/chat/<id>', methods=['GET'])
def chat(id):
    if request.method == 'GET':
        i = db_session.query(Jobs).filter(Jobs.id == int(id)).first()
        print(i)
        infos = {
            'recLogo': i.recLogo,

            'areaCodeName': i.areaCodeName,
            'jobName': i.jobName,
            'lowMonthPay': i.lowMonthPay,

            'degreeName': i.degreeName,
            'highMonthPay': i.highMonthPay,
            'headCount': i.headCount,
            'major': i.major,


            'updateDate': i.updateDate,
            'publishDate': i.publishDate,

            'recName': i.recName,
            'recProperty': i.recProperty,
            'recScale': i.recScale,


            'recTags': i.recTags,


        }
        return render_template('chat.html', infos=infos)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':

        # 搜索
        try:
            name = str(request.get_json()['input_chaxun'])
            infos = db_session.query(Jobs).filter().all()
            db_session.commit()
            db_session.close()
            infos_new = []
            for i in infos:
                if name in str(i.jobName):
                    infos_new.append({
                        'id': i.id,
                        'jobName': i.jobName,
                        'highMonthPay': i.highMonthPay,
                        'updateDate': i.updateDate,
                        'lowMonthPay': i.lowMonthPay,
                        'headCount': i.headCount,
                        'publishDate': i.publishDate,
                        'degreeName': i.degreeName,
                        'recName': i.recName,
                        'recLogo': i.recLogo,
                        'areaCodeName': i.areaCodeName,
                        'recScale': i.recScale,
                        'recTags': i.recTags,
                        'major': i.major,
                        'recProperty': i.recProperty
                    })
            number_list = ['all']
            return jsonify({'number_list': number_list, 'infos': infos_new})
        except:
            pass

        # 获取 axios 信息
        number = int(request.get_json()['number'])
        di_qu = request.get_json()['di_qu']
        gong_zi = request.get_json()['gong_zi']

        if gong_zi == '月薪(不限)':
            pass
        else:
            gongzi_qian = float(gong_zi.split('-', )[0])
            gongzi_ho = float(gong_zi.split('-', )[1])

        # 单独工资 单独地区
        if di_qu != '地区(不限)' and gong_zi != '月薪(不限)':
            len_number = int(
<<<<<<< HEAD
                int(len(db_session.query(Jobs).filter(gongzi_qian <= Jobs.highMonthPay).filter(
                    gongzi_ho >= Jobs.highMonthPay).filter(Jobs.areaCodeName == di_qu).all())) / 10) + 2# 一页十条信息
=======
                int(len(db_session.query(Jobs).filter(gongzi_qian <= Jobs.lowMonthPay).filter(
                    gongzi_ho >= Jobs.highMonthPay).filter(Jobs.areaCodeName == di_qu).all())) / 10) + 2
>>>>>>> 576f25c44d1790e9362898a273b80804182912d3
            number_list = []
            for i in range(1, len_number):
                number_list.append(i)

<<<<<<< HEAD
            infos = db_session.query(Jobs).filter(gongzi_qian <= Jobs.highMonthPay).filter(
=======
            infos = db_session.query(Jobs).filter(gongzi_qian <= Jobs.lowMonthPay).filter(
>>>>>>> 576f25c44d1790e9362898a273b80804182912d3
                gongzi_ho >= Jobs.highMonthPay).filter(Jobs.areaCodeName == di_qu).all()
            db_session.commit()
            db_session.close()
            infos = infos[number * 10 - 10:10 * number]
            infos_new = []
            for i in infos:
                infos_new.append({
                    'id': i.id,
                    'jobName': i.jobName,
                    'highMonthPay': i.highMonthPay,
                    'updateDate': i.updateDate,
                    'lowMonthPay': i.lowMonthPay,
                    'headCount': i.headCount,
                    'publishDate': i.publishDate,
                    'degreeName': i.degreeName,
                    'recName': i.recName,
                    'recLogo': i.recLogo,
                    'areaCodeName': i.areaCodeName,
                    'recScale': i.recScale,
                    'recTags': i.recTags,
                    'major': i.major,
                    'recProperty': i.recProperty
                })
            return jsonify({'number_list': number_list, 'infos': infos_new})

        # 单独工资
        if di_qu == '地区(不限)' and gong_zi != '月薪(不限)':
            len_number = int(
<<<<<<< HEAD
                int(len(db_session.query(Jobs).filter(gongzi_qian <= Jobs.highMonthPay).filter(
=======
                int(len(db_session.query(Jobs).filter(gongzi_qian <= Jobs.lowMonthPay).filter(
>>>>>>> 576f25c44d1790e9362898a273b80804182912d3
                    gongzi_ho >= Jobs.highMonthPay).all())) / 10) + 2
            number_list = []
            for i in range(1, len_number):
                number_list.append(i)

<<<<<<< HEAD
            infos = db_session.query(Jobs).filter(gongzi_qian <= Jobs.highMonthPay).filter(
=======
            infos = db_session.query(Jobs).filter(gongzi_qian <= Jobs.lowMonthPay).filter(
>>>>>>> 576f25c44d1790e9362898a273b80804182912d3
                gongzi_ho >= Jobs.highMonthPay).all()
            db_session.commit()
            db_session.close()
            infos = infos[number * 10 - 10:10 * number]
            infos_new = []
            for i in infos:
                infos_new.append({
                    'id': i.id,
                    'jobName': i.jobName,
                    'highMonthPay': i.highMonthPay,
                    'updateDate': i.updateDate,
                    'lowMonthPay': i.lowMonthPay,
                    'headCount': i.headCount,
                    'publishDate': i.publishDate,
                    'degreeName': i.degreeName,
                    'recName': i.recName,
                    'recLogo': i.recLogo,
                    'areaCodeName': i.areaCodeName,
                    'recScale': i.recScale,
                    'recTags': i.recTags,
                    'major': i.major,
                    'recProperty': i.recProperty
                })
            return jsonify({'number_list': number_list, 'infos': infos_new})

        # 单独地区
        if di_qu != '地区(不限)' and gong_zi == '月薪(不限)':
<<<<<<< HEAD
            len_number = int(int(len(db_session.query(Jobs).filter(Jobs.areaCodeName == di_qu).all())) / 10) + 2 # 一页十条信息
=======
            len_number = int(int(len(db_session.query(Jobs).filter(Jobs.areaCodeName == di_qu).all())) / 10) + 2
>>>>>>> 576f25c44d1790e9362898a273b80804182912d3
            number_list = []
            for i in range(1, len_number):
                number_list.append(i)
            infos = db_session.query(Jobs).filter(Jobs.areaCodeName == di_qu).all()
            db_session.commit()
            db_session.close()
            infos = infos[number * 10 - 10:10 * number]
            infos_new = []
            for i in infos:
                infos_new.append({
                    'id': i.id,
                    'jobName': i.jobName,
                    'highMonthPay': i.highMonthPay,
                    'updateDate': i.updateDate,
                    'lowMonthPay': i.lowMonthPay,
                    'headCount': i.headCount,
                    'publishDate': i.publishDate,
                    'degreeName': i.degreeName,
                    'recName': i.recName,
                    'recLogo': i.recLogo,
                    'areaCodeName': i.areaCodeName,
                    'recScale': i.recScale,
                    'recTags': i.recTags,
                    'major': i.major,
                    'recProperty': i.recProperty
                })
            return jsonify({'number_list': number_list, 'infos': infos_new})

        # 啥都没有定义
        len_number = int(int(len(db_session.query(Jobs).filter().all())) / 10) + 2
        number_list = []
        for i in range(1, len_number):
            number_list.append(i)
        if di_qu == '地区(不限)' and gong_zi == '月薪(不限)':
            infos = db_session.query(Jobs).filter().all()
            db_session.commit()
            db_session.close()
            infos = infos[number * 10 - 10:10 * number]
            infos_new = []
            for i in infos:
                infos_new.append({
                    'id': i.id,
                    'jobName': i.jobName,
                    'highMonthPay': i.highMonthPay,
                    'updateDate': i.updateDate,
                    'lowMonthPay': i.lowMonthPay,
                    'headCount': i.headCount,
                    'publishDate': i.publishDate,
                    'degreeName': i.degreeName,
                    'recName': i.recName,
                    'recLogo': i.recLogo,
                    'areaCodeName': i.areaCodeName,
                    'recScale': i.recScale,
                    'recTags': i.recTags,
                    'major': i.major,
                    'recProperty': i.recProperty
                })
            return jsonify({'number_list': number_list, 'infos': infos_new})


if __name__ == '__main__':
    app.run()
