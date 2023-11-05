from api.client.serializers import UserRegisterSerializer,UserProfileSerializer
from api.client.serializers import UserChangePasswordSerializer, AboutMeSerializers, SkillSerializers
from api.client.serializers import SciolSerializers, EducationSerializers, ExprienceWorkSerializers
from api.client.serializers import ProjectSerializers, AwardsSerilizers, BookArticleSerilizers, ContactUsSerializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from home.models import AboutMeModels, SkillModel, EducationModel, ExpreienceWorkModel, ContactUsModel
from home.models import ProjectModel, AwardsModel, BoookArticleModel, SciolModel, AuthoreModel



class UserRegisterApiView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()



class UserProfileApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    

class UserChangePasswordApiView(UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
   
   
class AboutMeApiView(CreateAPIView):
    queryset = AboutMeModels.objects.all()
    serializer_class = AboutMeSerializers
    permission_classes = (IsAuthenticated, )
    
    
class AboutMeUpdateRetieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = AboutMeModels.objects.all()
    serializer_class = AboutMeSerializers
    permission_classes = (IsAuthenticated, )


class SkillCreateApiView(CreateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializers
    permission_classes = (IsAuthenticated, )
    
class SkillUpdateRetrieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializers
    permission_classes = (IsAuthenticated, )

class SciolCreateApiView(CreateAPIView):
    queryset = SciolModel.objects.all()
    serializer_class = SciolSerializers
    permission_classes = (IsAuthenticated, )

class SciolUpdateRetriveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = SciolModel.objects.all()
    serializer_class = SciolSerializers
    permission_classes = (IsAuthenticated, )
    

class EducatioCreareApiView(CreateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializers
    permission_classes = (IsAuthenticated, )

class EducatioUpdateDeleteRetiveApiView(RetrieveUpdateDestroyAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializers
    permission_classes = (IsAuthenticated, )

class ExprienceCreateApiView(CreateAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = ExprienceWorkSerializers
    permission_classes = (IsAuthenticated, )

    

class ExpriencRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = ExprienceWorkSerializers
    permission_classes = (IsAuthenticated, )
    

class ExprienceUpdateDeleteDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = ExprienceWorkSerializers
    permission_classes = (IsAuthenticated, )
    

class ProjectCreateApiView(CreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializers
    permission_classes = (IsAuthenticated, )

class ProjectUpdateRetriveDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializers
    permission_classes = (IsAuthenticated, )
    
    
class AwardsCreateApiView(CreateAPIView):
    queryset = AwardsModel.objects.all()
    serializer_class = AwardsSerilizers
    permission_classes = (IsAuthenticated, )
    
    
class AwardsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AwardsModel.objects.all()
    serializer_class = AwardsSerilizers
    permission_classes = (IsAuthenticated, )
    
    
class AuthoreCreateAPIView(CreateAPIView):
    queryset = AuthoreModel.objects.all()
    serializer_class = AwardsSerilizers
    permission_classes = (IsAuthenticated, )
    

class AuthoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AuthoreModel.objects.all()
    serializer_class = AwardsSerilizers
    permission_classes = (IsAuthenticated, )
    
    
class BookArticleCreateApiView(CreateAPIView):
    queryset = BoookArticleModel.objects.all()
    serializer_class = BookArticleSerilizers
    permission_classes = (IsAuthenticated, )
    

class BookArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BoookArticleModel.objects.all()
    serializer_class = BookArticleSerilizers
    permission_classes = (IsAuthenticated, )


class ContactUsCreateApiview(CreateAPIView):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializers
    permission_classes = (IsAuthenticated, )