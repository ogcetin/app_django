from django.urls import include, path
from rest_framework import routers
from api import views

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'datas', views.DataViewSet)
router.register(r'activities', views.ActivityViewSet)
# router.register(r'staffs', views.StaffViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/changePassword/', views.changePasswordFormView),
    path('api/activitiesByDataID/<int:data_id>/', views.activityListByDataIDView)
]