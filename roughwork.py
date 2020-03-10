while True:
    print("Enter the correct answer.")
    print("What is your age?")
    ans=input()

    try:
        ans=int(ans)

    except:
        print("Only integers please.")
        continue

    if ans < 4:
            print(f"You can't be {ans} years old mate.")
            continue

    if ans >= 65:
            print(f"{ans} years old? You're overrage mate.")
            continue

    else:
        print(f"Your age is {ans}")
        break
    