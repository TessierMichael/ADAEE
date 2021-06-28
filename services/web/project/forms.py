from project import db

class Study_Cases(db.Model):
    __tablename__ = "study_cases"

    id = db.Column(db.Integer, primary_key=True)
    faultNumber = db.Column(db.Integer, nullable=False)
    faultLocation = db.Column(db.Integer, nullable=True)
    points = db.relationship("Case_Study")

    def __init__(self, id, faultNumber, faultLocation):
        self.id = id
        self.faultNumber = faultNumber
        self.faultLocation = faultLocation


class Case_Study(db.Model):
    __tablename__ = "case_study"

    case_id = db.Column(db.Integer, db.ForeignKey('study_cases.id'), primary_key=True)

    index = db.Column(db.Integer, primary_key=True)
    faultNumber = db.Column(db.Float, nullable=False)
    simulationRun = db.Column(db.Float, nullable=False)
    sample = db.Column(db.Float, nullable=False)

    xmeas_1 = db.Column(db.Float, nullable=False)
    xmeas_2 = db.Column(db.Float, nullable=False)
    xmeas_3 = db.Column(db.Float, nullable=False)
    xmeas_4 = db.Column(db.Float, nullable=False)
    xmeas_5 = db.Column(db.Float, nullable=False)
    xmeas_6 = db.Column(db.Float, nullable=False)
    xmeas_7 = db.Column(db.Float, nullable=False)
    xmeas_8 = db.Column(db.Float, nullable=False)
    xmeas_9 = db.Column(db.Float, nullable=False)
    xmeas_10 = db.Column(db.Float, nullable=False)
    xmeas_11 = db.Column(db.Float, nullable=False)
    xmeas_12 = db.Column(db.Float, nullable=False)
    xmeas_13 = db.Column(db.Float, nullable=False)
    xmeas_14 = db.Column(db.Float, nullable=False)
    xmeas_15 = db.Column(db.Float, nullable=False)
    xmeas_16 = db.Column(db.Float, nullable=False)
    xmeas_17 = db.Column(db.Float, nullable=False)
    xmeas_18 = db.Column(db.Float, nullable=False)
    xmeas_19 = db.Column(db.Float, nullable=False)
    xmeas_20 = db.Column(db.Float, nullable=False)
    xmeas_21 = db.Column(db.Float, nullable=False)
    xmeas_22 = db.Column(db.Float, nullable=False)
    xmeas_23 = db.Column(db.Float, nullable=False)
    xmeas_24 = db.Column(db.Float, nullable=False)
    xmeas_25 = db.Column(db.Float, nullable=False)
    xmeas_26 = db.Column(db.Float, nullable=False)
    xmeas_27 = db.Column(db.Float, nullable=False)
    xmeas_28 = db.Column(db.Float, nullable=False)
    xmeas_29 = db.Column(db.Float, nullable=False)
    xmeas_30 = db.Column(db.Float, nullable=False)
    xmeas_31 = db.Column(db.Float, nullable=False)
    xmeas_32 = db.Column(db.Float, nullable=False)
    xmeas_33 = db.Column(db.Float, nullable=False)
    xmeas_34 = db.Column(db.Float, nullable=False)
    xmeas_35 = db.Column(db.Float, nullable=False)
    xmeas_36 = db.Column(db.Float, nullable=False)
    xmeas_37 = db.Column(db.Float, nullable=False)
    xmeas_38 = db.Column(db.Float, nullable=False)
    xmeas_39 = db.Column(db.Float, nullable=False)
    xmeas_40 = db.Column(db.Float, nullable=False)
    xmeas_41 = db.Column(db.Float, nullable=False)

    xmv_1 = db.Column(db.Float, nullable=False)
    xmv_2 = db.Column(db.Float, nullable=False)
    xmv_3 = db.Column(db.Float, nullable=False)
    xmv_4 = db.Column(db.Float, nullable=False)
    xmv_5 = db.Column(db.Float, nullable=False)
    xmv_6 = db.Column(db.Float, nullable=False)
    xmv_7 = db.Column(db.Float, nullable=False)
    xmv_8 = db.Column(db.Float, nullable=False)
    xmv_9 = db.Column(db.Float, nullable=False)
    xmv_10 = db.Column(db.Float, nullable=False)
    xmv_11 = db.Column(db.Float, nullable=False)

    Loss_mae = db.Column(db.Float, nullable=True)
    Threshold = db.Column(db.Float, nullable=True)
    pointType = db.Column(db.String(5), nullable=False)

    def __init__(self, case_id, index, faultNumber, simulationRun, sample, xmeas_1,
                 xmeas_2, xmeas_3, xmeas_4, xmeas_5, xmeas_6, xmeas_7, xmeas_8,
                 xmeas_9, xmeas_10, xmeas_11, xmeas_12, xmeas_13, xmeas_14, xmeas_15,
                 xmeas_16, xmeas_17, xmeas_18, xmeas_19, xmeas_20, xmeas_21, xmeas_22,
                 xmeas_23, xmeas_24, xmeas_25, xmeas_26, xmeas_27, xmeas_28, xmeas_29,
                 xmeas_30, xmeas_31, xmeas_32, xmeas_33, xmeas_34, xmeas_35, xmeas_36,
                 xmeas_37, xmeas_38, xmeas_39, xmeas_40, xmeas_41, xmv_1, xmv_2, xmv_3,
                 xmv_4, xmv_5, xmv_6, xmv_7, xmv_8, xmv_9, xmv_10, xmv_11,
                 Loss_mae, Threshold, pointType):

        self.case_id = case_id

        self.index = index
        self.faultNumber = faultNumber
        self.simulationRun = simulationRun
        self.sample = sample

        self.xmeas_1 = xmeas_1
        self.xmeas_2 = xmeas_2
        self.xmeas_3 = xmeas_3
        self.xmeas_4 = xmeas_4
        self.xmeas_5 = xmeas_5
        self.xmeas_6 = xmeas_6
        self.xmeas_7 = xmeas_7
        self.xmeas_8 = xmeas_8
        self.xmeas_9 = xmeas_9
        self.xmeas_10 = xmeas_10
        self.xmeas_11 = xmeas_11
        self.xmeas_12 = xmeas_12
        self.xmeas_13 = xmeas_13
        self.xmeas_14 = xmeas_14
        self.xmeas_15 = xmeas_15
        self.xmeas_16 = xmeas_16
        self.xmeas_17 = xmeas_17
        self.xmeas_18 = xmeas_18
        self.xmeas_19 = xmeas_19
        self.xmeas_20 = xmeas_20
        self.xmeas_21 = xmeas_21
        self.xmeas_22 = xmeas_22
        self.xmeas_23 = xmeas_23
        self.xmeas_24 = xmeas_24
        self.xmeas_25 = xmeas_25
        self.xmeas_26 = xmeas_26
        self.xmeas_27 = xmeas_27
        self.xmeas_28 = xmeas_28
        self.xmeas_29 = xmeas_29
        self.xmeas_30 = xmeas_30
        self.xmeas_31 = xmeas_31
        self.xmeas_32 = xmeas_32
        self.xmeas_33 = xmeas_33
        self.xmeas_34 = xmeas_34
        self.xmeas_35 = xmeas_35
        self.xmeas_36 = xmeas_36
        self.xmeas_37 = xmeas_37
        self.xmeas_38 = xmeas_38
        self.xmeas_39 = xmeas_39
        self.xmeas_40 = xmeas_40
        self.xmeas_41 = xmeas_41

        self.xmv_1 = xmv_1
        self.xmv_2 = xmv_2
        self.xmv_3 = xmv_3
        self.xmv_4 = xmv_4
        self.xmv_5 = xmv_5
        self.xmv_6 = xmv_6
        self.xmv_7 = xmv_7
        self.xmv_8 = xmv_8
        self.xmv_9 = xmv_9
        self.xmv_10 = xmv_10
        self.xmv_11 = xmv_11

        self.Loss_mae = Loss_mae
        self.Threshold = Threshold
        self.pointType = pointType