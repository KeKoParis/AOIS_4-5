import quine

lab_4 = [
    "(!x1*!x2*x3)+(!x1*x2*!x3)+(x1*!x2*!x3)+(x1*x2*x3)",
    "(!x1*x2*x3)+(x1*!x2*x3)+(x1*x2*!x3)+(x1*x2*x3)",
    "(!x1+x2+x3+x4)*(!x1+!x2+x3+x4)*(!x1+x2+!x3+x4)*(!x1+x!x2+!x3+x4)*(!x1+x2+x3+!x4)",
    "(x1+x2+x3+x4)*(!x1+!x2+x3+x4)*(x1+x2+!x3+!x4)*(!x1+x!x2+!x3+x4)*(!x1+x2+x3+!x4)",
    "(!x1+!x2+x3+x4)*(x1+x2+!x3+x4)*(!x1+x2+!x3+x4)*(x1+!x2+!x3+x4)",
    "(x1+x2+x3+x4)*(!x1+x2+!x3+x4)*(x1+!x2+x3+x4)"]
lab4_names = ["s", "p", "y1", "y2", "y3", "y4"]

lab5 = [
    "(x1*!x2*!x3*!x4)+(x1*x2*!x3*!x4)+(x1*!x2*x3*!x4)+(x1*x2*x3*!x4)+(x1*!x2*!x3*x4)+(x1*x2*!x3*x4)+(x1*!x2*x3*x4)+(x1*x2*x3*x4)",
    "(x1*x2*!x3*!x4)+(x1*x2*x3*!x4)+(x1*x2*!x3*x4)+(x1*x2*x3*x4)",
    "(x1*x2*x3*!x4)+(x1*x2*x3*x4)"]
lab5_names = ["h1", "h2", "h3"]

print("Lab4")
for i in range(len(lab4_names)):
    print(lab4_names[i])
    quine.solve(lab_4[i])

print("Lab5")
for i in range(len(lab5)):
    print(lab5_names[i])
    quine.solve(lab5[i])
