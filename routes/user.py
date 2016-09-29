from routes import *
from models.user import User

main = Blueprint('user', __name__)

Model = User


@main.route('/login_view')
def index():
    return render_template('login.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    print(u.valid())
    if u.valid():
        u.save()
    else:
        abort(410)
    return redirect(url_for('user.index'))


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
