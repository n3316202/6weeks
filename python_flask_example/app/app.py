
from flask import Flask, render_template , request, url_for,redirect
from  model.study import Grade ,VisualEx
from  model.db_crud import DBExample

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('home.html')

@app.route('/login')
def login(): 
    pass

@app.route('/user/<username>')
def profile(username): 
    pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/grade_view')
def grade_view():
    return render_template('grade.html')


@app.route('/grade')
def grade():
    kor = request.values.get("kor")
    eng = request.values.get("eng")
    math = request.values.get("math")
    total = int(kor) + int(eng) + int(math)
    avg = int(kor) + int(eng) + int(math) / 3.0
    grade = Grade(int(kor) , int(eng) , int(math))

    #return render_template('grade_result.html',total=total, avg=avg)
    return render_template('grade_result.html',grade=grade)

@app.route('/graph')
def graphExample():
    visualEx = VisualEx()
    return render_template('visual_example.html',plot_url = visualEx.basic_example())

@app.route('/show_table')
def show_table():
    db_example = DBExample()
    db_example.show_table()
    df = db_example.select_customers()
    print(df)
    return df.to_html(index=False)


@app.route('/customer_insert_view')
def customer_insert_view():
    return render_template('customer_insert.html')

@app.route('/customer_insert')
def customer_insert():
    name = request.values.get("name")
    email = request.values.get("email")

    db_example = DBExample()
    db_example.insert_customers(email=email,name=name)

    #return db_example.select_customers().to_html(index=False)
    return render_template('customers_view.html',df=db_example.select_customers())

@app.route('/customer_delete')
def customer_delete():
    id = request.values.get("bid")


    db_example = DBExample()
    db_example.delete_customers(id=id)

    #return render_template('customers_view.html',df=db_example.select_customers())
    return redirect(url_for('customer_view'))

@app.route('/customer_view')
def customer_view():

    db_example = DBExample()
    return render_template('customers_view.html',df=db_example.select_customers())


if __name__ == '__main__':
    app.run(debug=True)

