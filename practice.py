import statistics
import cowsay
from sys import argv
print(statistics.mean([20, 10]))

try:
    print("hello name: ", argv[1], sep="\n")
except:
    print("too few arguments")

if len(argv) > 1:
    print("hello name is: ", argv[1])
else:
    print("too few arguments")

for arg in argv[1:]:
    print("for loop: hello name is: ", arg)

cowsay.cow("Hello: "+ argv[1])