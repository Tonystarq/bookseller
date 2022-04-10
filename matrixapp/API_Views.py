import email
from hashlib import new
from typing import Generic


from matrixapp import seriealzers
from matrixapp.EmailBackEnd import EmailBackEnd
from matrixapp.seriealzers import AddPlotSerliazer,CustomerSerliazer,BookPlotSerliazer,KycSerliazer,CustomUserSerliazer,SuperAgentSerliazer,InstallmentSerliazer,LoginSerliazer#,HODSerliazer
from rest_framework.viewsets import ViewSet,ModelViewSet
from .models import HOD, Customer,AddPlot,BookPlot, Installment,Kyc,SuperAgent,CustomUser
from rest_framework.response import Response
from rest_framework import viewsets,response
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import GenericAPIView,CreateAPIView
from rest_framework.authentication import BasicAuthentication


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()     
    serializer_class  = CustomerSerliazer
     

class PlotViewSet(ModelViewSet):
    queryset = AddPlot.objects.all()     
    serializer_class  = AddPlotSerliazer
     

class BookPlotViewSet(ModelViewSet):
    queryset = BookPlot.objects.all()     
    serializer_class  = BookPlotSerliazer
     

class KYCViewSet(ModelViewSet):
    queryset = Kyc.objects.all()     
    serializer_class  = KycSerliazer
     

class InstallmentViewSet(ModelViewSet):
    queryset = Installment.objects.all()     
    serializer_class  = InstallmentSerliazer


# class CustomUserViewSet(viewsets.ModelViewSet):
#     serializer_class = SuperAgentSerliazer

#     def get_queryset(self):
#         posts = Posts.objects.all()
#         return posts
    
#     def create(self,request,*args, **kwargs):
#         post_data = request.data

#         new_rate = PostsRates.objects.create(likes=post_data["rates"]["likes"],dislikes=post_data["rates"]["dislikes"])
#         new_rate.save()

#         new_post = Posts.objects.create(post_title=post_data["post_title"],post_body=post_data["post_body"],rates=new_rate)
#         new_post.save()
#         serializer = PostsSerializer(new_post)
#         return Response(serializer.data)


# class HODViewSet(ModelViewSet):
#     queryset = HOD.objects.all()     
#     serializer_class  = HODSerliazer
     

class CustomUserViewSet(ModelViewSet):
    # queryset = CustomUser.objects.all()     
    # serializer_class  = CustomUserSerliazer
    serializer_class = CustomUserSerliazer
    def get_queryset(self):
        posts = CustomUser.objects.all()
        return posts
     
    def create(self,request,*args, **kwargs):
        post_data = request.data
        

        new_rate = CustomUser(first_name=post_data["first_name"],last_name=post_data["last_name"],username=post_data["username"],email=post_data["email"],user_type=2,rank=post_data["rank"])
        # new_rate = CustomUser.objects.create(user_type=post_data["admin"]["user_type"],profile_pic=post_data["admin"]["profile_pic"],user_id=post_data["admin"]["user_id"],rank=post_data["admin"]["rank"])
        
        
        new_rate.save()
        new_rate.set_password(post_data['password'])
        new_rate.save()

        new_post = SuperAgent(reference_id=post_data["reference_id"],admin=new_rate)
        new_post.save()
        serializer = SuperAgentSerliazer(new_post)
        return Response(serializer.data)


class AgentViewSet(viewsets.ModelViewSet):
    serializer_class = SuperAgentSerliazer


    def get_queryset(self):
        rates = SuperAgent.objects.all()
        return rates   

class LoginViewSet(CreateAPIView):
    authentication_classes = [BasicAuthentication]
    serializer_class = LoginSerliazer
    def post(self,request,*args, **kwargs):
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # print(email)
        user=EmailBackEnd.authenticate(request, username=request.POST.get('email'), password = request.POST.get('password'))
        # print(request.POST.get('password'))
        # if user:
        #     # seriealzer = self.serializer_class(user)
        #     return response.Response({"message":'login successful'})
        
        # return response.Response({"message":'error'})

        
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return response.Response({"message":'user_type:1'})
            elif user_type == '2':
                return response.Response({"message":'user_type:2'})
        else:
            return response.Response({"message":'Invalid Login Or Password!!'})
            # messages.error(request,"Invalid Login Or Password!!")
                
                # return redirect('Agent_Home')
                # return redirect('admin_home')


   

    
# class AgentViewSet(ModelViewSet):
#     queryset = SuperAgent.objects.all()
#     serializer_class  = SuperAgentSerliazer   

    

# class AgentViewSet(ModelViewSet):
#     serializer_class = SuperAgentSerliazer
#     def get_queryset(self):
#         posts = SuperAgent.objects.all()
#         return posts
     
#     def create(self,request,*args, **kwargs):
#         post_data = request.data

#         new_rate = CustomUser.objects.create(user_type=post_data["admin"]["user_type"],profile_pic=post_data["admin"]["profile_pic"],user_id=post_data["admin"]["user_id"],rank=post_data["admin"]["rank"])
#         new_rate.save()

#         new_post = SuperAgent.objects.create(reference_id=post_data["reference_id"],first_name=post_data["first_name"],created_at=post_data["created_at"],updated_at=post_data["updated_at"],admin=new_rate)
#         new_post.save()
#         serializer = SuperAgentSerliazer(new_post)
#         return Response(serializer.data)

     