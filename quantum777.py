# QUANTUM777 SHELL v1.0 - OLVERA x BlackPanter4
# Shell de alto nivel para gestión de talleres

import os, datetime

BANNER = """
 ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗████████╗██╗   ██╗███╗   ███╗ 777
██╔═══██╗██║   ██║██╔══██╗████╗  ██║╚══██╔══╝██║   ██║████╗ ████║
██║   ██║██║   ██║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
  [OLVERA motors - Secure Shell]
"""

comandos = {
    "help": "Muestra comandos",
    "olvera": "Entra al sistema OLVERA motors",
    "bateria": "Cotiza batería $550 domicilio",
    "clear": "Limpia pantalla",
    "exit": "Salir"
}

def shell():
    print(BANNER)
    print(f"Quantum777 iniciado: {datetime.datetime.now()}")
    while True:
        try:
            cmd = input("quantum777@olvera:~$ ").lower().strip()
            if cmd == "help":
                for k,v in comandos.items():
                    print(f"  {k:10} -> {v}")
            elif cmd == "olvera":
                print(">> Conectando a OLVERA motors... Bocho Dorado Activo")
            elif cmd == "bateria":
                print(">> BATERÍA ITALIKA MF-FA ICB6L-B | $550 a domicilio | 12V 6.5Ah")
            elif cmd == "clear":
                os.system('cls' if os.name=='nt' else 'clear')
                print(BANNER)
            elif cmd == "exit":
                print("Cerrando Quantum777...")
                break
            elif cmd == "":
                continue
            else:
                print(f"Comando no encontrado: {cmd} - escribe help")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    shell()
