from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path("Home.html", views.Home, name="Home"),
    path("Authority-Login.html", views.AuthorityLogin, name="Authority-Login"),
    path("AuthorityLoginAction", views.AuthorityLoginAction,name="AuthorityLoginAction"),
    path("UserLogin.html", views.UserLogin, name="UserLogin"),
    path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
    path("RegistrationPage.html", views.Register, name="Register"),
    path("RegisterAction", views.RegisterAction, name="RegisterAction"),
    path("SubmitTip.html", views.SubmitTip, name="SubmitTip"),
    path("SubmitTipAction", views.SubmitTipAction, name="SubmitTipAction"),
    path("ViewTip", views.ViewTip, name="ViewTip"),
    path("TrainML", views.TrainML, name="TrainML"),
    path("ViewReports", views.ViewReports, name="ViewReports"),
    path("ViewUsers", views.ViewUsers, name="ViewUsers"),
    path("feedback", views.feedback, name="feedback"),
    path("ViewallFeedbacks",views.ViewallFeedbacks,name="ViewallFeedbacks"),
]