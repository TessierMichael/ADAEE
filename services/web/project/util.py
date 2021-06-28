from forms import Case_Study

def get_data(template):
    return Case_Study.query.all()
