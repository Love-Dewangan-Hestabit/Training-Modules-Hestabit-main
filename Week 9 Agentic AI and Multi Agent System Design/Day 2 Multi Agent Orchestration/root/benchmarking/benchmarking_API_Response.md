```
(venv) lovedewangan@hestabit-LP:~/Desktop/Training-Modules-Hestabit-main/Week 9 Agentic AI and Multi Agent System Design/Day 2 Multi Agent Orchestration/root$ python main_day2.py

Using GROQ
Endpoint: https://api.groq.com/openai/v1

Ask a question (type 'exit' to quit): Prepare a Diet Plan for me.

[PLANNER OUTPUT]

1. Determine daily calorie needs based on age, weight, height, and activity level.
2. Identify dietary restrictions and preferences, such as vegetarian, gluten-free, or dairy-free.
3. Research and select a suitable diet type, including options like low-carb, keto, or Mediterranean.
4. Plan breakfast options, including portion control and macronutrient balance.
5. Develop a list of healthy snack choices to curb hunger between meals.
6. Create a lunch and dinner meal plan, incorporating lean proteins, whole grains, and a variety of vegetables.
7. Consider including physical activity and exercise recommendations to support weight loss and overall health.
8. Schedule regular check-ins to monitor progress and make adjustments to the diet plan as needed.

[EXECUTION TREE]

Planner
- Worker 1 -> Determine daily calorie needs based on age, weight, height, and activity level.
- Worker 2 -> Identify dietary restrictions and preferences, such as vegetarian, gluten-free, or dairy-free.
- Worker 3 -> Research and select a suitable diet type, including options like low-carb, keto, or Mediterranean.
- Worker 4 -> Plan breakfast options, including portion control and macronutrient balance.
- Worker 5 -> Develop a list of healthy snack choices to curb hunger between meals.
- Worker 6 -> Create a lunch and dinner meal plan, incorporating lean proteins, whole grains, and a variety of vegetables.
- Worker 7 -> Consider including physical activity and exercise recommendations to support weight loss and overall health.
- Worker 8 -> Schedule regular check-ins to monitor progress and make adjustments to the diet plan as needed.

[WORKER OUTPUTS]

Worker 1 Output:
* Sedentary: 1,600-2,000 calories
* Lightly active: 1,800-2,200 calories
* Moderately active: 2,000-2,400 calories
* Very active: 2,200-2,800 calories
* Extremely active: 2,400-3,000 calories

Worker 2 Output:
* Vegetarian: exclude meat, fish, poultry
* Gluten-free: avoid wheat, barley, rye
* Dairy-free: exclude milk, cheese, yogurt
* Other options: vegan, keto, low-carb

Worker 3 Output:
* Low-carb for weight loss
* Keto for diabetes management
* Mediterranean for heart health

Worker 4 Output:
* Oatmeal with fruits and nuts (300 calories, 40g carbs, 10g protein)
* Scrambled eggs with whole-grain toast (250 calories, 10g carbs, 20g protein)
* Greek yogurt with berries and granola (200 calories, 30g carbs, 15g protein)

Worker 5 Output:
* Fresh fruits and nuts
* Veggie sticks with hummus
* Protein bars or energy balls
* Yogurt or cottage cheese
* Handful of trail mix

Worker 6 Output:
* Lean proteins: chicken, fish, turkey
* Whole grains: brown rice, quinoa, whole wheat
* Vegetables: leafy greens, broccoli, bell peppers
* Sample meals: grilled chicken with roasted vegetables, whole grain pasta with turkey meatballs

Worker 7 Output:
* 150 minutes/week of moderate-intensity exercise
* 75 minutes/week of vigorous-intensity exercise
* Incorporate strength training and high-intensity interval training (HIIT)

Worker 8 Output:
* Set weekly or bi-weekly check-ins
* Track weight, measurements, and progress photos
* Adjust calorie intake and meal plan as needed

[REFLECTION AGENT]

## Dietary Guidelines
* Daily calorie intake:
  + Sedentary: 1,600-2,000 calories
  + Active: 1,800-3,000 calories
* Special diets:
  + Vegetarian, gluten-free, dairy-free, vegan, keto, low-carb

## Healthy Foods
* Breakfast options:
  + Oatmeal with fruits and nuts
  + Scrambled eggs with whole-grain toast
* Snacks:
  + Fresh fruits and nuts
  + Yogurt or cottage cheese
* Proteins:
  + Lean proteins (chicken, fish, turkey)
  + Whole grains (brown rice, quinoa, whole wheat)
  + Vegetables (leafy greens, broccoli, bell peppers)

## Fitness and Tracking
* Exercise: 150 minutes/week of moderate-intensity exercise
* Progress tracking:
  + Weight, measurements, progress photos
  + Adjust calorie intake and meal plan as needed

[VALIDATOR AGENT]

Validator made No changes

[VALIDATOR OUTPUT]

## Dietary Guidelines
* Daily calorie intake:
  + Sedentary: 1,600-2,000 calories
  + Active: 1,800-3,000 calories
* Special diets:
  + Vegetarian, gluten-free, dairy-free, vegan, keto, low-carb

## Healthy Foods
* Breakfast options:
  + Oatmeal with fruits and nuts
  + Scrambled eggs with whole-grain toast
* Snacks:
  + Fresh fruits and nuts
  + Yogurt or cottage cheese
* Proteins:
  + Lean proteins (chicken, fish, turkey)
  + Whole grains (brown rice, quinoa, whole wheat)
  + Vegetables (leafy greens, broccoli, bell peppers)

## Fitness and Tracking
* Exercise: 150 minutes/week of moderate-intensity exercise
* Progress tracking:
  + Weight, measurements, progress photos
  + Adjust calorie intake and meal plan as needed

[FINAL ANSWER]

## Dietary Guidelines
* Daily calorie intake:
  + Sedentary: 1,600-2,000 calories
  + Active: 1,800-3,000 calories
* Special diets:
  + Vegetarian, gluten-free, dairy-free, vegan, keto, low-carb

## Healthy Foods
* Breakfast options:
  + Oatmeal with fruits and nuts
  + Scrambled eggs with whole-grain toast
* Snacks:
  + Fresh fruits and nuts
  + Yogurt or cottage cheese
* Proteins:
  + Lean proteins (chicken, fish, turkey)
  + Whole grains (brown rice, quinoa, whole wheat)
  + Vegetables (leafy greens, broccoli, bell peppers)

## Fitness and Tracking
* Exercise: 150 minutes/week of moderate-intensity exercise
* Progress tracking:
  + Weight, measurements, progress photos
  + Adjust calorie intake and meal plan as needed

```
