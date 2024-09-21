from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of all teachers"""
    all_teachers = Teacher.get_all_teachers()
    all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
    return APIResponse.respond(data=all_teachers_dump)


@principal_teachers_resources.route('/teachers', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def assign_teacher(p, incoming_payload):
    """Assign a teacher to a class or responsibility"""
    teacher_id = incoming_payload.get('teacher_id')
    responsibility = incoming_payload.get('responsibility')
    Teacher.assign_responsibility(teacher_id, responsibility)
    db.session.commit()
    return APIResponse.respond(data={'message': 'Teacher assigned successfully'})
