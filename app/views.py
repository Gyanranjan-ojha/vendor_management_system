from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .auth.authentication import APITokenAuthentication

class CheckAPIView(APIView):
    """
    API view for checking the APITokenAuthentication status.
    """
    authentication_classes = [APITokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "APITokenAuthentication status is fine."}, status=status.HTTP_200_OK)
