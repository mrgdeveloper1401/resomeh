from api.client import serializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from home.models import AboutMeModels, SkillModel, EducationModel, ExpreienceWorkModel, ContactUsModel
from home.models import ProjectModel, AwardsModel, BoookArticleModel, SciolModel, AuthoreModel
from api.client.base_permission import IsOwner


class UserRegisterApiView(CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer
    queryset = User.objects.all()


class UserChangePasswordApiView(UpdateAPIView):
    serializer_class = serializers.UserChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class AboutMeApiView(CreateAPIView):
    queryset = AboutMeModels.objects.all()
    serializer_class = serializers.AboutMeSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AboutMeUpdateRetieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = AboutMeModels.objects.all()
    serializer_class = serializers.AboutMeSerializers
    permission_classes = (IsAuthenticated,)


class SkillCreateApiView(CreateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = serializers.SkillSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkillUpdateRetrieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = serializers.SkillSerializers
    permission_classes = (IsAuthenticated,)


class SciolCreateApiView(CreateAPIView):
    queryset = SciolModel.objects.all()
    serializer_class = serializers.SciolSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SciolUpdateRetriveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = SciolModel.objects.all()
    serializer_class = serializers.SciolSerializers
    permission_classes = (IsAuthenticated,)


class EducatioCreareApiView(CreateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = serializers.EducationSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EducatioUpdateDeleteRetiveApiView(RetrieveUpdateDestroyAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = serializers.EducationSerializers
    permission_classes = (IsAuthenticated,)


class ExprienceCreateApiView(CreateAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = serializers.ExprienceWorkSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpriencRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = serializers.ExprienceWorkSerializers
    permission_classes = (IsAuthenticated,)


class ProjectCreateApiView(CreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = serializers.ProjectSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectUpdateRetriveDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = serializers.ProjectSerializers
    permission_classes = (IsAuthenticated,)


class AwardsCreateApiView(CreateAPIView):
    queryset = AwardsModel.objects.all()
    serializer_class = serializers.AwardsSerilizers
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AwardsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AwardsModel.objects.all()
    serializer_class = serializers.AwardsSerilizers
    permission_classes = (IsAuthenticated,)


class AuthoreCreateAPIView(CreateAPIView):
    queryset = AuthoreModel.objects.all()
    serializer_class = serializers.AwardsSerilizers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AuthoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AuthoreModel.objects.all()
    serializer_class = serializers.AwardsSerilizers
    permission_classes = (IsAuthenticated,)


class BookArticleCreateApiView(CreateAPIView):
    queryset = BoookArticleModel.objects.all()
    serializer_class = serializers.BookArticleSerilizers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BoookArticleModel.objects.all()
    serializer_class = serializers.BookArticleSerilizers
    permission_classes = (IsAuthenticated,)


class ContactUsCreateApiview(CreateAPIView):
    queryset = ContactUsModel.objects.all()
    serializer_class = serializers.ContactUsSerializers
    permission_classes = (IsAuthenticated,)
