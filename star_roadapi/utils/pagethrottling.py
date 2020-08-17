from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    cursor_query_param = 'page'  # 每一页查询的key
    page_size = 5  #每页显示的条数
    ordering = '-id'  #排序字段




from rest_framework.pagination import PageNumberPagination
class Mypage(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    # 定制传参
    page_size_query_param = 'size'
    # 最大一页的数据
    max_page_size = 5


