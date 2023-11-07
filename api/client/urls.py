from rest_framework.urls import path
from api.client.views import UserRegisterApiView, UserChangePasswordApiView
from api.client import views


app_name = 'client'
urlpatterns = [
    path('logup/', UserRegisterApiView.as_view(),name='logup_api'),
    path('change_password/<int:pk>/', UserChangePasswordApiView.as_view(), name='change_password_api'),
    path('about-me-create/', views.AboutMeApiView.as_view(), name='about_me_api'),
    path('about-me-rud/<int:pk>/', views.AboutMeUpdateRetieveDeleteApiView.as_view(), name='about_me_rud_api'),
    path('skill-create/', views.SkillCreateApiView.as_view(), name='create skill'),
    path('skill-rup/<int:pk>/', views.SkillUpdateRetrieveDeleteApiView.as_view(), name='skill_rup'),
    path('sciol-create/', views.SciolCreateApiView.as_view(), name='create_sciol'),
    path('sciol-rud/<int:pk>/', views.SciolUpdateRetriveDeleteApiView.as_view(), name='rud_sciol'),
    path('education-create/', views.EducatioCreareApiView.as_view(), name='create_education'),
    path('education-rud/<int:pk>/', views.EducatioUpdateDeleteRetiveApiView.as_view(), name='rud_education'),
    path('exprience-work-create/', views.ExprienceCreateApiView.as_view(), name='exprience_work'),
    path('exprience-work-rud/<int:pk>/', views.ExpriencRetrieveUpdateDestroyAPIView.as_view(), name='rud_exprience_work'),
    path('project-create/', views.ProjectCreateApiView.as_view(), name='create_project'),
    path('project-rud/<int:pk>/', views.ProjectUpdateRetriveDestroyApiView.as_view(), name='rud_project'),
    path('awards-create/', views.AwardsCreateApiView.as_view(), name='create_awards'),
    path('awards-rud/<int:pk>/', views.AwardsRetrieveUpdateDestroyAPIView.as_view(), name='rud_awards'),
    path('book-article-create/', views.BookArticleCreateApiView.as_view(), name='create-book-article'),
    path('book-article-rud/<int:pk>/', views.BookArticleRetrieveUpdateDestroyAPIView.as_view(), name='rud-book-article'),
    path('contact-us-create/', views.ContactUsCreateApiview.as_view(), name='create-contact-us'),
]
