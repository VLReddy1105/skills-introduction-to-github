from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store timetable entries
# Each entry is a dictionary with 'subject' and 'time'
timetable = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form.get('subject')
        time = request.form.get('time')
        if subject and time:
            timetable.append({'subject': subject, 'time': time})
        return redirect(url_for('index'))
    return render_template('index.html', timetable=timetable)

if __name__ == '__main__':
    app.run(debug=True)
