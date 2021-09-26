
from django.conf.urls import url
from first import views

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'), 
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^course/$', views.CoursePageView.as_view(), name='course'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^thankyou/$', views.ThankyouPageView.as_view(), name='thankyou'),
    url(r'^placementform/$', views.placementform, name='placementform'),
    url(r'^algorithform/$', views.algorithmform, name='algorithmform'),
    url(r'^languageform/$', views.languageform, name='languageform'),
    url(r'^developmentform/$', views.developmentform, name='developmentform'),
    url(r'^enquiryform/$', views.enquiryform, name='enquiryform'),
]
