from rest_framework.urls import path
from api.client.views import UserRegisterApiView, UserChangePasswordApiView
from api.client import views


app_name = 'client_api'
urlpatterns = [
    path('api/logup/', UserRegisterApiView.as_view(),name='logup_api'),
    path('api/change_password/<int:pk>/', UserChangePasswordApiView.as_view(), name='change_password_api'),
    path('api/create-about-me/<int:pk>/', views.AboutMeApiView.as_view(), name='about_me_api'),
    path('api/about-me-rud/<int:pk>/', views.AboutMeUpdateRetieveDeleteApiView.as_view(), name='about_me_rud_api'),
    path('api/skills/<int:pk>/', views.SkillCreateApiView.as_view(), name='create skill'),
    path('api/skills-rup/<int:pk>/', views.SkillUpdateRetrieveDeleteApiView.as_view(), name='skill_rup'),
    path('api/create-sciol/<int:pk>/', views.SciolCreateApiView.as_view(), name='create_sciol'),
    path('api/rud-sciol/<int:pk>/', views.SciolUpdateRetriveDeleteApiView.as_view(), name='rud_sciol'),
    path('api/create-education/<int:pk>/', views.EducatioCreareApiView.as_view(), name='create_education'),
    path('api/rud-education/<int:pk>/', views.EducatioUpdateDeleteRetiveApiView.as_view(), name='rud_education'),
    path('api/create-exprience-work/<int:pk>/', views.ExprienceCreateApiView.as_view(), name='exprience_work'),
    path('api/rud-exprience/<int:pk>/', views.ExprienceUpdateDeleteDestroyApiView.as_view(), name='rud_exprience_work'),
    path('api/create-project/<int:pk>/', views.ProjectCreateApiView.as_view(), name='create_project'),
    path('api/rud-project/<int:pk>/', views.ProjectUpdateRetriveDestroyApiView.as_view(), name='rud_project'),
    path('api/create_awards/<int:pk>/', views.AwardsCreateApiView.as_view(), name='create_awards'),
    path('api/rud-awards/<int:pk>/', views.AwardsRetrieveUpdateDestroyAPIView.as_view(), name='rud_awards'),
    path('api/create-authore/<int:pk>/', views.AuthoreCreateAPIView.as_view(), name='create_authore'),
    path('api/rud-authore/<int:pk>/', views.AuthoreRetrieveUpdateDestroyAPIView.as_view(), name='rud_authore'),
    path('api/create-book-article/<int:pk>/', views.BookArticleCreateApiView.as_view(), name='create-book-article'),
    path('api/rud-book-article/<int:pk>/', views.BookArticleRetrieveUpdateDestroyAPIView.as_view(), name='rud-book-article'),
    path('api/create-contact-us/<int:pk>/', views.ContactUsCreateApiview.as_view(), name='create-contact-us'),
]
