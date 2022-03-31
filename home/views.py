from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    """A view to return the index page"""

    logger.error('Test')

    return render(request, 'home/index.html')