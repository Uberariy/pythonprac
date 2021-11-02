"Testing script for pythonprac (2021y)"
import os
for i in os.listdir('.'):
    if str(i)[:4] == "2021":
        for j in range(1, 4):
            print("dir: "+i+", program: ", j)
            # Following two lines process execution (commend them, if u want to avoid it)
            for k in range(1, 4):
                os.system("python3 ~/pythonprac/"+i+"/"+str(j)+"/task.py < ~/pythonprac/"+i+"/"+str(j)+"/tests/"+str(k)+".in > ~/pythonprac/"+i+"/"+str(j)+"/tests/"+str(k)+".out;")
            # Following line process testing (commend it, if u want to avoid testing)
            os.system("python3 checkerNN.py ~/pythonprac/"+i+"/"+str(j)+"/task.py ~/pythonprac/"+i+"/"+str(j)+"/tests")