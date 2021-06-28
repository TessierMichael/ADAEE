from flask.cli import FlaskGroup


from project import app, db
from project.forms import Study_Cases, Case_Study
from util import fetch_data


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    caseNumber = 0
    for faultNumber in [1]:
        for faultLocation in [20, 80]:
            df = fetch_data(faultNumber, faultLocation)
            db.session.add(Study_Cases(caseNumber, faultNumber, faultLocation))
            db.session.flush()
            df_array = df.to_numpy()
            case_study_array = []
            index = 0
            for row in df_array:
                case_study_array.append(Case_Study(caseNumber, index, row[0], row[1], row[2], row[3], row[4],
                                                   row[5], row[6], row[7], row[8], row[9], row[10],
                                                   row[11], row[12], row[13], row[14], row[15], row[16],
                                                   row[17], row[18], row[19], row[20], row[21], row[22],
                                                   row[23], row[24], row[25], row[26], row[27], row[28],
                                                   row[29], row[30], row[31], row[32], row[33], row[34],
                                                   row[35], row[36], row[37], row[38], row[39], row[40],
                                                   row[41], row[42], row[43], row[44], row[45], row[46],
                                                   row[47], row[48], row[49], row[50], row[51], row[52],
                                                   row[53], row[54], row[55], row[56], row[57]))
                index += 1
            db.session.bulk_save_objects(case_study_array)
            db.session.commit()
            caseNumber += 1


if __name__ == "__main__":
    cli()
