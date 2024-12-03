from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise, ExerciseCategory, EquipmentCategory
from .forms import ExerciseForm, ExerciseCategoryForm, EquipmentCategoryForm
from django.contrib.auth.decorators import login_required

# List all exercises
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_management/exercise_list.html', {'exercises': exercises})

# Detail view for a single exercise
def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'exercise_management/exercise_detail.html', {'exercise': exercise})

# Create a new exercise
@login_required
def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'exercise_management/exercise_form.html', {'form': form})

# Update an existing exercise
@login_required
def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'exercise_management/exercise_form.html', {'form': form})


# List all exercise categories
def exercise_category_list(request):
    categories = ExerciseCategory.objects.all()
    return render(request, 'exercise_management/exercise_category_list.html', {'categories': categories})

# Create a new exercise category
@login_required
def exercise_category_create(request):
    if request.method == 'POST':
        form = ExerciseCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exercise_category_list')
    else:
        form = ExerciseCategoryForm()
    return render(request, 'exercise_management/exercise_category_form.html', {'form': form})

# Update an exercise category
@login_required
def exercise_category_update(request, pk):
    category = get_object_or_404(ExerciseCategory, pk=pk)
    if request.method == 'POST':
        form = ExerciseCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('exercise_category_list')
    else:
        form = ExerciseCategoryForm(instance=category)
    return render(request, 'exercise_management/exercise_category_form.html', {'form': form})

# List all equipment categories
def equipment_category_list(request):
    equipment_categories = EquipmentCategory.objects.all()
    return render(request, 'exercise_management/equipment_category_list.html', {'equipment_categories': equipment_categories})

# Create a new equipment category
@login_required
def equipment_category_create(request):
    if request.method == 'POST':
        form = EquipmentCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_category_list')
    else:
        form = EquipmentCategoryForm()
    return render(request, 'exercise_management/equipment_category_form.html', {'form': form})

def exercise_category_delete(request, pk):
    # Get the category by pk or return a 404 error if not found
    category = get_object_or_404(ExerciseCategory, pk=pk)

    if request.method == "POST":
        # Delete the category
        category.delete()
        # Redirect to the exercise categories list page
        return redirect('exercise_category_list')  # Make sure to replace with your actual URL name

    # If it's not a POST request, render the confirmation page
    return render(request, 'exercise_management/exercise_category_confirm_delete.html', {'category': category})