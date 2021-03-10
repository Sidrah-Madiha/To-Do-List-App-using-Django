from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from .models import Todo


def list_view(request):
	Todos = Todo.objects.all().order_by("-added_date")
	context = {
		'object_list' : Todos
		}
	#create
	if request.method == "POST":
		current_date = timezone.now()
		content = request.POST["content"]
		create_object = Todo.objects.create(added_date=current_date, text=content)
		# return render(request, 'todolist/index.html')
	return render(request, 'todolist/index.html', context)
	# if request.method == None:
	# 	Todos = Todo.objects.all().order_by("added_date")
	# 	context = {
	# 	'object_list' : Todos
	# 	}
	# 	return render(request, 'todolist/index.html', context)
def delete_view(request, todo_id):
	print(todo_id)
	item = get_object_or_404(Todo, id=todo_id)
	print(item)
	if request.method == "POST":
		item.delete()
		return redirect('../../todolist/')
		#../todolist/
	else:
		context = {'item': item}

		return render(request,'todolist/delete.html', context )