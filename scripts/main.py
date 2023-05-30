import subprocess
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--changeVar",nargs=2)

args=parser.parse_args()

os.system("export {0}={1}".format(args.changeVar[0], args.changeVar[1]))
os.system("echo \"export {0}={1}\" >> ~/.bashrc".format(args.changeVar[0], args.changeVar[1]))

os.system("export NEW_VAR=\"HELLO\"")
os.system("echo \"export NEW_VAR=HELLO\" >> ~/.bashrc")


print(os.environ["ENV_VALUE"])

if(args.changeVar[0] not in os.environ.keys()):  
    print("new environment variable is created")

val=subprocess.run(["conftest","verify", "--policy" ,"./policies/policy1", "--output=table"],capture_output=True,text=True)

output=val.stdout

print(output)

if(val.returncode==0):
    print("successfully runned")
else:
    print("unsuccessful")