from flask import Flask, jsonify, abort, make_response, request, send_file, render_template, url_for, redirect

class Job(object):
    def __init__(self, position, location, skills, descrp):
        self.position = position
        self.location = location
        self.skills = skills
        self.descrp = descrp

joblist = []


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('MainPage.html')

@app.route('/profile/')
def profile():
    return render_template('ProfilePage.html')

@app.route('/jobs/')
def jobs():
    return render_template('FeedPage.html')

@app.route('/createjob/', methods=['GET','POST'] )
def createjob():
    if request.method == "POST":
        position = request.form.get("Position")
        location = request.form.get("Location")
        skills = request.form.get("skills")
        descrp = request.form.get("descrp")

        joblist.append(Job(position, location, skills, descrp))
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
    app.run(debug=True)