# Variable declaration
price_painting = 200
kilo_painting = 10
apprenticeship_price = 10
duration_worked_per_day = 6
learning_number = 3
number_hours = 6 
number_floor = 6
sum = 0
# The price collected per hakim to paint the building
sum = (price_painting * kilo_painting + (apprenticeship_price * duration_worked_per_day * learning_number * number_hours) ) * number_floor

# The net to win
net = 0
net = 6000 * 6 - sum

# Result
print(f"Le prix encaisse par hakim pour peindre l'immeuble {sum}")
print(f"Le net a gagner {net}")