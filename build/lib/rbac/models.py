from django.db import models
from django.contrib.auth.models import AbstractUser

class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    path = models.CharField(max_length=158, null=True, blank=True, verbose_name="链接地址")
    is_frame = models.BooleanField(default=False, verbose_name="外部菜单")
    is_show = models.BooleanField(default=True, verbose_name="显示标记")
    sort = models.IntegerField(null=True, blank=True, verbose_name="排序标记")
    component = models.CharField(max_length=200, null=True, blank=True, verbose_name="组件")
    pid = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Permission(models.Model):
    """
    权限
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="权限名")
    method = models.CharField(max_length=50, null=True, blank=True, verbose_name="方法")
    pid = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父权限")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Role(models.Model):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色")
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name="权限")
    menus = models.ManyToManyField("Menu", blank=True, verbose_name="菜单")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")
    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Organization(models.Model):
    """
    组织架构
    """
    organization_type_choices = (
        ("company", "company"),
        ("department", "department")
    )
    name = models.CharField(max_length=60, verbose_name="name")
    type = models.CharField(max_length=20, choices=organization_type_choices, default="company", verbose_name="type")
    pid = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="main organization")

    class Meta:
        verbose_name = "organization"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    '''
    User
    '''
    name = models.CharField(max_length=20, default="", verbose_name="name")
    mobile = models.CharField(max_length=11, default="", verbose_name="mobile number")
    email = models.EmailField(max_length=50, verbose_name="image")
    image = models.ImageField(upload_to="static/%Y/%m", default="image/default.png",
                              max_length=100, null=True, blank=True)
    department = models.ForeignKey("Organization", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="department")
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name="position")
    superior = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="superior")
    roles = models.ManyToManyField("Role", verbose_name="roles", blank=True)

    class Meta:
        verbose_name = "User info"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username
