# prea

prea takes at least 3 coordinates, from positional arguments or stdin,
gives back the area of a polygon in m². With verbose flag: area,
vector length and total circumference

usage: prea.py [-h] [-v] [Coordinates ...]

Calculate the area of a simple polygon

positional arguments:
  Coordinates  Coordinates in Format x,y whitespace delimiter

options:
  -h, --help   show this help message and exit
  -v           Verbose Output


calculate the area of a simple polygon, with the shoelace formula
https://en.wikipedia.org/wiki/Shoelace_formula
https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Trapezformel


