from forms import Case_Study

def get_data(template):
    cases = Case_Study.query.all()
    result = []
    for case in cases:
        result.append({ "case_id": case.case_id,
                        "index": case.index,
                        "Loss_mae": case.Loss_mae,
                        "Threshold": case.Threshold,
                        "pointType": case.pointType
                      })
    return result
