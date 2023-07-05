from django.shortcuts import render, redirect
from forum.models import *
from django.db.models import Count
from .filters import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.urls import reverse_lazy
import logging
from django.contrib import messages


logger = logging.getLogger(__name__)

