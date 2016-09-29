from routes import *
from models.user import User

main = Blueprint('user', __name__)

Model = User


@main.route('/login')
def login_index():
    return render_template('login.html')
