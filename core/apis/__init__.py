from core import app
from .responses import APIResponse
from .assignments import student_assignments_resources, teacher_assignments_resources, principal_assignments_resources
from .teachers import principal_teachers_resources

# Register Blueprints
app.register_blueprint(student_assignments_resources, url_prefix='/student')
app.register_blueprint(teacher_assignments_resources, url_prefix='/teacher')
app.register_blueprint(principal_assignments_resources, url_prefix='/principal/assignments')
app.register_blueprint(principal_teachers_resources, url_prefix='/principal/teachers')

# Set custom response class
app.response_class = APIResponse
