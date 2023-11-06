from rest_framework import viewsets
from .serializers import UserSerlizers, AboutMeSerializrs, SkillSerializrs, SciolSerializrs, \
    ExpreienceWorkSerializrs, EducationSerializrs, ProjectSerializrs, AwardsSerializrs, \
    BoookArticleSerializrs, ContactUsSerializrs
from accounts.models import User
from home.models import AboutMeModels, SkillModel, SciolModel, ExpreienceWorkModel, \
    EducationModel, ProjectModel, AwardsModel, ContactUsModel, BoookArticleModel
from .base_permission import IsSuperUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerlizers
    permission_classes = (IsSuperUser,)


class AboutViewSet(viewsets.ModelViewSet):
    queryset = AboutMeModels.objects.all()
    serializer_class = AboutMeSerializrs
    permission_classes = (IsSuperUser,)


class SkillviewSet(viewsets.ModelViewSet):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializrs
    permission_classes = (IsSuperUser,)


class SciolviewSet(viewsets.ModelViewSet):
    queryset = SciolModel.objects.all()
    serializer_class = SciolSerializrs
    permission_classes = (IsSuperUser,)


class ExpreienceWorkviewSet(viewsets.ModelViewSet):
    queryset = ExpreienceWorkModel.objects.all()
    serializer_class = ExpreienceWorkSerializrs
    permission_classes = (IsSuperUser,)


class EducationviewSet(viewsets.ModelViewSet):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializrs
    permission_classes = (IsSuperUser,)


class ProjectviewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializrs
    permission_classes = (IsSuperUser,)


class AwardsviewSet(viewsets.ModelViewSet):
    queryset = AwardsModel.objects.all()
    serializer_class = AwardsSerializrs
    permission_classes = (IsSuperUser,)


class BoookArticleviewSet(viewsets.ModelViewSet):
    queryset = BoookArticleModel.objects.all()
    serializer_class = BoookArticleSerializrs
    permission_classes = (IsSuperUser,)


class ContactUsviewSet(viewsets.ModelViewSet):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializrs
    permission_classes = (IsSuperUser,)
