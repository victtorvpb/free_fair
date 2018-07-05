from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ItsAliveView(APIView):
    def get(self, request):
        return Response({"message": "It's Alive"}, status=status.HTTP_200_OK)
