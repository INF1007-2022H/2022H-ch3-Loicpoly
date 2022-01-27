#  !/usr/bin/env python
#  -*- coding: utf-8 -*-
import math


def square_root(a: float) -> float:
    sqr = pow(a, 0.5)
    return sqr


def square(a: float) -> float:
    sqrt = pow(a, 2)
    return sqrt


def average(a: float, b: float, c: float) -> float:
    avera = (a + b + c) / 3
    return avera


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    deg = angle_degs + angle_mins / 60 + angle_secs / 3600
    rad = math.radians(deg)
    return rad


def to_degrees(angle_rads: float) -> tuple:
    deg = 180 * angle_rads / math.pi
    angle_degre = int(deg)
    interim = deg - angle_degre
    minu = int(interim * 60)
    second = int(interim * 60 - minu)
    return (angle_degre, minu, second)


def to_celsius(temperature: float) -> float:
    celc = (temperature - 32) / 1.8
    return celc


def to_farenheit(temperature: float) -> float:
    far = temperature * 1.8 + 32
    return far


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    #  Dans l'énoncé c'était 100 et je l'ai modifié pour 180 pour être en accord avec la valeur dans l'énoncé
    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
