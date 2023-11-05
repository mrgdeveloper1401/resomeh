from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from . import views


router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"aboutme", views.AboutViewSet, basename="aboutme")
router.register(r"skill", views.SkillviewSet, basename="skill")
router.register(r"scicol", views.SciolviewSet, basename="scicol")
router.register(r"expreiencework", views.ExpreienceWorkviewSet, basename="expreiencework")
router.register(r"education", views.EducationviewSet, basename="education")
router.register(r"project", views.ProjectviewSet, basename="project")
router.register(r"awards", views.AwardsviewSet, basename="awards")
router.register(r"authore", views.AuthoreviewSet, basename="authore")
router.register(r"boookarticle", views.BoookArticleviewSet, basename="boookarticle")
router.register(r"contactus", views.ContactUsviewSet, basename="contactus")


app_name = 'admin_api'
urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns + router.urls