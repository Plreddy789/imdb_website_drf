from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True}

        }

    def validate(self, data):
        """
        Validate password confirmation and email uniqueness.
        """
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation',None)

        if password != password_confirmation:
            raise serializers.ValidationError("The passwords do not match.")

        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email address already exists. Please use a different email.")

        return data

    def save(self):
        """
        Create and return the user.
        """
        validated_data = self.validated_data
        account = User(email=validated_data['email'], username=validated_data['username'])
        account.set_password(validated_data['password'])
        account.save()
        return account