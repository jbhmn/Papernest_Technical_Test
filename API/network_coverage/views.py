from rest_framework.decorators import api_view
from .functions import network_coverage_by_address
from rest_framework.response import Response

@api_view(['GET'])
def get_network_coverage(request):
    address = request.GET.get('q')
    return Response(network_coverage_by_address(address))