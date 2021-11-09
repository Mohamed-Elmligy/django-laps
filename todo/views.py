from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.http.response import JsonResponse

from pprint import pprint


# Create your views here.

def index(request):
    return render(request, 'main/base_layout.html')


my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Interstellar',
        'priority': 1,
        'description': "Interstellar is about Earth's last chance to find a habitable planet before a lack of resources causes the human race to go extinct. The film's protagonist is Cooper (Matthew McConaughey), a former NASA pilot who is tasked with leading a mission through a wormhole to find a habitable planet in another galaxy.",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Avatar ',
        'priority': 4,
        'description': "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home. When his brother is killed in a robbery, paraplegic Marine Jake Sully decides to take his place in a mission on the distant world of Pandora.",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Harry Potter',
        'priority': 2,
        'description': "Throughout the series, Harry is described as having his father's perpetually untidy black hair, his mother's bright green eyes, and a lightning bolt-shaped scar on his forehead. He is further described as small and skinny for his age with a thin face and knobbly knees, and he wears Windsor glasses.",

    },
]


def _get_target_task(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)

    # Getting index of the required task from my_task_list
    index_of_task = my_task_list.index(final_list[0])

    return index_of_task


def todo_list(request):
    my_context = {'task_list': my_task_list, }
    return render(request, 'todo/todo_list.html', context=my_context)


def todo_update(request, **kwargs):
    task_id = kwargs.get('task_id')
    index_to_update = _get_target_task(task_id)
    my_task_list[index_to_update]['name'] = 'Updated {}'.format(my_task_list[index_to_update].get('name'))

    return redirect('todo:todo-list')


def todo_delete(request, **kwargs):
    task_id = kwargs.get('task_id')

    index_to_delete = _get_target_task(task_id)

    if my_task_list:
        my_task_list.pop(index_to_delete)

    return redirect('todo:todo-list')


def todo_detail(request, *args, **kwargs):

    # NEW CONTEXT
    task_id = kwargs.get('task_id')

    task_index = _get_target_task(task_id)

    my_task_dictionary = my_task_list[task_index]

    my_context = {
        'task_id': my_task_dictionary.get('id'),
        'task_name': my_task_dictionary.get('name'),
        'task_priority': my_task_dictionary.get('priority'),
        'task_description': my_task_dictionary.get('description')
    }

    return render(request, 'todo/todo_detail.html', context=my_context)
