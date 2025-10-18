from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    user = request.user
    notifications = user.notifications.all()

    unread = notifications.filter(read=False)
    unread.update(read=True)  # mark as read when fetched

    data = [
        {
            'id': n.id,
            'actor': n.actor.username,
            'verb': n.verb,
            'target': str(n.target),
            'timestamp': n.timestamp,
            'read': n.read,
        }
        for n in notifications
    ]
    return Response(data)
