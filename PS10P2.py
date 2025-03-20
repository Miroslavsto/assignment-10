def compute_square_footage(length, width, height):
    square_footage = (2 * length * width) + (2 * length * height) + (2 * width * height)
    return square_footage

def compute_gallons_needed(square_footage):
    return square_footage / 50

while True:
    repeat = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if repeat != 'yes':
        break
    
    length = float(input("Enter the length of the room: "))
    width = float(input("Enter the width of the room: "))
    height = float(input("Enter the height of the room: "))
    
    square_footage = compute_square_footage(length, width, height)
    gallons_needed = compute_gallons_needed(square_footage)
    
    print(f"Square footage of the room: {square_footage:.2f} square feet")
    print(f"Number of gallons needed to paint the room: {gallons_needed:.2f}\n")

print("Program ended.")