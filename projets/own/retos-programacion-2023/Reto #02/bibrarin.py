'''
 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien gane cada punto del juego.
 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
   15 - Love
   30 - Love
   30 - 15
   30 - 30
   40 - 30
   Deuce
   Ventaja P1
   Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.   
 - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''


def RolangGarros(puntos):
    lista_puntos = {0:'0', 1:'15', 2:'30', 3:'40'}
    contador_P1 = 0
    contador_P2 = 0
    winner = ''

    for punto in puntos:
        if (punto == 'P1'):
            contador_P1 += 1
        elif (punto == 'P2'):
            contador_P2 += 1
        else:
            print('Error en la inserción de datos')

        if (contador_P1 <= 3 and contador_P2 < 3 ) or (contador_P1 < 3 and contador_P2 <= 3 ):
            print(f"{lista_puntos[contador_P1]} - {lista_puntos[contador_P2]}")
        elif (contador_P1 == contador_P2):
            print('Deuce')
        elif (contador_P1 - contador_P2 == 1):
            print('Ventaja P1')
        elif (contador_P1 - contador_P2 == -1):
            print('Ventaja P2')
        else:
            if (contador_P1 > contador_P2):
                winner = 'Ganador es el jugador 1'
            else:
                winner = 'Ganador es el jugador 2'
    if winner == ''
        return 'Quedan puntos por disputar'
    else:
        return winner

def main():
    puntos = ('P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P1')
    print(RolangGarros(puntos))

if __name__ == "__main__":
    main() 