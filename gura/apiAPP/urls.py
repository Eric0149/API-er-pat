from django.urls import path
from .views import ProductListView, CartView, OrderListView, OrderCreateAPIView, AddToCartView
from drf_yasg.views import get_schema_view
# for Documenting orders
from drf_yasg import openapi
from django.conf.urls.static import static
from gura import settings
schema_view = get_schema_view(
    openapi.Info(
        title="ALL OF MY APIs",
        default_version='v1',
        description="ALL APIs Documentations",
        terms_of_service="#",
        contact=openapi.Contact(email="eris@admin.com"),
        license=openapi.License(name="3rr"),
    ),
    public=True,
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart-list'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('create-order/', OrderCreateAPIView.as_view(), name='create-order'),

    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
