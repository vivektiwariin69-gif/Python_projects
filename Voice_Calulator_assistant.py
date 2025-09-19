import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_voice_input(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(prompt)
        print(prompt)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please try again.")
        print("Sorry, I did not understand. Please try again.")
        return get_voice_input(prompt)
    except sr.RequestError:
        speak("Sorry, there was an error with the speech recognition service.")
        print("Sorry, there was an error with the speech recognition service.")
        return None

def python_user(name):
    print(f"Hello {name}, welcome to the Python programming world!")

def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
    return a + b

def subtract(a, b):
    print(f"The difference of {a} and {b} is {a - b}")
    return a - b

def multiply(a, b):
    print(f"The product of {a} and {b} is {a * b}")
    return a * b

def divide(a, b):
    if b != 0:
        print(f"The division of {a} and {b} is {a / b}")
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None

def modulus(a, b):
    if b != 0:
        print(f"The modulus of {a} and {b} is {a % b}")
        return a % b
    else:
        print("Error: Modulus by zero is not allowed.")
        return None

def exponent(a, b):
    print(f"The exponent of {a} and {b} is {a ** b}")
    return a ** b

def floor_divide(a, b):
    if b != 0:
        print(f"The floor division of {a} and {b} is {a // b}")
        return a // b
    else:
        print("Error: Floor division by zero is not allowed.")
        return None

def python_assistant():
    speak("Welcome to your python assistant!")
    print("Welcome to your python assistant!")
    name = get_voice_input("Enter your name:")
    python_user(name)

    while True:
        menu = ("Choose an operation: 1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Modulus, 6. Exponent, 7. Floor Divide, 8. Exit")
        speak(menu)
        print("\n" + menu.replace(",", "\n"))
        choice = get_voice_input("Enter choice (1-8):")

        if choice in ['1', '2', '3', '4', '5', '6', '7'] or choice.lower() in ['add','subtract','multiply','divide','modulus','exponent','floor divide']:
            try:
                num1 = get_voice_input("Enter first number:")
                num1 = float(num1)
                num2 = get_voice_input("Enter second number:")
                num2 = float(num2)
            except ValueError:
                speak("Invalid input! Please enter numeric values.")
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1' or choice.lower() == 'add':
                result = add(num1, num2)
                speak(f"The result is {result}")
            elif choice == '2' or choice.lower() == 'subtract':
                result = subtract(num1, num2)
                speak(f"The result is {result}")
            elif choice == '3' or choice.lower() == 'multiply':
                result = multiply(num1, num2)
                speak(f"The result is {result}")
            elif choice == '4' or choice.lower() == 'divide':
                result = divide(num1, num2)
                if result is not None:
                    speak(f"The result is {result}")
            elif choice == '5' or choice.lower() == 'modulus':
                result = modulus(num1, num2)
                if result is not None:
                    speak(f"The result is {result}")
            elif choice == '6' or choice.lower() == 'exponent':
                result = exponent(num1, num2)
                speak(f"The result is {result}")
            elif choice == '7' or choice.lower() == 'floor divide':
                result = floor_divide(num1, num2)
                if result is not None:
                    speak(f"The result is {result}")
        elif choice == '8' or choice.lower() == 'exit':
            speak("Exiting the program. Goodbye!")
            print("Exiting the program. Goodbye!")
            break
        else:
            speak("Invalid choice! Please select a valid operation.")
            print("Invalid choice! Please select a valid operation.")

python_assistant()
