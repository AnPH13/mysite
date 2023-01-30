from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..models.game import Game
from ..serializers.game_serializer import GameSerializer

class GameView(ViewSet):
    def get_all(self, request):
        queryset = Game.objects.filter()
        serializer = GameSerializer(queryset, many=True)
        
        return Response(serializer.data)