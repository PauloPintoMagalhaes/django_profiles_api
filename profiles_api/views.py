from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test the API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of apiview features"""
        an_apiview=[
        'uses http methods as a function (get, post, patch, put, delete)',
        'is similar to a traditional django view',
        'gives you the most control over your app logic',
        'is mapped manually to urls',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        # pk means primary key, if updating a current item
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle patching an item"""
        return Response({'method': 'PATCH'})

    def delete(seld, request, pk=None):
        """Handle deleting an item"""
        return Response({'method': 'PATCH'})
