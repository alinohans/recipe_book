class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_method = ""

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_cooking_method(self, method):
        self.cooking_method = method

    def __str__(self):
        ingredients = ", ".join(self.ingredients)
        return f"Recipe Name: {self.name}\nIngredients: {ingredients}\nCooking Method: {self.cooking_method}\n"
    
    @staticmethod
    def save_recipe(recipe):
        file_name = f"{recipe.name}.txt"
        try:
            with open(file_name, "w") as file:
                file.write(str(recipe))
            print(f"Recipe '{recipe.name}' saved to file '{file_name}'.")
        except Exception as e:
            print(f"An error occurred while saving the recipe: {e}")


if __name__ == "__main__":
    while True:
        print("\nPlease choose one of the below action:")
        print("1. Create a new recipe")
        print("2. Add ingredient to a recipe")
        print("3. Add cooking method to a recipe")
        print("4. Save recipe to file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            recipe = Recipe(name)
            print(f"Recipe '{name}' created.")

        elif choice == "2":
            ingredient = input("Enter ingredient to add: ")
            if 'recipe' in locals():
                recipe.add_ingredient(ingredient)
                print(f"Ingredient '{ingredient}' added to recipe '{recipe.name}'.")
            else:
                print("Please create a recipe first.")

        elif choice == "3":
            method = input("Enter cooking method: ")
            if 'recipe' in locals():
                recipe.add_cooking_method(method)
                print(f"Cooking method added to recipe '{recipe.name}'.")
            else:
                print("Please create a recipe first.")

        elif choice == "4":
            if 'recipe' in locals():
                recipe.save_recipe(recipe)
                del recipe 
            else:
                print("No recipe to save. Please create a recipe first.")

        elif choice == "5":
            print("Recipe Book Program Exited Sucessfully!")
            break

        else:
            print("Invalid choice. Please try again.")