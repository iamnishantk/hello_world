print("hello world");
import random
var=random.random();
max=5;
min=3;
print(var);
var1=random.randint(min,max);
print(var1);


from boltiot import Bolt
api_key = "7aa8ddf9-d2c1-4f78-a309-6b5ab29c12fb"
device_id  = "BOLT11692813"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print (response)
