from rest_framework import serializers
from accounts.models import User
from home.models import AboutMeModels, SkillModel, SciolModel, EducationModel, ExpreienceWorkModel
from home.models import ProjectModel, AwardsModel, BoookArticleModel, AuthoreModel, ContactUsModel
from django_jalali.serializers.serializerfield import JDateField, JDateTimeField

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'id')
        
        extra_kwargs = {
            'password': {"write_only": True},
            'id': {'read_only': True}
        }


class UserProfileSerializer(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = User
        fields = (
            'full_name',
            'email',
            'mobile_phone',
            'created_at',
            'last_login',
            'id'
        )


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = (
            'password',
            'new_password',
            'new_password_confirm'
        )

    def update(self, instance, validated_data):
        if instance.check_password(validated_data['password']):
            instance.set_password(validated_data['new_password'])
        else:
            raise serializers.ValidationError({'password': 'old password is wrong'})
        return instance
    

class AboutMeSerializers(serializers.ModelSerializer):
    birth_day = JDateField()
    class Meta:
        model = AboutMeModels
        fields = (
            'id',
            'user',
            'image',
            'explain',
            'job',
            'marital_status',
            'created_at',
            'gender_choose',
            'address',
            'birth_day',
        )


class SkillSerializers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = SkillModel
        fields = (
            'id',
            'user',
            'skill_name',
            'created_at',
        )
        

class SciolSerializers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = SciolModel
        fields = (
            'id',
            'user',
            'sciol_name',
            'sciol_url',
            'created_at',
        )
        
        
class ExprienceWorkSerializers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = ExpreienceWorkModel
        fields = (
            'id',
            'user',
            'job_title',
            'organization_name',
            'explain_your_duties',
            'link_company',
            'at_date_exprence',
            'to_date_exprence',
            'status_work',
            'created_at',
        )
        

class EducationSerializers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = EducationModel
        fields = '__all__'
        

class ProjectSerializers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = ProjectModel
        fields = (
            'id',
            'user',
            'title',
            'explain_project',
            'project_url',
            'image',
            'from_date',
            'up_to_date',
            'status_project',
            
        )
        

class AwardsSerilizers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = AwardsModel
        fields = '__all__'


class AuthoreSerilizers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = AuthoreModel
        
    
class BookArticleSerilizers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = BoookArticleModel
        fields = '__all__'
        
    
class ContactUsSerializers(serializers.ModelSerializer):
    created_at = JDateTimeField()
    class Meta:
        model = ContactUsModel
        fields = '__all__'