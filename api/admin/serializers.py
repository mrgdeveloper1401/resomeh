from rest_framework import serializers
from accounts.models import User
from home.models import AboutMeModels, SkillModel, SciolModel, ExpreienceWorkModel, \
    EducationModel, ProjectModel, AwardsModel, ContactUsModel, BoookArticleModel, \
        AuthoreModel
        

class UserSerlizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    
class AboutMeSerializrs(serializers.ModelSerializer):
    class Meta:
        model = AboutMeModels
        fields = '__all__'
        
        
class SkillSerializrs(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = '__all__'
        
        
class SciolSerializrs(serializers.ModelSerializer):
    class Meta:
        model = SciolModel
        fields = '__all__'
        

class ExpreienceWorkSerializrs(serializers.ModelSerializer):
    class Meta:
        model = ExpreienceWorkModel
        fields = '__all__'
        
        
class EducationSerializrs(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = '__all__'
        

class ProjectSerializrs(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'
        
        
class AwardsSerializrs(serializers.ModelSerializer):
    class Meta:
        model = AwardsModel
        fields = '__all__'
        
        
class AuthoreSerializrs(serializers.ModelSerializer):
    class Meta:
        model = AuthoreModel
        fields = '__all__'
        
    
class BoookArticleSerializrs(serializers.ModelSerializer):
    class Meta:
        model = BoookArticleModel
        fields = '__all__'
        
        
class ContactUsSerializrs(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = '__all__'