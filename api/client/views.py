from api.client import serializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from home import  models
from api.client.base_permission import IsOwner


class UserRegisterApiView(CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer
    queryset = models.User.objects.all()


class UserChangePasswordApiView(UpdateAPIView):
    serializer_class = serializers.UserChangePasswordSerializer
    queryset = models.User.objects.all()
    permission_classes = (IsAuthenticated,)


class AboutMeApiView(CreateAPIView):
    queryset = models.AboutMeModels.objects.all()
    serializer_class = serializers.AboutMeSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AboutMeUpdateRetieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.AboutMeModels.objects.all()
    serializer_class = serializers.AboutMeSerializers
    permission_classes = (IsAuthenticated, IsOwner)


class SkillCreateApiView(CreateAPIView):
    queryset = models.SkillModel.objects.all()
    serializer_class = serializers.SkillSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkillUpdateRetrieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.SkillModel.objects.all()
    serializer_class = serializers.SkillSerializers
    permission_classes = (IsAuthenticated, IsOwner)


class SciolCreateApiView(CreateAPIView):
    queryset = models.SciolModel.objects.all()
    serializer_class = serializers.SciolSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SciolUpdateRetriveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.SciolModel.objects.all()
    serializer_class = serializers.SciolSerializers
    permission_classes = (IsAuthenticated, IsOwner)


class EducatioCreareApiView(CreateAPIView):
    queryset = models.EducationModel.objects.all()
    serializer_class = serializers.EducationSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EducatioUpdateDeleteRetiveApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.EducationModel.objects.all()
    serializer_class = serializers.EducationSerializers
    permission_classes = (IsAuthenticated, IsOwner)


class ExprienceCreateApiView(CreateAPIView):
    queryset = models.ExpreienceWorkModel
    serializer_class = serializers.ExprienceWorkSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpriencRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.ExpreienceWorkModel
    serializer_class = serializers.ExprienceWorkSerializers
    permission_classes = (IsAuthenticated, IsOwner)


class ProjectCreateApiView(CreateAPIView):
    queryset = models.ProjectModel.objects.all()
    serializer_class = serializers.ProjectSerializers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectUpdateRetriveDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.ProjectModel.objects.all()
    serializer_class = serializers.ProjectSerializers
    permission_classes = (IsAuthenticated, IsOwner)


class AwardsCreateApiView(CreateAPIView):
    queryset = models.AwardsModel.objects.all()
    serializer_class = serializers.AwardsSerilizers
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AwardsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.AwardsModel.objects.all()
    serializer_class = serializers.AwardsSerilizers
    permission_classes = (IsAuthenticated, IsOwner)


class BookArticleCreateApiView(CreateAPIView):
    queryset = models.BoookArticleModel.objects.all()
    serializer_class = serializers.BookArticleSerilizers
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.BoookArticleModel.objects.all()
    serializer_class = serializers.BookArticleSerilizers
    permission_classes = (IsAuthenticated, IsOwner)


class ContactUsCreateApiview(CreateAPIView):
    queryset = models.ContactUsModel.objects.all()
    serializer_class = serializers.ContactUsSerializers
    permission_classes = (IsAuthenticated,)
