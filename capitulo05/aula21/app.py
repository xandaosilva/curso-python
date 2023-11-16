import enum

class Directions(enum.Enum):
    ESQUERDA = "esquerda"
    DIREITA = "direita"
    ACIMA = "acima"
    ABAIXO = "abaixo"


def to_move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError("Direção não encontrada")
    print(f"Movendo para {direction.name} - {direction.value}")


to_move(Directions.DIREITA)
to_move(Directions.ACIMA)
to_move(Directions.ABAIXO)
to_move(Directions.ESQUERDA)
