from rest_framework import serializers
from . import models

class FAQSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FAQ
        fields = '__all__'

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__'

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Ticket
        fields = '__all__'