
from email.mime import base
from django.contrib import admin
from django.db import router
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from matrixapp import views

from .import views , HOD_Views,SuperAgent_Views

# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns



def trigger_error(request):
    division_by_zero = 1 / 0



urlpatterns = [
    
    path('admin/', admin.site.urls),
     path('admin/', admin.site.urls),
    # path('', include("Home.urls")),

    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    
    path('base1', views.BASE1, name='base1') ,

    path('pagelogin', views.pagelogin, name='login') ,
    path('pagelogin1', views.pagelogin1, name='login1') ,
    path('', views.prelogin, name='prelogin') ,

    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogin1', views.doLogin1, name='doLogin1'),
    path('Logout', views.doLogout,name="logout"),
    path('viewcars', views.viewcars,name="viewcars"),

    #profile update 

    
    path('registeruserr/', views.registeruserr,name="registeruserr"),
    path('do_superAgent_signup',views.dosuperAgent,name="do_superAgent_signup"),
    path('do_Agent_signup',views.doAgent,name="do_Agent_signup"),

    # Car Path 

    path('addbook/', HOD_Views.addbook,name="addbook"),
    path('book/view_book', HOD_Views.view_book,name="view_book"),
    path('book/availablebook', HOD_Views.availablebook,name="availablebook"),
    path('view_book/Edit<str:id>', HOD_Views.EDIT_book,name="EDIT_book"),
    path('view_book/UPDATE', HOD_Views.Updatebook,name="Updatebook"),
    path('view_book/deletebook<str:id>', HOD_Views.deletebook,name="deletebook"),
   
     
    
   
    path('HOD/approvedplote/', HOD_Views.approvedplote,name="approvedplote"),
    path('HOD/bookplot/Delete/<str:id>',HOD_Views.DELETE_PLOT,name="delete_plot"),
    path('HOD/searchbar/',HOD_Views.SEARCH_BAR,name="searchbar"),

    # Hod Panel 
    path('signup_admin/',views.signup_admin,name="signup_admin"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('HOD/Home', HOD_Views.HOME, name='admin_home'),


     ########################## define for user url ############################

    path('Agent/Home', SuperAgent_Views.Home, name='Agent_Home') ,
    path('book/view_book1', SuperAgent_Views.view_book1,name="view_book1"),
    path('book/buybook<str:id>', SuperAgent_Views.buybook,name="buybook"),
    path('book/buybook', SuperAgent_Views.buybook1,name="buybook1"),
    path('books/soldbooks', SuperAgent_Views.soldbooks,name="soldbooks"),
    path('books/booksbought', SuperAgent_Views.booksbought,name="booksbought"),


    



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
         path('__debug__/', include('debug_toolbar.urls')),

    ]+urlpatterns

# urlpatterns += staticfiles_urlpatterns()
   