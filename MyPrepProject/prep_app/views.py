from django.http import HttpResponse, request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ApplicationUser
from .serializers import ATMWithdrawalSerializer


def view1(request):
    return HttpResponse("This is view 1.")


def view2(request):
    return HttpResponse("This is view 2.")


def view3(request):
    users = ApplicationUser.objects.all()
    return HttpResponse(users)


'''
API
'''


class ATMWithdrawalView(APIView):
    def post(self, request):
        serializer = ATMWithdrawalSerializer(data=request.data)
        if serializer.is_valid():
            # Process withdrawal (dummy response for now)
            return Response({"message": "Withdrawal successful!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
blogpost API
'''
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostView(APIView):
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)