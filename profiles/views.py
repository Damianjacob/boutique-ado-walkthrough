from multiprocessing import context
from django.shortcuts import render, get_object_or_404


def profile(request):
    """display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)