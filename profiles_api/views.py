from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions

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


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return hello message"""
        a_viewset = [
            'users actions (list, create, retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more functionality with less code',
        ]
        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # contrary to APIviews, these will only appear on GUI
    # if you add an id to the url.
    def retrieve(self, request, pk=None):
        """handles getting an object by id"""
        return Response({'hhtp_method': 'GET'})

    def update(self, request, pk=None):
        """handles updating an object by id"""
        return Response({'hhtp_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handles partial updating an object by id"""
        return Response({'hhtp_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handles deleting an object by id"""
        return Response({'hhtp_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
