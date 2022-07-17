from rest_framework import serializers

from ...models import CandleStick


class ConsultaPeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandleStick
        fields = 'period', 'dolar', 'real', 'euro', 'jpy'
        read_only_fields = fields