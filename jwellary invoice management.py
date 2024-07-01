import mysql.connector
from datetime import date
mycon1=mysql.connector.connect(host="localhost",password="1234",user="root",database="SRJewellers")
if mycon1.is_connected() == False:
    print("not connected")
cursor=mycon1.cursor()

def Monthly_Typewise_Collection():
    qr= "select monthname(trans_date),orn_type ,sum(total_amount)  from ornaments o, transactions t where o.orn_id = t.orn_id group by month(trans_date), orn_type"

    cursor.execute(qr)
    print(qr)
    dt=cursor.fetchall()
    for row in dt:
        print(row[0],row[1],row[2])
    mycon1.commit()   
    print("="*77)
    
def Monthly_Collection():
    qr="select monthname(trans_date) ,sum(total_amount)  from  transactions t  group by month(trans_date)"
    cursor.execute(qr)
    
    dt=cursor.fetchall()
    for row in dt:
        print(row[0],row[1])
    mycon1.commit()
          
    print("="*77)   
    def Report_menu():
     while True: 
             print(" "*25,"1. Monthly_Collection")
             print(" "*25,"2. Monthly_Typewise_Collection")
             print(" "*25,"0. Quit")
             print("="*77)
             ch=input(" Enter your coice (1/2/0): ")
             if ch=="1":
                 Monthly_Collection()
                
             elif ch=="2" :
                 Monthly_Typewise_Collection()
                     
             elif ch=="0" :
                 break
                
             else :
                 print(" "*25,"Please enter right choice (1/2/0) ")           
def GST_update():
        cursor.execute("select * from gst_details")
        dt=cursor.fetchall()
            
        for row in dt:
            print(row)  
        gst_id=int(input(" Enter GST id to be modified   "))
        rate=int(input("Enter GST Rate to modify "))
        qr="update gst_details set rate=%s where gst_id='%s'"%(rate,gst_id,) 
        cursor.execute(qr)
        print("Rate for ",gst_id," is modified successfully")   
        mycon1.commit()   
        print("="*77)
def Delete_Ornament():
        cursor.execute("select * from ornaments")
        dt=cursor.fetchall()
        for row in dt:
            print(row)
        orn_id=int(input("ornament id "))
        qr="delete from ornaments where orn_id=%s"%(orn_id,)
        cursor.execute(qr)
        mycon1.commit()
        print("Record for ",orn_id," is deleted successfully")
        print("="*77)
def Modify_Ornament():
        cursor.execute("select * from ornaments")
        dt=cursor.fetchall()
        for row in dt:
            print(row)
        orn_id=int(input("ornament id  "))
        qr="select * from ornaments where orn_id=%s"%(orn_id)
        cursor.execute(qr)
        dt=cursor.fetchall()
        for row in dt:
             orn_name=row[1]
             orn_type=row[2]
             orn_weight=row[3]
             orn_price=row[4]
             orn_purity=row[5]
        print(" "*25,"1. Ornament Name ")
        print(" "*25,"2. Ornament Type ")
        print(" "*25,"3. Ornament Weight ")
        print(" "*25,"4. Ornament Price ")
        print(" "*25,"5. Ornament Purity ")
        print(" "*25,"0. Quit")
        
        ch=int(input("Pls enter which field you wish to modify: "))
             
        while True : 
                      if ch==1:
                          orn_name=input("Enter Ornament Name ")
                          break
                      elif ch==2:
                           orn_type=input("Enter Ornament Type ")
                           break
                      elif ch==3:
                          orn_weight=int(input("Enter Ornament Weight "))
                          break
                      elif ch==4:
                          orn_price=int(input("Enter Ornament Price "))
                          break
                      elif ch==5:
                          orn_purity=input("Enter Ornament Purity ")
                          break
                      elif ch==0 :
                          break
                      else :
                          print(" "*25,"Please enter right choice (1/2/3/4/5/0) ")
                      
        qr="update ornaments set orn_name='%s', orn_type ='%s', orn_weight=%s,orn_price=%s,orn_purity='%s' where orn_id=%s"%(orn_name,orn_type,orn_weight,orn_price,orn_purity,orn_id)
        cursor.execute(qr)
        print("Record for ",orn_id," is modified successfully")
        mycon1.commit()
        print("="*77)
def Add_New_Ornament():
    orn_name=input("Enter ornament name")
    orn_type=input("Enter ornament type")
    orn_weight=int(input("Enter ornament weight"))
    orn_price=int(input("Enter ornament price"))
    orn_purity=input("Enter ornament purity")
    qr="insert into ornaments(orn_name,orn_type,orn_weight,orn_price,orn_purity) values ('%s','%s',%s,%s,'%s')"%(orn_name,orn_type,orn_weight,orn_price,orn_purity,)
    cursor.execute(qr)
    mycon1.commit()
    print("="*77)
def Ornaments_menu():
    while True :
        print(" "*25,"1. Add_New_Ornament")
        print(" "*25,"2. Modify_Ornament")
        print(" "*25,"3. Delete_Ornament")
        print(" "*25,"0. Quit")
        print("="*77)
        ch=input(" Enter your coice (1/2/3/0) : ")
        if ch== "1":
            
            Add_New_Ornament()
        elif ch=="2" :
             
             Modify_Ornament()
        elif ch=="3" :
             
             Delete_Ornament()
        elif ch=="0" :
            break
        else :
              print(" "*25,"Please enter right choice (1/2/3/0) ")
