from flask import Flask, render_template, jsonify

app = Flask(__name__)

HYPS = [
  {
    'id': 1,
    'title': 'team iteration',
    'org_level': 'team',
    'prod_fl_level': 'delivery',
    'Biz value': 'feedback',
    'frequency': '2 weeks'
  },
  {
    'id': 2,
    'title': 'leadership updates',
    'org_level': 'leadership',
    'prod_fl_level': 'vision',
    'Biz value': 'steer',
    'frequency': 'weekly'
  },
  {
    'id': 3,
    'title': 'middle layer coordination',
    'org_level': 'middle layer',
    'prod_fl_level': 'links and dependencies',
    'Biz value': 'coordination',
    'frequency': 'weekly'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', hyps=HYPS)


@app.route("/api/hyps")
def list_hyps():
  return jsonify(HYPS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
