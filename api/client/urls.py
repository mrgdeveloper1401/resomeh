from rest_framework.urls import path
from api.client.views import UserRegisterApiView, UserChangePasswordApiView
from api.client import views


app_name = 'client_api'
urlpatterns = [
    path('api/logup/', UserRegisterApiView.as_view(),name='logup_api'),
    path('api/change_password/<int:pk>/', UserChangePasswordApiView.as_view(), name='change_password_api'),
    path('api/create-about-me/', views.AboutMeApiView.as_view(), name='about_me_api'),
    path('api/about-me-rud/<int:pk>/', views.AboutMeUpdateRetieveDeleteApiView.as_view(), name='about_me_rud_api'),
    path('api/skill-create/', views.SkillCreateApiView.as_view(), name='create skill'),
    path('api/skill-rup/<int:pk>/', views.SkillUpdateRetrieveDeleteApiView.as_view(), name='skill_rup'),
    path('api/sciol-create/', views.SciolCreateApiView.as_view(), name='create_sciol'),
    path('api/sciol-rud/<int:pk>/', views.SciolUpdateRetriveDeleteApiView.as_view(), name='rud_sciol'),
    path('api/education-create/', views.EducatioCreareApiView.as_view(), name='create_education'),
    path('api/education-rud/<int:pk>/', views.EducatioUpdateDeleteRetiveApiView.as_view(), name='rud_education'),
    path('api/exprience-work-create/', views.ExprienceCreateApiView.as_view(), name='exprience_work'),
    path('api/exprience-work-rud/<int:pk>/', views.ExpriencRetrieveUpdateDestroyAPIView.as_view(), name='rud_exprience_work'),
    path('api/project-create/', views.ProjectCreateApiView.as_view(), name='create_project'),
    path('api/rud-project/<int:pk>/', views.ProjectUpdateRetriveDestroyApiView.as_view(), name='rud_project'),
    path('api/awards-create/', views.AwardsCreateApiView.as_view(), name='create_awards'),
    path('api/rud-awards/<int:pk>/', views.AwardsRetrieveUpdateDestroyAPIView.as_view(), name='rud_awards'),
    path('api/authore-create/', views.AuthoreCreateAPIView.as_view(), name='create_authore'),
    path('api/authore-rud/<int:pk>/', views.AuthoreRetrieveUpdateDestroyAPIView.as_view(), name='rud_authore'),
    path('api/book-article-create/', views.BookArticleCreateApiView.as_view(), name='create-book-article'),
    path('api/rud-book-article/<int:pk>/', views.BookArticleRetrieveUpdateDestroyAPIView.as_view(), name='rud-book-article'),
    path('api/contact-us-create/', views.ContactUsCreateApiview.as_view(), name='create-contact-us'),
]
