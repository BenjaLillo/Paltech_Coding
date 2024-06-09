import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_dem(filename):
    dem_points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, z = map(float, line.split())
            dem_points.append({'x': x, 'y': y, 'z': z})
    return dem_points

def plot_dem(ax, dem_file, resolution_factor):
    dem_points = []
    with open(dem_file, 'r') as file:
        for i, line in enumerate(file):
            if i % resolution_factor == 0:
                x, y, z = map(float, line.split())
                dem_points.append({'x': x, 'y': y, 'z': z})
    
    x_vals = [point['x'] for point in dem_points]
    y_vals = [point['y'] for point in dem_points]
    z_vals = [point['z'] for point in dem_points]
    
    ax.plot_trisurf(x_vals, y_vals, z_vals, cmap='terrain')

def plot_ray_and_intersection(ax, ray_file):
    with open(ray_file, 'r') as file:
        lines = file.readlines()
        ox, oy, oz = map(float, lines[0].split(','))
        vx, vy, vz = map(float, lines[1].split(','))
        ix, iy, iz = map(float, lines[2].split(','))

    z_cutoff = 650
    t = (z_cutoff - oz) / vz  # Calculate the parameter where z equals the cutoff value
    ox_cutoff = ox + t * vx
    oy_cutoff = oy + t * vy
    oz_cutoff = z_cutoff  # Set the z-component to the cutoff value
    
    # Plot the ray with z-components below the cutoff value set to NaN
    ax.plot([ox, ox_cutoff], [oy, oy_cutoff], [oz, oz_cutoff], color='r', label='Ray')
    ax.scatter(ix, iy, iz, color='b', label='Intersection Point')

def main():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot DEM terrain with lower resolution
    plot_dem(ax, 'dem.txt', resolution_factor=50)
    
    # Plot ray and intersection point
    plot_ray_and_intersection(ax, 'out.txt')
    
    ax.set_title('Terrain, Ray, and Intersection Point')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    
    plt.show()

if __name__ == "__main__":
    main()
