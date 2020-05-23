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

# for i, j in zip(total[1:], total[:-1]):
#     print(i, j)

# Array to store interest earned
interest = [i-j for i, j in zip(total[1:], total[:-1])]
# print(interest)

# Plotting how interest changes overtime
plt.plot(list(range(1, 101)), interest)
plt.xlabel("Years")
plt.ylabel("Interest Earned")
plt.title("Plotting Compund Interest Earned")
plt.show()

rate = [i/j for i, j in zip(interest, total[:-1])]
print(rate)
# The sum of all interest payments plus the original principal equals the last value in the total array
print(sum(interest)+P)
print(total[-1])
