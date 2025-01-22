from flask import Blueprint
from controllers.PublisherController import get_publishers, get_publisher, add_publisher, update_publisher, delete_publisher
from flask_cors import CORS

CORS(blueprint_instance, resources={r"/*": {"origins": "https:/https://gamingdb-test4.vercel.app/"}}, supports_credentials=True)


publisher_bp = Blueprint('publisher_bp', __name__)

publisher_bp.route('/api/publishers', methods=['GET'])(get_publishers)
publisher_bp.route('/api/publishers/<int:publisher_id>', methods=['GET'])(get_publisher)
publisher_bp.route('/api/publishers', methods=['POST'])(add_publisher)
publisher_bp.route('/api/publishers/<int:publisher_id>', methods=['PUT'])(update_publisher)
publisher_bp.route('/api/publishers/<int:publisher_id>', methods=['DELETE'])(delete_publisher)
