from flask import render_template,redirect,url_for,flash,request,session
from app import app,db
from models import User,Product
from forms import RegistrationForm,LoginForm,ProductForm
from flask_login import login_user,logout_user,login_required,current_user
from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/')
def home():
    products=Product.query.all()
    return render_template('home.html',products=products)

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=generate_password_hash(form.password.data)
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!','success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid credentials','danger')
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items=session.get('cart',[])
    return render_template('cart.html',cart=cart_items)

@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    product=Product.query.get(product_id)
    if product:
        if 'cart' not in session:
            session['cart']=[]
        session['cart'].append({'id':product.id,'name':product.name,'price':product.price})
        session.modified=True
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    session['cart']=[]
    flash("Order placed successfully!","success")
    return redirect(url_for('home'))