DULJINA_BROJA_KARTICE = 16 # duljina PAN broja

provjera_duljine_kartice = False
global_loop = True


def konvert_broja_kartice(pan_raw):
    try:
        pan_clear = int(pan_raw.replace("-", ""))
    except ValueError:
        print(f"{pan_raw} je neispravan format kartice. Osim broja, dozvoljen je i '-' znak Molim unesite ponovno\n")
        return False
    else:
        if provjera_duljine_kartice and len(str(pan_clear)) != DULJINA_BROJA_KARTICE:
            print("Neispravna duljina broja kartice. Molim unesite ponovno\n")
            return False
        else:
            global char_za_zastitu
            zasticen_broj = ""

            # sakrij sve brojeve 
            for char in pan_raw:
                if char.isdigit():
                    zasticen_broj = zasticen_broj + char_za_zastitu
                else:
                    zasticen_broj = zasticen_broj + char

            # prikazi zadnja 4 chara
            zasticen_broj = zasticen_broj[:-4] + pan_raw[-4:]
            print(f"Ovo je krajnji rez: {zasticen_broj}")
            return zasticen_broj
        

char_za_zastitu = input("Unesi znak s kojim zelis zastiti broj, default:'#' ") or "#"

while len(char_za_zastitu) > 1:
    char_za_zastitu = input("Maksimalna duljina je 1, lupi enter za default ") or "#"

while global_loop:
    pan_raw = input("Unesi broj kartice: ")

    if konvert_broja_kartice(pan_raw):
        global_loop = False

print("\nKraj koda.")

