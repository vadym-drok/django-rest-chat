from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def MessageList(request, pk):
    # view with a list of messages
    # pagination for 10 messages:  ..list/0/ => 1:10

    all_messages = Message.objects.all()
    pagination_message = []

    for x in range(pk*10, (pk+1) * 10):
        if x < len(all_messages):
            # create a list with 10 (or less) messages

            b = all_messages[x]
            pagination_message.append(b)

    queryset = pagination_message
    serializer = MessageSerializer(queryset, many=True)

    return Response(serializer.data)


class MessageDetailView(generics.RetrieveAPIView):
    # detail view for a single message
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreateView(generics.CreateAPIView):
    # view for a created single message
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
