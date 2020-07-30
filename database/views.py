from rest_framework.response import Response
from rest_framework.views import APIView

from .models import deal
from .serializers import DealSerializer


class DealView(APIView):
    def get(self, request):
        deals = deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response({"deals": serializer.data})

    def post(self, request):
        deal = request.data.get('deal')

        # Create an article from the above data
        serializer = DealSerializer(data=deal)
        if serializer.is_valid(raise_exception=True):
            deal_saved = serializer.save()
        return Response({"success": "Deal '{}' created successfully".format(deal_saved.title)})