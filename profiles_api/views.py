from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test the API view"""
    def get(self, request, format=None):
        """Returns a list of apiview features"""
        an_apiview=[
        'uses http methods as a function (get, post, patch, put, delete)',
        'is similar to a traditional django view',
        'gives you the most control over your app logic',
        'is mapped manually to urls',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})
