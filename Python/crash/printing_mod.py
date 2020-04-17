#we can reorganize the above code by writing 2 function

def print_models(unprinted, completed):
    """Simulate printing each design until none are left.
        move each design to completed_models after printing"""
    while unprinted:
        current = unprinted.pop()
        print("Printing: " + current)
        completed.append(current)

def show_completed(completed):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for complete in completed:
        print(completed)

    unprinted = ['iphone', 'robot', 'space']
    completed = []
    print_models(unprinted,completed)
    show_completed(completed)
