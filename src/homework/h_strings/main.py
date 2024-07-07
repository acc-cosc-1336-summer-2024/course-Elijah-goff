from strings import get_hamming_distance, get_dna_complement

def main_menu():

    while True:
        print("\nMenu")
        print("1- Hamming Distance")
        print("2- DNA Complement")
        print("3-Exit Now")

        choice = input("Enter a choice:")

        if choice == "1":
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA String: ")

            try:

              distance = get_hamming_distance(dna1, dna2)
              print("Hamming Distance: " + str(distance))

            except ValueError as e:
                print("Error: " + str(e))

        elif choice == "2":
            dna = input("Enter DNA string: ")
            complement = get_dna_complement(dna)
            print("DNA Complement: " + complement)


        elif choice == "3":
            print("Exiting Program...")   
            break 


        else:
            print("Invalid Option. Please choose option 1, 2 or 3.")


    if __name__ == "__main__":
        main_menu()





