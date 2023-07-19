from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)


class Process500:
    def __init__(self, get_responce):
        self._get_responce = get_responce

    def __call__(self, request):
        return self._get_responce(request)

    def process_exception(self, request, exception):
        logger.error(f"Error: {exception}")
        return redirect("home")
