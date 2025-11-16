from django.urls import path
from members.views import MemberApiView, MemberApiViewDetail

urlpatterns = [
    path('v1/members', MemberApiView.as_view()),
    path('v1/members/<int:id>', MemberApiViewDetail.as_view())
]
