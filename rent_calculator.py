Total_rent = int(input("Tell about the total rent"))
Food_rent = int(input("Total food amount ordered for snacking"))
Electricity_spend = int(input("Total units of electricty spend is"))
extra = int(input("charge per unit"))
n = int(input("total number of members live toggether "))
Total_amount = (Total_rent) + (Food_rent )+ ((Electricity_spend) * (extra))
print(f"Total bill is {(Electricity_spend) * (extra)}")

print(f"The amount pay by a single person is :- {(Total_amount) / n}")
