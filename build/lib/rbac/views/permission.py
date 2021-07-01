from rest_framework.viewsets import ModelViewSet
from ..models import Permission
from ..serializers.permission_serializer import PermissionListSerializer
from utils.custom import CommonPagination, RbacPermission, TreeAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class PermissionViewSet(ModelViewSet, TreeAPIView):
    '''
    Permission: add, delete, modify and check
    '''
    perms_map = ({'*': 'admin'}, {'*': 'permission_all'}, {'get': 'permission_list'}, {'post': 'permission_create'},
                 {'put': 'permission_edit'},{'delete': 'permission_delete'})
    queryset = Permission.objects.all()
    serializer_class = PermissionListSerializer
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)


class PermissionTreeView(TreeAPIView):
    '''
    Permission tree
    '''
    queryset = Permission.objects.all()
