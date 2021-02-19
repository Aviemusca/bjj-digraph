from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """ Serializer for contact messages """

    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")