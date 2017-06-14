
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from datetime import datetime 
from Addons.test.models.fecha import Fecha


class FechaSerializer(serializers.Serializer):
    hora_actual = serializers.DateTimeField()
    class Meta:
    	fields = ('hora_actual')

class FechaViewSet(viewsets.ModelViewSet):
	queryset = Fecha.objects.all()
	serializer_class = FechaSerializer
	def list(self, request): 
		return Response({"hora_actual": (datetime.now()).isoformat()})
 