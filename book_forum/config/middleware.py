from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


class Process500:
    def __init__(self, get_responce):
        self._get_responce = get_responce

    def __call__(self, request):
        return self._get_responce(request)

    def process_exception(self, request, exception):
        match exception:
            case ValueError():
                logger.error(f"Error: {exception}")
                message = "Помилка даних"
            case _:
                logger.error(f"Error: {exception}")
                message = "Помилка"
        response = render(request, "base/500.html", {"message": message})
        response.status_code = 500
        return response
