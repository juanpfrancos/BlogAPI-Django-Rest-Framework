from django.contrib import admin
from django.urls import include, path 
from rest_framework.schemas import get_schema_view # new
from rest_framework.documentation import include_docs_urls # new


API_TITLE = 'Blog API' # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.' # new
schema_view = get_schema_view(title=API_TITLE) # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')), # new
    path('schema/', schema_view), # new
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)), # new
]
