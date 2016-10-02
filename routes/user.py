from routes import *
from models.user import User

main = Blueprint('user', __name__)

Model = User


@main.route('/login_view')
def index():
    return render_template('login.html')


@main.route('/reg_view')
def reg_view():
    return render_template('register.html')


@main.route('/profile')
def profile():
    u = current_user()
    if u is not None:
        return render_template('profile.html', user=u)
    else:
        return redirect(url_for('.index'))


@main.route('/update_password', methods=['POST'])
def update_password():
    u = current_user()
    password = request.form.get('password', '')
    print('password', password)
    if u.change_password(password):
        print('用户密码修改成功')
    else:
        print('用户密码修改失败')
    return redirect(url_for('user.profile'))


@main.route('/update_avatar', methods=['POST'])
def update_avatar():
    u = current_user()
    avatar = request.form.get('avatar', '')
    print('avatar', avatar)
    if u.change_avatar(avatar):
        print('头像修改成功')
    else:
        print('头像修改失败')
    return redirect(url_for('user.profile'))


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    u_valid =u.valid()
    print(u_valid)
    if u_valid[0]:
        u.save()
        print(u.id, u.username)
        session['user_id'] = u.id
    else:
        abort(410)
    return redirect(url_for('user.profile'))


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate_login(u):
        print('登录成功')
        session['user_id'] = user.id
    else:
        print('登录失败')
    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 user
    return redirect(url_for('index.index'))
