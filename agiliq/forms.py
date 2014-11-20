from wtforms import Form, StringField, FileField, SubmitField

class ResumeForm(Form):
    first_name   = StringField('First Name')
    last_name    = StringField('Last Name')
    projects_url = StringField('Projects Url')
    code_url     = StringField('Code Url')
    resume       = FileField('Resume')
    submit       = SubmitField()
