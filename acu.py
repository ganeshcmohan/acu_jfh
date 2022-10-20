from flask import request
from flask_restplus import Resource, fields, Namespace

from models import User, AcuReport
from schemas.acu import UserSchema, AcuReportSchema
from api import AcuApi

REPORT_NOT_FOUND = "Search not found."


acu_search_ns = Namespace("search", description="search related operations")

user_schema = UserSchema()
acu_report_schema = AcuReportSchema()

# Model required by flask_restplus for expect


acu_report = acu_search_ns.model(
    "AcuReport",
    {
        "keyword": fields.String,
        "address": fields.String,
        "loc_key": fields.String,
        "weather": fields.String,
    },
)

class User(Resource):
    def post(self):
        print("In post")
        user_login = request.get_json()
        try:
            user = User.query.filter_by(username=user_login["username"]).first()
            if user.check_password_hash(user.passwor_hash, user_login["password"]):
                msg = {"message": "Login Successfulk!"}
                return msg, 200
            else:
                msg = {"message": "Invalid Username or password!"}
                return msg, 400
        except Exception as e:
            msg = {"message": "Something went wrong!"}
            return msg, 400

class AcuReport(Resource):
    def get(self, id):
        print("In detail")
        report_data = AcuReport.find_by_id(id)
        if report_data:
            return report_data.json()
        return {"message": REPORT_NOT_FOUND}, 404

    @acu_search_ns.expect(acu_report)
    @acu_search_ns.doc("Create a Report")
    def post(self):
        print("In post")
        report_json = request.get_json()
        weather = AcuApi.current_condition(report_json['keyword'])
        report_data = AcuReportSchema.load(report_json)
        report_data.save_to_db()
        return report_data.json(), 201



