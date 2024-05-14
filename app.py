from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
  'id' : 1,
  'title': 'Data Analyst',
  'location': 'Johannesburg, South Africa',
  'salary': 'R650 000'
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Cape Town, South Africa',
    'salary': 'R800 000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Cape Town, South Africa',
    'salary': 'R850 000'
  },
  {
    'id': 2,
    'title': 'ML/AI Engineer',
    'location': 'Cape Town, South Africa',
    'salary': 'R1 200 000'
  }
]

@app.route('/')
def hello_world():
  return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)