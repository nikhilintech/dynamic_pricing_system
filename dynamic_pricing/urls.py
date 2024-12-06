"""
URL configuration for dynamic_pricing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path 

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



# from django.contrib import admin
# from django.urls import path, include  # Import both `path` and `include`

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin routes
#     path('api/', include('pricing.urls')),  # Include the routes from `pricing.urls`
# ]


from django.contrib import admin
from django.urls import path, include
from pricing import views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pricing.urls')),  # Include API routes from the 'pricing' app
    path('', views.home),  # This will handle the root URL (http://127.0.0.1:8080/)
]




