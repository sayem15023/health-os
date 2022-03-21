from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import CompanySerializer, UserSerializer, PlanSerializer, PhoneNumberSerializer, PaymentInfoSerializer
from .models import PaymentInfo, User
from django.http import Http404


# Project views


class AppView(APIView):

    @api_view(['POST'])
    def index(request):
        s_data = CompanySerializer(data=request.data)
        if s_data.is_valid():
            print(s_data.data)
        return HttpResponse("Haaat the polls index.")


    def get_object(ModalTable, pk):
        try:
            return ModalTable.objects.get(pk=pk)
        except PaymentInfo.DoesNotExist:
            raise Http404

    @api_view(['POST'])
    def customer_registration(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def withdwaw_money(request, pk):
        payment_info = AppView.get_object(PaymentInfo, pk)
        serializer = PaymentInfoSerializer(payment_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def update_user_plan(request, pk):
        user = AppView.get_object(User, pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Additional for project


class AppViewAdditional(APIView):

    @api_view(['GET'])
    def get_all_user(request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Prerequisite for project


class AppViewPrerequisite(APIView):

    @api_view(['POST'])
    def save_company(request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    def save_plan(request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    def save_phone(request):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    def save_payment(request):
        serializer = PaymentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
