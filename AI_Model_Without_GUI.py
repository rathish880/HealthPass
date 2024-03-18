from random import randint

def suggest_food(weight, height, age, gender, activity):
    protein = ['Yogurt(1 cup)', 'Cooked meat(3 Oz)', 'Cooked fish(4 Oz)', '1 whole egg + 4 egg whites', 'Tofu(5 Oz)']
    fruit = ['Berries(80 Oz)', 'Apple', 'Orange', 'Banana', 'Dried Fruits(Handful)', 'Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)', 'Whole Grain Bread(1 slice)', 'Half Large Potato(75g)', 'Oats(250g)', '2 corn tortillas']
    ps = ['Soy nuts(i Oz)', 'Low fat milk(250ml)', 'Hummus(4 Tbsp)', 'Cottage cheese (125g)', 'Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil', '2 TBSP (30g) reduced-calorie salad dressing', '1/4 medium avocado', 'Small handful of nuts', '1/2 ounce grated Parmesan cheese', '1 TBSP (20g) jam, jelly, honey, syrup, sugar']

    cal = 0

    if gender == 'Male':
        cal = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'Female':
        cal = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    if activity == 'Sedentary (little or no exercise)':
        cal *= 1.2
    elif activity == 'Lightly active (1-3 days/week)':
        cal *= 1.375
    elif activity == 'Moderately active (3-5 days/week)':
        cal *= 1.55
    elif activity == 'Very active (6-7 days/week)':
        cal *= 1.725
    elif activity == 'Super active (twice/day)':
        cal *= 1.9

    suggestions = []

    if cal < 1500:
        suggestions.append("Breakfast: " + protein[randint(0, 4)] + " + " + fruit[randint(0, 5)])
        suggestions.append("Lunch: " + protein[randint(0, 4)] + " + " + vegetable[0] + " + Leafy Greens " + grains[randint(0, 4)] + " + " + taste_en[randint(0, 5)])
        suggestions.append("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
        suggestions.append("Dinner: " + protein[randint(0, 4)] + " + 2 " + vegetable[0] + " + Leafy Greens " + grains[randint(0, 4)] + " + " + taste_en[randint(0, 5)])
        suggestions.append("Snack: " + fruit[randint(0, 5)])

    elif cal < 1800:
        suggestions.append("Breakfast: " + protein[randint(0, 4)] + " + " + fruit[randint(0, 5)])
        suggestions.append("Lunch: " + protein[randint(0, 4)] + " + " + vegetable[0] + " + Leafy Greens " + grains[randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        suggestions.append("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
        suggestions.append("Dinner: 2 " + protein[randint(0, 4)] + " + " + vegetable[0] + " + Leafy Greens " + grains[randint(0, 4)] + " + " + taste_en[randint(0, 5)])
        suggestions.append("Snack: " + fruit[randint(0, 5)])

    elif cal < 2200:
        suggestions.append("Breakfast: " + protein[randint(0, 4)] + " + " + fruit[randint(0, 5)])
        suggestions.append("Lunch: " + protein[randint(0, 4)] + " + " + vegetable[0] + " + Leafy Greens " + grains[randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        suggestions.append("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
        suggestions.append("Dinner: 2 " + protein[randint(0, 4)] + " + 2 " + vegetable[0] + " + Leafy Greens + 2 " + grains[randint(0, 4)] + " + 2 " + taste_en[randint(0, 5)])
        suggestions.append("Snack: " + fruit[randint(0, 5)])

    else:
        suggestions.append("Breakfast: 2 " + protein[randint(0, 4)] + " + " + fruit[randint(0, 5)] + " + " + grains[randint(0, 4)])
        suggestions.append("Lunch: " + protein[randint(0, 4)] + " + " + vegetable[0] + " + Leafy Greens " + grains[randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
        suggestions.append("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
        suggestions.append("Dinner: 2 " + protein[randint(0, 4)] + " + 2 " + vegetable[0] + " + Leafy Greens + 2 " + grains[randint(0, 4)] + " + 2 " + taste_en[randint(0, 5)])
        suggestions.append("Snack: " + fruit[randint(0, 5)])

    return suggestions

# Example usage:
weight = int(input("Enter your weight (in kg): "))
height = int(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ")
activity = input("Enter your activity level (Sedentary/Lightly active/Moderately active/Very active/Super active): ")


food_suggestions = suggest_food(weight, height, age, gender, activity)
for suggestion in food_suggestions:
    print(suggestion)
