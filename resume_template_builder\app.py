from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)

# Sample resume template (replace with your own template)
resume_template = """
# {{ personal_info.name }}

## Personal Information
- **Email:** {{ personal_info.email }}
- **Phone:** {{ personal_info.phone }}
- **Address:** {{ personal_info.address }}

## Education
{% for degree in education %}
- **{{ degree.degree }} in {{ degree.major }}**
  - *{{ degree.school }}, {{ degree.year }}*
{% endfor %}

## Experience
{% for job in experience %}
- **{{ job.title }} at {{ job.company }}**
  - *{{ job.location }}*
  - *{{ job.date }}*
  - {{ job.description }}
{% endfor %}
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    # Extract user input from the form
    personal_info = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'address': request.form['address']
    }

    education = []
    for i in range(1, 4):  # Assuming up to 3 degrees
        degree = request.form.get(f'degree{i}')
        major = request.form.get(f'major{i}')
        school = request.form.get(f'school{i}')
        year = request.form.get(f'year{i}')
        if degree and major and school and year:
            education.append({
                'degree': degree,
                'major': major,
                'school': school,
                'year': year
            })

    experience = []
    for i in range(1, 4):  # Assuming up to 3 job experiences
        title = request.form.get(f'title{i}')
        company = request.form.get(f'company{i}')
        location = request.form.get(f'location{i}')
        date = request.form.get(f'date{i}')
        description = request.form.get(f'description{i}')
        if title and company and location and date and description:
            experience.append({
                'title': title,
                'company': company,
                'location': location,
                'date': date,
                'description': description
            })

    # Render the resume using the template
    template = Template(resume_template)
    resume_content = template.render(personal_info=personal_info, education=education, experience=experience)

    return render_template('resume.html', resume_content=resume_content)

if __name__ == '__main__':
    app.run(debug=True)
