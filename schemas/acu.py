from ma import ma
from models import UserModel, AcuReportModel

# from models import ProductModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_fk = True
        exclude = ("is_active")

    id = ma.auto_field()


class AcuReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AcuReportModel
        load_instance = True
        include_fk = True
        # exclude = ("",)
