from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from .schema import AssignmentSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_all_assignments(p):
    """Returns a list of all assignments"""
    all_assignments = Assignment.get_all_assignments()
    all_assignments_dump = AssignmentSchema().dump(all_assignments, many=True)
    return APIResponse.respond(data=all_assignments_dump)


@principal_assignments_resources.route('/assignments', methods=['DELETE'], strict_slashes=False)
@decorators.authenticate_principal
def delete_assignment(p, incoming_payload):
    """Principal can delete any assignment"""
    assignment_id = incoming_payload.get('id')
    Assignment.delete(assignment_id)
    db.session.commit()
    return APIResponse.respond(data={'message': 'Assignment deleted successfully'})
