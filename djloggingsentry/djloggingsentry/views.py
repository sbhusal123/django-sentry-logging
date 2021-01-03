from django.http import HttpResponse

from logging import getLogger

logger = getLogger(__name__)

def test_view(request, pk):
    if pk > 10:
        logger.warn("Resolve here")
        logger.error("Value Too great: pk")
        return HttpResponse ("Value too great")

    return HttpResponse (f"value is{pk}")