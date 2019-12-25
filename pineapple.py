from flask import Flask, jsonify, abort, make_response, request, send_file, render_template, url_for, redirect, session, flash
import json

class Job(object):
    def __init__(self, position, company, location, skills, descrp):
        self.position = position
        self.company = company
        self.location = location
        self.skills = skills
        self.descrp = descrp


joblist = []
comparedJobs = []

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        req = request.form

        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("public/sign_up.html", feedback=feedback)

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        job_title = request.form.get("job_title")
        email = request.form.get("EMAIL")
        password = request.form.get("pwd")
        location = request.form.get("location")
        #country = request.form.get("country_select")

        return redirect(request.url)
    return render_template('signup.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("EMAIL")
        password = request.form.get("pwd")
        if password == 'password' and email == 'admin@pineapple.com':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('wrong credentials!')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    return render_template('profile.html')

# @app.route('/jobs/', methods=['GET', 'POST'])
# def jobs():
#     if request.method == "POST":
#         comparedJob = request.get_json()
#         comparedJobs = comparedJob
#         session['comparedJob'] = comparedJob
#         #comparedJob = request.form.getlist('checkboxn')
#         #return render_template('Comparison.html', comparedJob=comparedJob)
#         #return redirect(url_for('comparison'))
#         file1 = open("db.txt", "w")
#         for obj in comparedJobs:
#             file1.write(obj)
#             file1.write("\n")
#         #file1.write("Hello \n")
#         #file1.writelines(comparedJobs)
#         file1.close()
#         #file1 = open("db.txt", "r+")
#         #print("Output is ", file1.readline())
#         return render_template('Comparison.html', comparedJob=comparedJob)
#     else:
#         return render_template('FeedPage.html', joblist=joblist)
#
# @app.route('/taketest/')
# def taketest():
#     return render_template('TestPage.html')
#
# @app.route('/comparison/')
# def comparison():
#     comparedjobs2 = []
#     file1 = open("db.txt", "r+")
#     for line in file1:
#         comparedJobs.append(line)
#     for obj in comparedJobs:
#         if obj == "Front-End Developer\n":
#             comparedjobs2.append(["Front-End Developer", "Softech", "Istanbul", "JavaScript, JQuery, CSS, HTML"])
#         if obj == "Back-End Developer\n":
#             comparedjobs2.append(["Back-End Developer", "İş Bankası", "İstanbul", "Python, MongoDB, SQL"])
#         if obj == "Product Manager\n":
#             comparedjobs2.append(["Product Manager", "Microsoft", "New York",
#                                   "MS office, JavaScript, HTML, MS project computer applications, Agile Methodologies"])
#
#     return render_template('Comparison.html', comparedjobs2=comparedjobs2)
#
# @app.route('/createjob/', methods=['GET','POST'] )
# def createjob():
#     if request.method == "POST":
#         position = request.form.get("Position")
#         company = request.form.get("company")
#         location = request.form.get("Location")
#         skills = request.form.get("skills")
#         descrp = request.form.get("descrp")
#
#         joblist.append(Job(position, company, location, skills, descrp))
#         for obj in joblist:
#             print(obj.position)
#             print(obj.location)
#             print(obj.skills)
#             print(obj.descrp)
#
#         return redirect(request.url)
#
#     return render_template('CreateJob.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)