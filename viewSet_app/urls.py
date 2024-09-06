from django.urls import path
from .views import *

urlpatterns=[
    path('detail/',detial_viewset.as_view(
        {
        "get":"list",
        "post":"create",

    }
    ),
    
),
path ('detail/<int:pk>',single_detail_viewset.as_view({
        "patch": "partial_update",
        "delete": "destroy",

    }
    )
    ),
]