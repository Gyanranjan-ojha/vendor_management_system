from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from os import getenv
from dotenv import load_dotenv
load_dotenv()

class APITokenAuthentication(BaseAuthentication):
    """Custom authentication class for API token-based authentication.

    This class extends the BaseAuthentication class provided by Django Rest Framework (DRF).
    It validates incoming requests based on the presence and correctness of an API token
    provided in the 'Authorization' header.

    Methods:
        authenticate(request):
            Validates the 'Authorization' header in the incoming request. It checks if the header
            is present, extracts the provided API token, and compares it with the expected API token
            stored in the environment settings. If the tokens match, the authentication is successful,
            and the method returns None. If the tokens do not match or the header is missing, an
            AuthenticationFailed exception is raised.
    """
    def authenticate(self, request):
        api_token = getenv("AUTH_TOKEN")

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise AuthenticationFailed("Invalid or missing Authorization header")

        elif api_token != auth_header:
            raise AuthenticationFailed("Invalid AUTH_TOKEN in Authorization header")

        # Authentication successful
        return None