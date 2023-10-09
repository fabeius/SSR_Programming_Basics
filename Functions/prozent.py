prozent = input("Bitte gib die Prozente an: ")

def visualize(percentage):
    print(f"{percentage}%: {'* ' * (percentage//10)}")

visualize(prozent)