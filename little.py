import random as ran

def main():
    score = 10
    level = get_level()
    
    for i in range(10):
        num1, num2 = generate_integer(level), generate_integer(level)
        operation = ran.choice(["+", "-"])
        ans = eval(f"{num1} {operation} {num2}")
        attempt, error = 0, 0
        while attempt != ans and error != 3:
            print(generate_string(num1, num2, operation, ans))
            try: attempt = int(input("").strip())
            except: pass
            if attempt != ans:
                print("EEE")
                error += 1
                if error == 3:
                    score -= 1
                    print(generate_string(num1, num2, operation, str(ans), True))
                    break
    print(f"Score: {score}")

def generate_string(num1, num2, operation, ans, show_answer=False):
    length = max(len(num1), len(num2))
    first_line = "\n" + " " * ((length - len(num1)) + 2) + num1
    second_line = operation + " " * ((length - len(num2)) + 1) + num2
    third_line = ((length + 2) * "-")
    string = "\n" .join([first_line, second_line, third_line])
    if show_answer:
        fourth_line = " " * (length - len(ans)+ 2) + ans
        string += "\n" + fourth_line
        return string
    return string

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]: return level
        except: continue

def generate_integer(level):
    lvl = "1000"
    if level == 1: return str(ran.randint(1, int(lvl[:level + 1]) - 1))
    else: return str(ran.randint(int(lvl[:level]), int(lvl[:level + 1]) - 1))

if __name__ == "__main__":
    main()
