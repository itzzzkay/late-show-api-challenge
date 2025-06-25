from flask import Blueprint, request, jsonify
from server.models.episode import Episode
from server.models import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episodes',__name__)

@episode_bp.route('/episodes',methods =['GET'])
@jwt_required()
def get_episodes():
    
    episodes = Episode.query.all()

    return jsonify([{'id':episode.name, 'number':episode.number,'date':episode.date.isoformat()}for episode in episodes])
