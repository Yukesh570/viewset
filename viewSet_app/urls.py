from django.urls import path
from .views import *
from . import views
urlpatterns=[
    path('detail/',detial_viewset.as_view(
        {
        "get":"list",
        "post":"create",
        "patch": "partial_update",
        "delete": "destroy",

    }
    ),
    
),
path('detail/<int:pk>',detial_viewset.as_view(
        {
        "get":"retrieve",
        "patch": "partial_update",
        "delete": "destroy",

    }
    ),
    
),
# path ('detail/<int:pk>',single_detail_viewset.as_view({
#         "patch": "partial_update",
#         "delete": "destroy",

#     }
#     )
#     ),
path ('hi/',views.test,name="test")
]