from flask import Blueprint
from controllers.DeveloperController import get_developers, get_developer, add_developer, update_developer, delete_developer, patch_developer
from flask_cors import CORS

CORS(blueprint_instance, resources={r"/*": {"origins": "https:/https://gamingdb-test4.vercel.app/"}}, supports_credentials=True)

developer_bp = Blueprint('developer_bp', __name__)

developer_bp.route('/api/developers', methods=['GET'])(get_developers)
developer_bp.route('/api/developers/<int:id_dev>', methods=['GET'])(get_developer)
developer_bp.route('/api/developers', methods=['POST'])(add_developer)
developer_bp.route('/api/developers/<int:id_dev>', methods=['PUT'])(update_developer)
developer_bp.route('/api/developers/<int:id_dev>', methods=['PATCH'])(patch_developer)
developer_bp.route('/api/developers/<int:id_dev>', methods=['DELETE'])(delete_developer)