def Modify_Customer():
        cursor.execute("select * from customers")
        dt=cursor.fetchall()
        for row in dt:
            print(row)
        cust_id=int(input("Customer ID  "))
        qr="select * from customers where customer_id=%s"%(cust_id)
        cursor.execute(qr)
        dt=cursor.fetchall()
        for row in dt:
            cust_name=row[1]
            cust_add=row[2]
            cust_pn=row[3]
            cust_email=row[4]
        print(" "*25,"1. Customer Name ")
        print(" "*25,"2. Customer Address ")
        print(" "*25,"3. Customer Phone ")
        print(" "*25,"4. Customer EMail ")
        print(" "*25,"0. Quit")
        ch=int(input("Pls enter which field you wish to modify   "))
        
        while True : 
                      if ch==1:
                          cust_name=input("Enter Customer Name ")
                          break
                      elif ch==2:
                           cust_add=input("Enter Customer Address ")
                           break
                      elif ch==3:
                          cust_pn=input("Enter Customer Phone No ")
                          break
                      elif ch==4:
                          cust_email=input("Enter Custom Email id ")
                          break
                      elif ch==0 :
                          break
                      else :
                          print(" "*25,"Please enter right choice (1/2/3/4/0) ")
        qr="update customers set customer_name='%s', customer_address ='%s', customer_phone_no='%s',customer_email='%s' where customer_id=%s"%(cust_name,cust_add,cust_pn,cust_email,cust_id)
        cursor.execute(qr)
        mycon1.commit()
        print("="*77)
        
def Add_New_Customer():       
        cust_name=input("Enter Customer Name")
        cust_add=input("Enter Customer Address")
        cust_pn=input("Enter Customer Phone No")
        cust_email=input("Enter Custom Email id")
        qr="insert into customers (Customer_Name,Customer_Address,Customer_Phone_No,Customer_Email) values ('%s','%s','%s','%s')"%(cust_name,cust_add,cust_pn,cust_email)
        cursor.execute(qr)
        mycon1.commit()
        print("="*77)
        
def customer_menu() :
        while True : 
            print(" "*25,"1. Add_New_Customer")
            print(" "*25,"2. Modify_Customer")
            print(" "*25,"0. Quit")
            print("="*77)
            ch=input(" Enter your coice (1/2/0) : ")
            if ch== "1":
                
                Add_New_Customer()
            elif ch=="2" :
                  
                Modify_Customer()
            elif ch=="0" :
                    break
            else :
                print(" "*25,"Please enter right choice (1/2/0) ")
                
def New_order():     
    cust_id=""
    cust_name=input("Customer Name  ")
    qr="select customer_id,customer_name from customers where customer_name='%s'"%(cust_name)
    print(qr)
    cursor.execute(qr)
    dt=cursor.fetchall()
    trans_date=date.today()
    for row in dt:
        cust_id=row[0]
    print("cust id ",cust_id)
    print("trans date ",trans_date)
    qr="select distinct(orn_type) from ornaments"
    
    cursor.execute(qr)
    dt=cursor.fetchall()
    trans_date=date.today()
    for row in dt:
        print(row)
    otype=input("Enter ornament type you wish to purchase  ")
    qr="select * from ornaments where orn_type='%s'"%(otype)
    
    cursor.execute(qr)
    dt=cursor.fetchall()
    for row in dt:
        print(row)
    orn_id=input("Enter ornament id you wish to purchase  ")
    qr="select * from ornaments where orn_id='%s'"%(orn_id)
    
    cursor.execute(qr)
    dt=cursor.fetchall()
    for row in dt:
        print(row)
        gamt=int(row[4])
    qr="select Rate from gst_details where description='%s'"%(otype)
    
    cursor.execute(qr)
    dt=cursor.fetchall()
    for row in dt:
        grate=int(row[0])
    netamt=((grate/100)*gamt)+gamt
    gstamt=((grate/100)*gamt)
    print("GST Amount for this ornament is : ",gstamt)
    print("Total Net amt for thiso ornament is : ",netamt)
    qr="insert into  transactions(total_amount,orn_id,Customer_id,trans_date) values (%s,%s,%s,'%s')"%(int(netamt),orn_id,cust_id,trans_date);
    
    cursor.execute(qr)
    mycon1.commit()
    print("="*77)

def main_menu() :
                while True :
                        print("="*20,"JEWELLERY SHOP MANAGEMENT SYSTEM","="*20)
                        print(" "*25,"1. New_Order" )
                        print(" "*25,"2. Customer_Details")
                        print(" "*25,"3. Ornaments_Details")
                        print(" "*25,"4. GST_Details")
                        # print(" "*25,"5. Report")
                        print(" "*25,"0. Quit")
                        print("="*77)
                        ch=input(" Enter your coice (1/2/3/4/5/0) : ")
                        if ch== "1" :
                            New_order()
                        elif ch=="2" :
                            
                            customer_menu()
                        elif ch=="3" :
                            
                            Ornaments_menu()
                        elif ch=="4" :
                            
                            GST_update()
                        # elif ch=="5" :
                            
                        #     Report_menu()                        
                        elif ch=="0" :
                                print(" "*30," THANK YOU!!! ","                                   ")
                                break
                        else :
                                print(" "*25,"Please enter right choice (1/2/3/4/5/0) ")


main_menu()