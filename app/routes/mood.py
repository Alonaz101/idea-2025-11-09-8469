from flask import Blueprint, request, jsonify
from .. import db
from ..models import Mood, Recipe
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('mood', __name__)

@bp.route('/', methods=['POST'])
@jwt_required()
def submit_mood():
    data = request.get_json()
    mood = data.get('mood')
    user_id = get_jwt_identity()
    if not mood:
        return jsonify({"msg": "Mood is required"}), 400

    mood_entry = Mood(mood=mood, user_id=user_id)
    db.session.add(mood_entry)
    db.session.commit()

    # Simplified recommendation engine: find recipes tagged with this mood
    recommended = Recipe.query.filter(Recipe.mood_tags.contains(mood)).all()
    recommendations = [{"id": r.id, "title": r.title} for r in recommended]
    
    return jsonify({"recommendations": recommendations}), 200
