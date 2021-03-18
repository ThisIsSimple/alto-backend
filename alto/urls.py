"""alto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from rest_framework import routers
from rest_framework_nested import routers as nestedRouter
from users import views as usersView
from ranks import views as ranksView
from departments import views as departmentsView
from labels import views as labelsView
from tasks import views as tasksView
from reports import views as reportsView
from attachments import views as attachmentsView

# router = routers.DefaultRouter()
router = nestedRouter.DefaultRouter()
router.register(r'users', usersView.UserViewSet)
router.register(r'ranks', ranksView.RankViewSet)
router.register(r'departments', departmentsView.DepartmentViewSet)
router.register(r'labels', labelsView.LabelViewSet)
router.register(r'tasks', tasksView.TaskViewSet)
router.register(r'task_progresses', tasksView.TaskProgressViewSet)
router.register(r'attachments', attachmentsView.AttachmentViewSet)
router.register(r'reports', reportsView.ReportViewSet)

user_router = nestedRouter.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'tasks/own', usersView.UserTaskOwnViewSet)
user_router.register(r'tasks/ordered',
                     usersView.UserTaskProgressOrderedByViewSet)
user_router.register(r'tasks/received',
                     usersView.UserTaskProgressOrderedToViewSet)
# user_router.register(r'ordered_by_tasks', usersView.UserTaskProgressViewSet)

task_router = nestedRouter.NestedSimpleRouter(router, r'tasks', lookup='task')
task_router.register(r'progresses', tasksView.TaskTaskProgressViewSet)
task_router.register(r'attachments', attachmentsView.TaskAttachmentViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    path('', include(router.urls)),
    path('', include(user_router.urls)),
    path('', include(task_router.urls)),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
