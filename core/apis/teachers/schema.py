from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.models.teachers import Teacher


class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE

    id = auto_field(required=False)
    name = auto_field(required=True)
    subject = auto_field(required=True)
    responsibility = auto_field(required=False)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        return Teacher(**data_dict)
