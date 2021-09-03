from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class PostCursorPagination(CursorPagination):
    page_size =5
    cursor_query_param = 'c'
    ordering = '-id'