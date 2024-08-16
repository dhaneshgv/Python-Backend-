# # from django.shortcuts import render

# # # Create your views here.
# # from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.parsers import JSONParser
# # from django.http.response import JsonResponse
# # from student.serializers import StudentSerializer
# # from student.models import Student


# # @csrf_exempt
# # def studentApi(request,id=0):
# #     if request.method=='GET':
# #         student = Student.objects.all()
# #         student_serializer=StudentSerializer(student,many=True)
# #         return JsonResponse(student_serializer.data,safe=False)
# #     elif request.method=='POST':
# #         student_data=JSONParser().parse(request)
# #         student_serializer=StudentSerializer(data=student_data)
# #         if student_serializer.is_valid():
# #             student_serializer.save()
# #             return JsonResponse("Added Successfully",safe=False)
# #         return JsonResponse("Failed to Add",safe=False)
# #     elif request.method=='PUT':
# #         student_data=JSONParser().parse(request)
# #         student=Student.objects.get(id=id)
# #         student_serializer=StudentSerializer(student,data=student_data)
# #         if student_serializer.is_valid():
# #             student_serializer.save()
# #             return JsonResponse("Updated Successfully",safe=False)
# #         return JsonResponse("Failed to Update")
# #     elif request.method=='DELETE':
# #         student=Student.objects.get(id=id)
# #         student.delete()
# #         return JsonResponse("Deleted Successfully",safe=False)




# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from rest_framework import status
# # from .models import Student
# # from .serializers import StudentSerializer

# # @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# # def studentApi(request, pk=None):
# #     if request.method == 'GET':
# #         if pk:
# #             # Retrieve a specific student
# #             try:
# #                 student = Student.objects.get(pk=pk)
# #             except Student.DoesNotExist:
# #                 return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
# #             serializer = StudentSerializer(student)
# #             return Response(serializer.data)
# #         else:
# #             # List all students
# #             students = Student.objects.all()
# #             serializer = StudentSerializer(students, many=True)
# #             return Response(serializer.data)

# #     elif request.method == 'POST':
# #         # Create a new student
# #         serializer = StudentSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     elif request.method == 'PUT':
# #         if pk:
# #             # Update a specific student
# #             try:
# #                 student = Student.objects.get(pk=pk)
# #             except Student.DoesNotExist:
# #                 return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
# #             serializer = StudentSerializer(student, data=request.data, partial=True)  # Use partial=True for partial updates
# #             if serializer.is_valid():
# #                 serializer.save()
# #                 return Response(serializer.data)
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #         return Response({"error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)

# #     elif request.method == 'DELETE':
# #         if pk:
# #             # Delete a specific student
# #             try:
# #                 student = Student.objects.get(pk=pk)
# #             except Student.DoesNotExist:
# #                 return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
# #             student.delete()
# #             return Response(status=status.HTTP_204_NO_CONTENT)
# #         return Response({"error": "ID is required for delete"}, status=status.HTTP_400_BAD_REQUEST)


# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from student.serializers import StudentSerializer
# from student.models import Student



# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework import status

# @csrf_exempt
# def studentApi(request, pk=0):
#     if request.method == 'GET':
#         if pk > 0:
#             try:
#                 student = Student.objects.get(id=pk)
#                 student_serializer = StudentSerializer(student)
#                 return JsonResponse(student_serializer.data, safe=False)
#             except Student.DoesNotExist:
#                 return JsonResponse({"error": "Student not found"}, status=404)
#         else:
#             students = Student.objects.all()
#             student_serializer = StudentSerializer(students, many=True)
#             return JsonResponse(student_serializer.data, safe=False)

#     elif request.method == 'POST':
#         student_data = JSONParser().parse(request)
#         student_serializer = StudentSerializer(data=student_data)
#         if student_serializer.is_valid():
#             student_serializer.save()
#             return JsonResponse({"message": "Added Successfully"}, status=201)
#         return JsonResponse(student_serializer.errors, status=400)

#     elif request.method == 'PUT':
#         if pk > 0:
#             try:
#                 student = Student.objects.get(id=pk)
#                 student_data = JSONParser().parse(request)
#                 student_serializer = StudentSerializer(student, data=student_data, partial=True)  # partial=True for partial updates
#                 if student_serializer.is_valid():
#                     student_serializer.save()
#                     return JsonResponse({"message": "Updated Successfully"}, status=200)
#                 return JsonResponse(student_serializer.errors, status=400)
#             except Student.DoesNotExist:
#                 return JsonResponse({"error": "Student not found"}, status=404)
#         return JsonResponse({"error": "ID is required for update"}, status=400)

#     elif request.method == 'DELETE':
#         if pk > 0:
#             try:
#                 student = Student.objects.get(id=pk)
#                 student.delete()
#                 return JsonResponse({"message": "Deleted Successfully"}, status=204)
#             except Student.DoesNotExist:
#                 return JsonResponse({"error": "Student not found"}, status=404)
#         return JsonResponse({"error": "ID is required for delete"}, status=400)
# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
#     return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def signup_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     try:
#         user = User.objects.create_user(username=username, password=password)
#         return JsonResponse({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
#     except:
#         return JsonResponse({'message': 'Error creating user'}, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from student.serializers import StudentSerializer
from student.models import Student

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def studentApi(request, pk=0):
    if request.method == 'GET':
        if pk > 0:
            try:
                student = Student.objects.get(id=pk)
                student_serializer = StudentSerializer(student)
                return JsonResponse(student_serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, status=404)
        else:
            students = Student.objects.all()
            student_serializer = StudentSerializer(students, many=True)
            return JsonResponse(student_serializer.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=201)
        return JsonResponse(student_serializer.errors, status=400)

    elif request.method == 'PUT':
        if pk > 0:
            try:
                student = Student.objects.get(id=pk)
                student_data = JSONParser().parse(request)
                student_serializer = StudentSerializer(student, data=student_data, partial=True)
                if student_serializer.is_valid():
                    student_serializer.save()
                    return JsonResponse({"message": "Updated Successfully"}, status=200)
                return JsonResponse(student_serializer.errors, status=400)
            except Student.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, status=404)
        return JsonResponse({"error": "ID is required for update"}, status=400)

    elif request.method == 'DELETE':
        if pk > 0:
            try:
                student = Student.objects.get(id=pk)
                student.delete()
                return JsonResponse({"message": "Deleted Successfully"}, status=204)
            except Student.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, status=404)
        return JsonResponse({"error": "ID is required for delete"}, status=400)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def signup_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')  # Optional field

    if not username or not password:
        return JsonResponse({'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({'message': f'Error creating user: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
