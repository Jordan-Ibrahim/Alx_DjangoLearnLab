from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model (or default if not replaced)
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for viewing and updating user profiles."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for registering a new user."""
    # Explicitly declare the password as a CharField (write-only)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Use Django's built-in create_user() to hash passwords correctly
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Automatically create an authentication token for the new user
        Token.objects.create(user=user)
        return user
