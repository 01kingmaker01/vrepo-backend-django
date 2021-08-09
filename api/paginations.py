from rest_framework.pagination import CursorPagination


class PostCursorPagination(CursorPagination):
    page_size =7
    cursor_query_param = 'c'
    ordering = '-id'