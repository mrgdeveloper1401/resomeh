from rest_framework.urls import path
from api.views.accounts import UserRegisterApiView, UserProfileApiView, UserChangePasswordApiView
from api.views import accounts


app_name = 'accounts_api'
urlpatterns = [
    path('api/logup/', UserRegisterApiView.as_view(),name='logup_api'),
    path('api/profile/<int:pk>/', UserProfileApiView.as_view(), name='profile_api'),
    path('api/profile/change_password/<int:pk>/', UserChangePasswordApiView.as_view(), name='change_password_api'),
    path('api/create-about-me/<int:pk>/', accounts.AboutMeApiView.as_view(), name='about_me_api'),
    path('api/about-me-rud/<int:pk>/', accounts.AboutMeUpdateRetieveDeleteApiView.as_view(), name='about_me_rud_api'),
    path('api/skills/<int:pk>/', accounts.SkillCreateApiView.as_view(), name='create skill'),
    path('api/skills-rup/<int:pk>', accounts.SkillUpdateRetrieveDeleteApiView.as_view(), name='skill_rup'),
    path('api/create-sciol/<int:pk>/', accounts.SciolCreateApiView.as_view(), name='create_sciol'),
    path('api/rud-sciol/<int:pk>/', accounts.SciolUpdateRetriveDeleteApiView.as_view(), name='rud_sciol'),
    path('api/create-education/<int:pk>/', accounts.EducatioCreareApiView.as_view(), name='create_education'),
    path('api/rud-education/<int:pk>/', accounts.EducatioUpdateDeleteRetiveApiView.as_view(), name='rud_education'),
    path('api/create-exprience-work/<int:pk>/', accounts.ExprienceCreateApiView.as_view(), name='exprience_work'),
    path('api/rud-exprience/<int:pk>/', accounts.ExprienceUpdateDeleteDestroyApiView.as_view(), name='rud_exprience_work'),
    path('api/create-project/<int:pk>/', accounts.ProjectCreateApiView.as_view(), name='create_project'),
    path('api/rud-project/<int:pk>/', accounts.ProjectUpdateRetriveDestroyApiView.as_view(), name='rud_project'),
    path('api/create_awards/<int:pk>/', accounts.AwardsCreateApiView.as_view(), name='create_awards'),
    path('api/rud-awards/<int:pk>/', accounts.AwardsRetrieveUpdateDestroyAPIView.as_view(), name='rud_awards'),
    path('api/create-authore/<int:pk>/', accounts.AuthoreCreateAPIView.as_view(), name='create_authore'),
    path('api/rud-authore/<int:pk>/', accounts.AuthoreRetrieveUpdateDestroyAPIView.as_view(), name='rud_authore'),
    path('api/create-book-article/<int:pk>/', accounts.BookArticleCreateApiView.as_view(), name='create-book-article'),
    path('api/rud-book-article/<int:pk>/', accounts.BookArticleRetrieveUpdateDestroyAPIView.as_view(), name='rud-book-article'),
    path('api/create-contact-us/<int:pk>/', accounts.ContactUsCreateApiview.as_view(), name='create-contact-us'),
]
