from flask import Blueprint, request, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'admin123':
            return "<h1>Đăng nhập thành công!</h1>"
        else:
            return "<h1>Sai tên đăng nhập hoặc mật khẩu!</h1>"
    
    return render_template('login.html')
