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
def compoundInterest(p, r, t):
    total = p*(1+r)**t
    return total


# Testing compounding interest over 100 years
timeline = list(range(101))
# print(timeline)

r = 0.05
P = 100
total = [compoundInterest(P, r, i) for i in timeline]
# print(total)

plt.plot(timeline, total)
plt.xlabel("Years")
plt.ylabel("Value")
plt.title("Plotting Compound Interest")
plt.show()

# for i, j in zip(total[1:], total[:-1]):
#     print(i, j)

# Array to store interest earned
interest = [i-j for i, j in zip(total[1:], total[:-1])]
# print(interest)

# Plotting how interest changes overtime
plt.plot(list(range(1, 101)), interest)
plt.xlabel("Years")
plt.ylabel("Interest Earned")
plt.title("Plotting Compound Interest Earned")
plt.show()

rate = [i/j for i, j in zip(interest, total[:-1])]
print(rate)
# The sum of all interest payments plus the original principal equals the last value in the total array
print(sum(interest)+P)
print(total[-1])

# Comparing different interest rates
r1 = 0.02
r2 = 0.05
r3 = 0.1
principal = 100
A1 = [compoundInterest(P, r1, i) for i in timeline]
A2 = [compoundInterest(P, r2, i) for i in timeline]
A3 = [compoundInterest(P, r3, i) for i in timeline]

plt.plot(timeline, A1, label="r=.02")
plt.plot(timeline, A2, label="r=.05")
plt.plot(timeline, A3, label="r=.1")
plt.xlabel("Years")
plt.ylabel("Return Total")
plt.title("Plotting Different Compound Interest Rates")
plt.legend()
plt.show()
