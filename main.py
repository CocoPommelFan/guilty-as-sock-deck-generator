import glob
import json
import os
from pathlib import Path

path = "decks\\"

def main():
    start()

def console_clear():
    os.system('cls||clear')
    
def default_data(_name):
    default_data = {
        "deckName": _name[6:],
        "isValid": True,
        "proofs": []
    }
    return default_data

def start():
    while True:
        print(f"1) Новая колода\n2) Добавить карты в существующую колоду\n0) Выход")
        match input():
            case "1":
                console_clear()
                deck_name = deckCreate()
                if deck_name == True:
                    continue
                console_clear()
                cycle(deck_name)
                return
            case "2":
                deck_name = checkExistsDecks()
                if deck_name == True:
                    continue
                console_clear()
                cycle(deck_name)
            case "0":
                return
            case _:
                return
        

def checkExistsDecks():
    console_clear()
    while True:
        decks = glob.glob("decks/*.txt", recursive=True)
        print("Выберите колоду")
        if not decks:
            console_clear()
            print("У вас нет колод")
            return True
        for i, deck in enumerate(decks):
            print(f"{i + 1}) {Path(deck[6:]).with_suffix('')}")
        try:
            deck_index = int(input())
            console_clear()
            if deck_index < 1 or deck_index > len(decks): 
                print("Несуществующая колода")
                continue
            else:
                return Path(decks[deck_index - 1][6:]).with_suffix('')
        except Exception as e:
            print("Несуществующая колода")
        

def deckCreate():
    print("Название колоды:")
    name = input()
    if os.path.exists(f"{name}.txt"):
        print(f"Колода уже существует")
        return True
    else:
        newFile(name)
        print(f"Колода {name}.json создана")
        return name


def newFile(_name): 
    Path("decks").mkdir(parents=True, exist_ok=True)
    with open(f"{path}{_name}.json", "w", encoding="utf-8") as file:
        json.dump(default_data(f"{path}{_name}"), file, ensure_ascii=False, indent=4)
    return
     

def addToFile(_, _name):
    Path("decks").mkdir(parents=True, exist_ok=True)
    with open(f"{path}{_name}.json", "w", encoding="utf-8") as file:
        json.dump(_, file, ensure_ascii=False, indent=4)
    toTxt(_name)
    print(f"Файл {_name} был создан")
    return

def toTxt(_):
    if os.path.exists(f"{path}{_}.txt"):
        os.remove(f"{path}{_}.txt")
    
    os.rename(f"{path}{_}.json", f"{path}{_}.txt")


def toJson(_):
    os.rename(f"{path}{_}.txt", f"{path}{_}.json")
    
    
def ifExit(x, deck_data, deck_name):
    if x.lower() == "выход":
        addToFile(deck_data, deck_name)
        console_clear()
        return True
    return False


def question(deck_data, deck_name):
    print("Введите заголовок:")
    h = input()
    if ifExit(h, deck_data, deck_name):
        return (True, True)
    print("Введите Описание:")
    d = input()
    if ifExit(d, deck_data, deck_name):
        return (True, True)
    
    console_clear()
    return (h, d)

   
def cycle(deck_name):
    if os.path.exists(f"{path}{deck_name}.txt"):
        toJson(deck_name)
    with open(f"{path}{deck_name}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    while True:        
        h, d = question(data, deck_name)
                
        if True in (h, d):
            return
        
        data["proofs"].append({
            "content": f"{h}",
            "tagline": f"{d}",
            "cardType": 3
        })


if __name__ == "__main__":
    main()




