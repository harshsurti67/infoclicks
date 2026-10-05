from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import ContactEnquiry
from .serializers import ContactEnquirySerializer


class ContactEnquiryListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        List all contact enquiries.
        """
        enquiries = ContactEnquiry.objects.all()
        serializer = ContactEnquirySerializer(enquiries, many=True)
        return Response({
            "status": "success",
            "count": enquiries.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Submit a new project contact enquiry.
        """
        serializer = ContactEnquirySerializer(data=request.data)
        if serializer.is_valid():
            enquiry = serializer.save()
            return Response({
                "status": "success",
                "message": "Thanks! Your enquiry has been received. We'll get back to you soon.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "message": "Please correct the errors in the form.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
