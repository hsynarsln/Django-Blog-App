from django.urls import path

from .views import create_post, post_list

urlpatterns = [
    path("", post_list, name="home"),
    # path("todos/", todo_list, name="todo_list"),
    path("create", create_post, name="create_post"),
    # path("todo/update/<int:id>", todo_update, name="todo_update"),
    # path("todo/delete/<int:id>", todo_delete, name="todo_delete"),
]
