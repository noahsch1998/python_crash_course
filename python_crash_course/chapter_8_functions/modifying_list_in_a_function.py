# create a function to simulate printing the designs
def print_designs(unprinted_designs, printed_models):
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing {current_design}")
        printed_models.append(current_design)


# create a function to show the models that were printed
def show_models(printed_models):
    print("\nThe following models have been completed:")
    for model in printed_models:
        print(model)

# create a list of items that need to be completed
# and a list to put them in when they are done
unprinted_designs = ['phone case', 'pendant', 'cube']
printed_models = []

print_designs(unprinted_designs, printed_models)
show_models(printed_models)