from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from members.models import Member
from members.serializer import MemberSerializer

# Create your views here.

class MemberApiView(APIView):
    def get(self, request):
        serializer = MemberSerializer(Member.objects.all(), many = True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
class MemberApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, id):
        member = self.get_object(id)
        serializer = MemberSerializer(member)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def put(self, request, id):
        member = self.get_object(id)
        if(member==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not Found data'})
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        member = self.get_object(id)
        member.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_200_OK, data=response)