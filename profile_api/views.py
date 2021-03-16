from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test APIView"""

    name = 'Hello Api View'
    def get(self, request, format=None):
        """Returns list of APIView features """
        an_api_view = [
            'Uses rest api methods as functions (get, post, put , patch and delete)',
            'Is similar to django View',
            'Give you most of the control over logic',
            'is mapped to urls'
        ]
        return Response({'message': 'Hello World', 'an_apiview': an_api_view})
