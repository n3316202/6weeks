<<<<<<< HEAD
from flask import Flask, render_template , request
from  model.study import Grade ,VisualEx

=======
from flask import Flask, render_template ,url_for
>>>>>>> 0420cdb921bf06bf326ff88b0bb402ffeff58736


app = Flask(__name__)

@app.route('/')
def index(): 
    pass

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

<<<<<<< HEAD
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

if __name__ == '__main__':
    app.run(debug=True)
=======
if __name__ == '__main__':
    app.run(debug = True)
>>>>>>> 0420cdb921bf06bf326ff88b0bb402ffeff58736
