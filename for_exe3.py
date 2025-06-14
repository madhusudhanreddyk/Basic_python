for i in range(5):
    print(f'you ran {i+1} km')
    response = input("are you tried")
    if response == "yes":
        break
if i == 4:
    print("you rocked it")
else:
    print("you lost it")
