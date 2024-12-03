from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Exercise, ExerciseCategory, EquipmentCategory
from .serializers import ExerciseSerializer, ExerciseCategorySerializer, EquipmentCategorySerializer
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# List all exercises
class ExerciseListView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

@api_view(['POST'])
def exercise_create(request):
    if request.method == 'POST':
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad Request

    # Update an existing exercise category
@api_view(['PUT'])
def exercise_update(request, pk):
    category = get_object_or_404(Exercise, pk=pk)
    if request.method == 'PUT':
        serializer = ExerciseSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # Updated
        return Response(serializer.errors, status=400)  # Bad Request

    # Delete an exercise category
@api_view(['DELETE'])
def exercise_delete(request, pk):
    category = get_object_or_404(Exercise, pk=pk)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=204)  # No Content

# Detail view for a single exercise
class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# List all exercise categories
class ExerciseCategoryListView(generics.ListCreateAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

# Create a new exercise category
@api_view(['POST'])
def exercise_category_create(request):
    if request.method == 'POST':
        serializer = ExerciseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad Request

# Update an existing exercise category
@api_view(['PUT'])
def exercise_category_update(request, pk):
    category = get_object_or_404(ExerciseCategory, pk=pk)
    if request.method == 'PUT':
        serializer = ExerciseCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # Updated
        return Response(serializer.errors, status=400)  # Bad Request

# Delete an exercise category
@api_view(['DELETE'])
def exercise_category_delete(request, pk):
    category = get_object_or_404(ExerciseCategory, pk=pk)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=204)  # No Content

# Update or Delete an exercise category
class ExerciseCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

# List all equipment categories
class EquipmentCategoryListView(generics.ListCreateAPIView):
    queryset = EquipmentCategory.objects.all()
    serializer_class = EquipmentCategorySerializer

# Create a new equipment category
@api_view(['POST'])
def equipment_category_create(request):
    if request.method == 'POST':
        serializer = EquipmentCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad Request


# Delete an exercise category
@api_view(['DELETE'])
def exercise_category_delete(request, pk):
    category = get_object_or_404(ExerciseCategory, pk=pk)

    if request.method == 'DELETE':
        category.delete()
        return Response(status=204)  # No Content

