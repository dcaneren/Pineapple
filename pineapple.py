from flask import Flask, jsonify, abort, make_response, request, send_file, render_template, url_for, redirect, session
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

joblist.append(Job("Front-End Developer","Softech","Istanbul","JavaScript, JQuery, CSS, HTML","Full-time, Writing well designed, testable, efficient code by using best software development practices. " +
"Creating website layout/user interfaces by using standard HTML/CSS practices, Integrating data from various back-end services and databases. "))

joblist.append(Job("Back-End Developer","İş Bankası","Istanbul","Python, MongoDB, SQL","Compile and analyze data, processes, and codes to troubleshoot problems and identify areas for improvement. " +
"Collaborating with the front-end developers and other team members to establish objectives and design more functional, cohesive codes to enhance the user experience. " +
"Developing ideas for new programs, products, or features by monitoring industry developments and trends. " +
"Recording data and reporting it to proper parties, such as clients or leadership." ))

joblist.append(Job("Project Manager","Kardeşler Pide & Kebap","Konya","MS office, JavaScript, HTML, MS project computer applications, Agile Methodologies ","Designing and installing all control systems and software applications in an effective and efficient manner. "+
"Maintaining a clean and safe work environment complying with safety measures and organizational standards and regulations. " +
"Utilizing relevant resources to execute project activates effectively and notifying unsafe conditions to supervisors and seniors for correct actions. "+
"Coordinating with client project seniors to identify project issues and concerns and making appropriate resolutions in a timely manner."))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('MainPage.html')

@app.route('/profile/')
def profile():
    return render_template('ProfilePage.html')

@app.route('/jobs/', methods=['GET', 'POST'])
def jobs():
    if request.method == "POST":
        comparedJob = request.get_json()
        comparedJobs = comparedJob
        session['comparedJob'] = comparedJob
        #comparedJob = request.form.getlist('checkboxn')
        #return render_template('Comparison.html', comparedJob=comparedJob)
        #return redirect(url_for('comparison'))
        return render_template('Comparison.html', comparedJob=comparedJob)
    else:
        return render_template('FeedPage.html', joblist=joblist)

@app.route('/taketest/')
def taketest():
    return render_template('TestPage.html')

@app.route('/comparison/')
def comparison():
    return render_template('Comparison.html')

@app.route('/createjob/', methods=['GET','POST'] )
def createjob():
    if request.method == "POST":
        position = request.form.get("Position")
        company = request.form.get("company")
        location = request.form.get("Location")
        skills = request.form.get("skills")
        descrp = request.form.get("descrp")

        joblist.append(Job(position, company, location, skills, descrp))
        for obj in joblist:
            print(obj.position)
            print(obj.location)
            print(obj.skills)
            print(obj.descrp)

        return redirect(request.url)

    return render_template('CreateJob.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)