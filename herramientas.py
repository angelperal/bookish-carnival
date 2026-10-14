
import os



def imprimir_titulo(texto):
    print("\n" + "=" * 50)
    print(f"  {texto}")
    print("=" * 50)


def imprimir_exito(texto):
    print(f"\n[OK] {texto}")


def imprimir_error(texto):
    print(f"\n[ERROR] {texto}")


def imprimir_info(texto):
    print(f"\n[INFO] {texto}")


def confirmar(texto):
    respuesta = input(f"{texto} (s/n): ").strip().lower()
    return respuesta == "s"
