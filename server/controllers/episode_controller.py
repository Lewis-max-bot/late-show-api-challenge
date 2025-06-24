from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models import db

episode_bp = Blueprint("episode_bp", __name__, url_prefix="/episodes")

@episode_bp.route("", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {
            "id": episode.id,
            "date": episode.date,
            "number": episode.number
        }
        for episode in episodes
    ])

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "id": app.id,
                "rating": app.rating,
                "guest": {
                    "id": app.guest.id,
                    "name": app.guest.name,
                    "occupation": app.guest.occupation
                }
            } for app in episode.appearances
        ]
    })

@episode_bp.route("/<int:id>", methods=["DELETE"])
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({ "message": "Episode deleted successfully" }), 200
