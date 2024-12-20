from luo_peli import luo_peli

def main():
    while True:
        print(
            "Valitse pelataanko\n"
            " (a) Ihmistä vastaan\n"
            " (b) Tekoälyä vastaan\n"
            " (c) Parannettua tekoälyä vastaan\n"
            "Muilla valinnoilla lopetetaan"
        )

        peli = luo_peli(valittu=input())
        if peli is not None:
            peli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
