from flask import Flask, jsonify, abort, make_response, request, send_file, render_template, url_for, redirect, session, flash
import json

class Job(object):
    def __init__(self, position, company, location, skills, descrp, type, salary, experience):
        self.position = position
        self.company = company
        self.location = location
        self.skills = skills
        self.descrp = descrp
        self.type = type
        self.salary = salary
        self.experience = experience

joblist = []
comparedJobs = []

joblist.append(Job("Front-End Developer","SoftTech","Istanbul","JavaScript, JQuery, CSS, HTML","Full-time, Writing well designed, testable, efficient code by using best software development practices. " +
"Creating website layout/user interfaces by using standard HTML/CSS practices, Integrating data from various back-end services and databases. ", "Full-Time", "$16000", "2+ Years"))

joblist.append(Job("Back-End Developer","İş Bankası","Istanbul","Python, MongoDB, SQL","Compile and analyze data, processes, and codes to troubleshoot problems and identify areas for improvement. " +
"Collaborating with the front-end developers and other team members to establish objectives and design more functional, cohesive codes to enhance the user experience. " +
"Developing ideas for new programs, products, or features by monitoring industry developments and trends. " +
"Recording data and reporting it to proper parties, such as clients or leadership.", "Full-Time", "$20000", "5+ Years"))

joblist.append(Job("Kebab Chef","The Avenue Chippy","Calcot, England","Chef(1+ year experience)","We are looking for a trained kebab chef to join our friendly and vibrant new team in our new chip shop. Experience would be ideal, as it will be a fast paced environment.", "Full-Time", "$12000", "3+ Years"))

joblist.append(Job("Front-End Developer", "İş Bankası", "İstanbul", "NodeJS, JQuery, HTML5, CSS", "Full-time, Writing well designed, testable, efficient code by using best software development practices. " +
"Creating website layout/user interfaces by using standard HTML/CSS practices, Integrating data from various back-end services and databases. ", "Full-Time", "$17000", "2+ Years"))

joblist.append(Job("Front-End Developer", "Microsoft", "İstanbul", "HTML, CSS, MySQL, JQuery, React", "Full-time, Writing well designed, testable, efficient code by using best software development practices. " +
"Creating website layout/user interfaces by using standard HTML/CSS practices, Integrating data from various back-end services and databases. ", "Full-Time", "$24000", "4+ Years"))

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/company')
def company():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index2.html')


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
        if password == 'password' and email == 'user@pineapple.com':
            session['logged_in'] = True
            return redirect(url_for('home'))
        elif password == 'password' and email == 'company@pineapple.com':
            session['logged_in'] = True
            return redirect(url_for('company'))
        else:
            flash('wrong credentials!')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('profile.html')

@app.route('/myapplications')
def myapplications():
    if not session.get('logged_in'):
        return render_template('login.html')
    application = []
    file1 = open("db.txt", "r+")
    for line in file1:
        application.append(line)

    return render_template('myapplications.html',application=application)

@app.route('/jobs')
def jobs():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('jobs.html', joblist=joblist)

@app.route('/jobs2')
def jobs2():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('jobs2.html', joblist=joblist)

@app.route('/createjob', methods=["GET", "POST"])
def createjob():
    if not session.get('logged_in'):
        return render_template('login.html')
    if request.method == "POST":

        position = request.form.get("position")
        company = request.form.get("company")
        location = request.form.get("location")
        skills = request.form.get("skills")
        descrp = request.form.get("descrp")
        type = request.form.get("type")
        salary = request.form.get("salary")
        experience = request.form.get("experience")

        joblist.append(Job(position, company, location, skills, descrp, type, salary, experience))

        file1 = open("db.txt", "w")

        file1.write(position)
        file1.write("\n")
        file1.write(company)
        file1.write("\n")
        file1.write(location)
        file1.write("\n")
        file1.write(skills)
        file1.write("\n")
        file1.write(descrp)
        file1.write("\n")
        file1.write(type)
        file1.write("\n")
        file1.write(salary)
        file1.write("\n")
        file1.write(experience)
        file1.write("\n")

        return redirect(url_for('jobs2'))
    return render_template('createjob.html')

@app.route('/compare')
def compare():
    if not session.get('logged_in'):
        return render_template('login.html')
    newjobarr = []
    file1 = open("db.txt", "r+")
    for line in file1:
        newjobarr.append(line)

    return render_template('compare.html', newjobarr=newjobarr)

@app.route('/taketest')
def taketest():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('testpage.html')

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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)