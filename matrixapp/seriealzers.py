
from rest_framework import serializers
from matrixapp.models import HOD, AddPlot, BookPlot, CustomUser, Customer, Kyc,SuperAgent,Installment


class CustomerSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
  

class AddPlotSerliazer(serializers.ModelSerializer):
    class Meta:
        model = AddPlot
        fields = "__all__"
  


    # id = serializers.IntegerField()
    # plot_no = serializers.CharField(max_length=100)
    # plc_rate = serializers.IntegerField()
    # plc = serializers.IntegerField()
    # plot_rate = serializers.IntegerField()
    # discount = serializers.IntegerField()




class BookPlotSerliazer(serializers.ModelSerializer):
    class Meta:
        model = BookPlot
        fields = "__all__"
    
    # ref_id = serializers.CharField(max_length=25)
    # # user_code = str(uuid.uuid4()).replace("-", "")[:4]
    # user_id = serializers.CharField(max_length=300)
    # # user_id=models.CharField(primary_key=True,max_length=50, default=user_code, editable=False)
    # plot_number = serializers.CharField(max_length=25)
    # Payable_amout = serializers.IntegerField()
    # Mnthly_Installment = serializers.IntegerField()
    # number_of_Installment = serializers.IntegerField()
    # name = serializers.CharField(max_length=100)
    # father_name = serializers.CharField(max_length=100)
    # mobile_no = serializers.IntegerField()
    # payment_mode = serializers.CharField(max_length=10)
    # remarks = serializers.CharField()
    # # receipt = serializers.ImageField(upload_to = 'receipt/')
    # joinig_date=serializers.DateField()


class KycSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Kyc
        fields = "__all__"
    # cust_id = serializers.CharField(max_length=300)
    # # user_id=models.CharField(primary_key=True,max_length=50, default=user_code, editable=False)
    # accountname = serializers.CharField(max_length=25)
    # accountno = serializers.IntegerField()
    # IFSCno = serializers.CharField(max_length=300)
    # Pancardno = serializers.CharField(max_length=300)

  

# class HODSerliazer(serializers.ModelSerializer):
#     class Meta:
#         model = HOD
#         fields = ['username']
       

       

class CustomUserSerliazer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name', 'username','password', 'email','rank','user_type','user_id']
        
 
 
class SuperAgentSerliazer(serializers.ModelSerializer):
    class Meta:
        model = SuperAgent
        fields = ['reference_id','created_at','updated_at','admin_id']   
        depth = 1    
        
   

class InstallmentSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = "__all__"   



class LoginSerliazer(serializers.Serializer):
    email = serializers.EmailField
    password = serializers.CharField
    class Meta:
       
        fields = ('email','password')  
        

