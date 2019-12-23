from django.shortcuts import render
# Create your views here.
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def get(self, request):
        print(request.data)
        employee_master_list = Lead.objects.all()
        serializer = LeadSerializer(employee_master_list, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # try:
        #     employee = Lead.objects.get(employee_id__iexact=request.data.get('employee_id'))
        #     return Response({"error": constants.EMPLOYEE_ALREADY_EXISTS, "message": "error"}, status.HTTP_400_BAD_REQUEST)
        # except models.Employee.DoesNotExist:
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"})
        return Response({"message": "error"})



     



class LeadListCreate_data(APIView):
    def get_object(self, pk):
        try:
            return Lead.objects.get(pk=pk)
        except Lead.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        emp_data = self.get_object(pk)
        emp_data.delete()
        return Response({"message": "success"}, status.HTTP_204_NO_CONTENT)


    # def post(self, request):
    #     return Response({"error": "", "data": {'name':,s},
    #                  "error_code": ""})


