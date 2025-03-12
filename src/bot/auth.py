from urllib.parse import urlencode

from config_proxy import INSTAGRAM_CLIENT_ID, INSTAGRAM_CLIENT_SECRET, INSTAGRAM_REDIRECT_URI

class InstagramAuthService:

    def __init__(self):
        self.client_id: str = INSTAGRAM_CLIENT_ID
        self.client_secret: str = INSTAGRAM_CLIENT_SECRET
        self.redirect_uri: str = INSTAGRAM_REDIRECT_URI
        self.base_auth_url: str = 'https://api.instagram.com/oauth/authorize'
        self.token_url: str = 'https://api.instagram.com/oauth/access_token'

    def generate_authorization_url(self, state: str="") -> str:
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': 'user_profile,user_media',
            'response_type': 'code',
            'state': state or ''
        }

        return f"{self.base_auth_url}?{urlencode(params)}"
        """
        Create or update Instagram OAuth token for a user

        :param user: Django User instance
        :param token_response: Token response from Instagram
        :return: InstagramOAuthToken instance
        """
        # Fetch user profile to get Instagram user ID
        profile = self.fetch_user_profile(token_response.get('access_token'))

        if not profile:
            raise ValueError("Unable to fetch user profile")

        # Create or update token
        token, created = InstagramOAuthToken.objects.update_or_create(
            user=user,
            instagram_user_id=profile.get('id'),
            defaults={
                'instagram_username': profile.get('username'),
                'access_token': token_response.get('access_token'),
                'refresh_token': token_response.get('refresh_token'),
                'expires_at': timezone.now() + timezone.timedelta(
                    seconds=token_response.get('expires_in', 3600)
                ),
                'scope': token_response.get('scope', 'user_profile,user_media')
            }
        )

        return token