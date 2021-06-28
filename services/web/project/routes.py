from flask import render_template, request
from project import app
from jinja2 import TemplateNotFound

# from project.forms import Case_Study

# import numpy as np

@app.route("/")
def index():
    return render_template('index.html', segment='index')

@app.route('/<template>')
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment)

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# def get_data():
#     cases = Case_Study.query.all()
#     result = [[] for i in range(2)]
#     for case in cases:
#         result[case.case_id].append({ "case_id": case.case_id,
#                                         "index": case.index,
#                                         "Loss_mae": (case.Loss_mae if not np.isnan(case.Loss_mae) else 0),
#                                         "Threshold": (case.Threshold if not np.isnan(case.Threshold) else 0),
#                                         "pointType": case.pointType
#                                     })
#     return result

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  