from rest_framework.generics import (
    ListAPIView,
)

from ..serializers import ConsultaPeriodoSerializer
from ...models import CandleStick
from datetime import datetime, timedelta
from rest_framework.exceptions import ValidationError

from ...utils import valida_moeda_informada


class ConsultaPeriodoListAPIView(ListAPIView):
    serializer_class = ConsultaPeriodoSerializer

    def get_queryset(self):
        verifica_moeda = valida_moeda_informada(self.kwargs['moeda'].lower())
        if not verifica_moeda:
            raise ValidationError({
                   "error":
                       "moeda informada não existe. favor informar "
                       "somente (euro, jpy, real)"
            })
        
        day_init = datetime.strptime(self.kwargs['init'], '%Y-%m-%d')
        day_end = (
            datetime.strptime(self.kwargs['end'], '%Y-%m-%d') +
            timedelta(hours=23, minutes=59, seconds=59)
        )

        if int(day_end.timestamp() - day_init.timestamp()) < 432000:
            dados = CandleStick.objects.filter(
                period__range=(
                    day_init, day_end
                )
            ).values('period', 'dolar', self.kwargs['moeda'].lower())

            return dados
        else:
            raise ValidationError({
                "error date":
                    "Intervalo maximo de 5 dias"
            })
