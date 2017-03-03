from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from crater_finder import views
from crater_locator import settings

router = routers.DefaultRouter()
router.register(r'v1/vehicle', views.VehicleViewSet, base_name='vehicle')
router.register(r'v1/crater', views.CraterViewSet, base_name='crater')
router.register(r'v1/falls', views.FallViewSet, base_name='fall')

urlpatterns = [
                  url(r'^api/', include(router.urls, namespace='api')),
                  url(r'^api/v1/token/', views.ObtainAuthToken.as_view()),
                  url(r'^api/v1/report/', views.ReceiveReport.as_view()),
                  url(r'^api/v1/employees/(?P<pk>[0-9]+)/$',
                      views.EmployeeDetails.as_view(),
                      name='employee-detail'),
                  url(r'^api/v1/craters/(?P<pk>[0-9]+)/$',
                      views.CraterDetails.as_view(),
                      name='crater-detail'),
                  url(r'^api/open/craters/', views.ListCraters.as_view(), name="list_craters"),
                  url(r'^admin/', admin.site.urls),
                  url(r'^docs/', include('rest_framework_docs.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
