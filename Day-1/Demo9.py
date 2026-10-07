'''
Write a python program:
- read an app name from <STDIN>
- test - flask -> initialize port number is 5000
- test - fastAPI -> initialize port number is 8080
- test - prometheus ->initialize port number is: 9090
|
-default app name is: web2.0 and port number 8000
|
- display app name and running port number
'''
appName = input('Enter app name: ')

if(appName == "flask"):
    port = 5000
elif(appName == "fastAPI"):
    port = 8080
elif(appName == "prometheus"):
    port = 9090
else:
    appName = "web2.0"
    port = 8000

print(f"App Name is:{appName} Running Port Number is:{port}")