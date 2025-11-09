from flask import Blueprint, jsonify
from ..models import Recipe
from flask_jwt_extended import jwt_required

bp = Blueprint('recipes', __name__)

@bp.route('/<int:recipe_id>', methods=['GET'])
@jwt_required()
def get_recipe_details(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    detailed_info = {
        "id": recipe.id,
        "title": recipe.title,
        "ingredients": recipe.ingredients,
        "steps": recipe.steps,
        "nutrition": recipe.nutrition,
        "mood_tags": recipe.mood_tags.split(",") if recipe.mood_tags else []
    }
    return jsonify(detailed_info)
