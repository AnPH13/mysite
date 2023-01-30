from rest_framework.serializers import *
from ..models.game import Game

class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id', 'name', 'status', 'created_at', 'updated_at', 'deleted_at'
        ]
    