from math import sqrt
import sys


if len(sys.argv) == 1:
    print("wrong amount of arguments")
if len(sys.argv) > 1:
    

    if sys.argv[1]  in ("+","addition","-","subtract","/","divide",'sqrt','koren_kvadraten',"*","umnoji","multiply"):
        print(f"no such method as: {sys.argv[1]} ")

    if sys.argv[1] == "+" or sys.argv[1] == "addition":
        print(f"The result of the Addition {sys.argv[2]} by {sys.argv[3]} is: {(float(sys.argv[2]) + float(sys.argv[3]))} ")


    if sys.argv[1] == "-" or sys.argv[1] == "subtract":
        print(f"The result of the Subtracting {sys.argv[2]} by {sys.argv[3]} is: {(float(sys.argv[2]) - float(sys.argv[3]))} ")

    if sys.argv[1] == "/" or sys.argv[1] == "divide":
        print(f"The result of Dividing {sys.argv[2]} by {sys.argv[3]} is: {(float(sys.argv[2]) / float(sys.argv[3]))}")

    if sys.argv[1] == 'sqrt' or sys.argv[1] == 'koren_kvadraten':
        print(f"The result of Square Rooting {sys.argv[2]} is: {sqrt(float(b))}")

    if sys.argv[1] == "*" or sys.argv[1] == "umnoji" or sys.argv[1] == "multiply":
        print(f"The result of Multiplying {sys.argv[2]} by {sys.argv[3]} is: {(float(sys.argv[2]) * float(sys.argv[3]))} ")






