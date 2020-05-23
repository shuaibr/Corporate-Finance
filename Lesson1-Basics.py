import matplotlib.pyplot as plt

principal = 100
interest_rate = 0.05
total = principal

# print("How many years would you like to calculate?")
# n = input()
n = 5

print("If principal is 100 and interest rate is 5%, what is the value in 5 years?")
# for t in range(int(n)):
#     total = total*(1+interest_rate)
# print("total is {:.2f} in year {:d}".format(total, t+1))

# Present Value Equation
total_pv = principal * (1+interest_rate)**(int(n))

print("For loop: {:.2f} \nPV equation: {:.2f}".format(total_pv, total))


# Plotting
# Present Value function
def compundInterest(p, r, t):
    total = p*(1+r)**t
    return total


# Testing compunding interest over 100 years
timeline = list(range(101))
# print(timeline)

r = 0.05
P = 100
total = [compundInterest(P, r, i) for i in timeline]
# print(total)

plt.plot(timeline, total)
plt.xlabel("Years")
plt.ylabel("Value")
plt.title("Plotting Compund Interest")
plt.show()
