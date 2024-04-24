# Title: Tocar Musica
#OBSERVACAO: CODIGO PRINCIPAL NAO TA FUNCIONANDO, ANALISAR FUTURAMENTE
#MUSICA ESTA TOCANDO COM ESSE CODIGO, MAS ERA PRA SER MENOS COMPLEXO

from pygame import mixer
mixer.init()
mixer.music.load("C:/Users/klebe/Dropbox/PC/Documents/CURSOS/Python/Modulo_03_Python/ex22.mp3") 
mixer.music.set_volume(0.7)
mixer.music.play() 

import pygame


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def main():
    print("Simple Music Player")
    print("-------------------")

    while True:
        print("1. Play Music")
        print("2. Stop Music")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = r".C:/Users/klebe/Dropbox/PC/Documents/CURSOS/Python/Modulo_03_Python/ex22.mp3"
            play_music(file_path)
        elif choice == "2":
            stop_music()
        elif choice == "3":
            stop_music()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
