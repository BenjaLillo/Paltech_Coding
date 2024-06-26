# Paltech Interview Test - Coding Challenge [Solution Proposal]
The goal of this repository is to keep all my progress on the solution well documented.

The selected programming language is Python, and the code aims to output the (x,y,z) coordinates of the closest intersection point between a 1km x 1km surface defined in `dem.txt`, and a ray traced by the input parameters (x,y,z,vx,vy,vz).

The coordinates are in the ETRS89 coordinate reference system (EPSG 25832).

## Running the code
As this code avoids against system-wide libraries, there is no need to install extra libraries for the main propose. Given that, the program runs with:
```
python paltech_coding_main.py [x] [y] [z] [vx] [vy] [vz]
```

Where:
- [x], [y] and [z] should be replaced by the coordinates of the origin point of the ray.
- [vx] [vy] [vz] should be replaced by the direction vector of a 3D ray.

The output may be whether indicating there is no intersection, or:

```
> Closest intersection point: x=[x coord.], y=[y coord.], z=[z coord.]
```

The program also writes a .txt file `out.txt` with: 1) Origin coordinates of the ray, 2) Direction vectors of the ray, and 3) Coordinates of the intersection point.

### Examples
Some examples are shown below: 

- **Example #1**

Input:
```
python paltech_coding_main.py 599434.50 5287590.50 800 0.1 -0.3 -0.2
```

Output:
```
> Closest intersection point: x=599486.11, y=5287435.67, z=696.78
```

- **Example #2**

Input:
```
python paltech_coding_main.py 599303.00 5287825.00 900 2 5 -0.15
```

Output:
```
> No intersection found.
```


- **Example #3**

Input:
```
python paltech_coding_main.py 599303.00 5287825.00 900 0.3 -0.1 -0.15
```

Output:
```
> Closest intersection point: x=599699.58, y=5287692.806666667, z=701.71
```



## EXTRA: Plots!
The file `plots.py` uses `matplotlib` library, which must be firstly installed:


```
pip install matplotlib
```

Then, running `plots.py` with ```python plots.py``` will use the information of the previoulsy executed main program in order to make a plot of the terrain, the ray and the intersection point. An example is shown below.
![3D Plot example](img/plotExample.jpg)