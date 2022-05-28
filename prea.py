#!/usr/bin/env python3
from dataclasses import dataclass
import argparse
import sys
from math import sqrt


@dataclass
class Vecs():
    x: float
    y: float


# Polygonal Circumference
def circum(vec):
    v_len = []
    for i in range(len(vec)):
        if i == len(vec)-1:
            a = vec[i].x - vec[0].x
            b = vec[i].y - vec[0].y
        else:
            a = vec[i+1].x - vec[i].x
            b = vec[i+1].y - vec[i].y
        v_len.append(sqrt(a*a+b*b))
    return v_len


# Polygonal area with shoelace/trapezoid formula
def poly_area(vec):

    a = 0.00
    b = 0.00
    for i in range(len(vec)):
        if i == len(vec)-1:
            a += vec[i].x * vec[0].y
            b += vec[i].y * vec[0].x
            break
        else:
            a += vec[i].x * vec[i+1].y
            b += vec[i].y * vec[i+1].x
    bet = a - b
    return abs((1/2) * bet)


def verbose_output(vectors):
    a = circum(vectors)
    print("\n")
    print("Area: \t\t%.3f m²\n" % poly_area(vectors))
    for i in range(len(a)):
        print("Distance", i, "\t\t %.3f m" % a[i])

    print("Total Circumference: \t%.3f m\n" % sum(a))


def arg_parser():
    parser = argparse.ArgumentParser(
            description='calculate the area of a simple polygon')
    parser.add_argument('coordinates', metavar='Coordinates', type=str,
                        nargs='*',
                        help='Coordinates in Format x,y whitespace delimiter')
    parser.add_argument('-v', action=argparse.BooleanOptionalAction,
                        help='Verbose Output')
    args = parser.parse_args()
    return args


def main():
    args = arg_parser()

    if len(args.coordinates) != 0:
        v = args.coordinates
    else:
        k = sys.stdin.read()
        v = k.split()

    vectors = []
    for i in range(len(v)):
        sp = v[i].split(",")
        vectors.append(Vecs(x=float(sp[0]), y=float(sp[1])))
    if args.v:
        verbose_output(vectors)
    else:
        print("%.3f" % poly_area(vectors))


main()
