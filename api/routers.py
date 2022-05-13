from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersList)
router.register(r'columns', views.ColumnsList)
router.register(r'cards', views.CardsList)