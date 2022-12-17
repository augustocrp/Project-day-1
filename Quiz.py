print("Seja muito bem vindo ao quiz da Biblia!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("Quem foi o primeiro Nazireu na história da biblia? \n (A) Abraão \n (B) Davi \n (C) Sansão \n (D) Samuel")
answer_1 = input("Resposta: ")

if answer_1 == "C":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print("Quem foi o homem mais velho de toda a história da biblia? \n (A) Adão \n (B) Noé \n (C) Daniel \n (D) Matuzalem")
answer_1 = input("Resposta: ")

if answer_1 == "D":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/2")