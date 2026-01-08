from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Add additional user data to the response (without adding to token)
        data['username'] = self.user.username
        data['user_type'] = self.user.user_type
        data['user_id'] = self.user.id

        return data
