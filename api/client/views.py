from api.serializer.accounts import UserRegisterSerializer,UserProfileSerializer
from api.serializer.accounts import UserChangePasswordSerializer, AboutMeSerializers, SkillSerializers
from api.serializer.accounts import SciolSerializers, EducationSerializers, ExprienceWorkSerializers
from api.serializer.accounts import ProjectSerializers, AwardsSerilizers, BookArticleSerilizers, ContactUsSerializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from accounts.models import User
from home.models import AboutMeModels, SkillModel, EducationModel, ExpreienceWorkModel, ContactUsModel
from home.models import ProjectModel, AwardsModel, BoookArticleModel, SciolModel, AuthoreModel



class UserRegisterApiView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class UserProfileApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    

class UserChangePasswordApiView(UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()
   
   
class AboutMeApiView(CreateAPIView):
    queryset = AboutMeModels.objects.all()
    serializer_class = AboutMeSerializers
    
    
class AboutMeUpdateRetieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = AboutMeModels.objects.all()
    serializer_class = AboutMeSerializers


class SkillCreateApiView(CreateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializers
    
    
class SkillUpdateRetrieveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializers
    

class SciolCreateApiView(CreateAPIView):
    queryset = SciolModel.objects.all()
    serializer_class = SciolSerializers
    

class SciolUpdateRetriveDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = SciolModel.objects.all()
    serializer_class = SciolSerializers
    

class EducatioCreareApiView(CreateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializers
    

class EducatioUpdateDeleteRetiveApiView(RetrieveUpdateDestroyAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializers
    

class ExprienceCreateApiView(CreateAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = ExprienceWorkSerializers
    

class ExpriencRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = ExprienceWorkSerializers
    

class ExprienceUpdateDeleteDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ExpreienceWorkModel
    serializer_class = ExprienceWorkSerializers
    

class ProjectCreateApiView(CreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializers
    

class ProjectUpdateRetriveDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializers
    
    
class AwardsCreateApiView(CreateAPIView):
    queryset = AwardsModel.objects.all()
    serializer_class = AwardsSerilizers
    
    
class AwardsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AwardsModel.objects.all()
    serializer_class = AwardsSerilizers
    
    
class AuthoreCreateAPIView(CreateAPIView):
    queryset = AuthoreModel.objects.all()
    serializer_class = AwardsSerilizers
    

class AuthoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AuthoreModel.objects.all()
    serializer_class = AwardsSerilizers
    
    
class BookArticleCreateApiView(CreateAPIView):
    queryset = BoookArticleModel.objects.all()
    serializer_class = BookArticleSerilizers
    

class BookArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BoookArticleModel.objects.all()
    serializer_class = BookArticleSerilizers


class ContactUsCreateApiview(CreateAPIView):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializers