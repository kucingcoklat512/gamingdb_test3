from flask import Blueprint
from controllers.PlatformController import get_platforms, get_platform, add_platform, update_platform, delete_platform
from flask_cors import CORS



platform_bp = Blueprint('platform_bp', __name__)
CORS(blueprint_instance, resources={r"/*": {"origins": "https:/https://gamingdb-test4.vercel.app/"}}, supports_credentials=True)
platform_bp.route('/api/platforms', methods=['GET'])(get_platforms)
platform_bp.route('/api/platforms/<int:platform_id>', methods=['GET'])(get_platform)
platform_bp.route('/api/platforms', methods=['POST'])(add_platform)
platform_bp.route('/api/platforms/<int:platform_id>', methods=['PUT'])(update_platform)
platform_bp.route('/api/platforms/<int:platform_id>', methods=['DELETE'])(delete_platform)
