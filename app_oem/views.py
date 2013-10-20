def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}