print("Welcome to the love calculator!")
your_name = input("What is your name?\n")
her_name = input("What is her name?\n")
your_nameL = your_name.lower()
her_nameL = her_name.lower()
# True
count_t = your_nameL.count("t") + her_nameL.count("t")
count_r = your_nameL.count("r") + her_nameL.count("r")
count_u = your_nameL.count("u") + her_nameL.count("u")
count_e = your_nameL.count("e") + her_nameL.count("e")
Total_true = count_t + count_r + count_u + count_e
# Love
count_l = your_nameL.count("l") + her_nameL.count("l")
count_o = your_nameL.count("o") + her_nameL.count("o")
count_v = your_nameL.count("v") + her_nameL.count("v")
count_E = your_nameL.count("e") + her_nameL.count("e")
Total_love = count_l + count_o + count_v + count_E
loveScore_str = str(Total_true) + str(Total_love)
loveScore = int(loveScore_str)
if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is **{loveScore}**, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is **{loveScore}**, you are alright together.")
else:
    print(f"Your score is **{loveScore}**.")
