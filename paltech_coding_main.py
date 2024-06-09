import argparse

def load_dem(filename):
    dem_points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y, z = map(float, line.split())
            dem_points.append({'x': x, 'y': y, 'z': z})
    return dem_points

def parse_arguments():
    parser = argparse.ArgumentParser(description='Find the intersection of a ray with a DEM.')
    parser.add_argument('ox', type=float, help='Origin x-coordinate')
    parser.add_argument('oy', type=float, help='Origin y-coordinate')
    parser.add_argument('oz', type=float, help='Origin z-coordinate')
    parser.add_argument('vx', type=float, help='Direction vector x-component')
    parser.add_argument('vy', type=float, help='Direction vector y-component')
    parser.add_argument('vz', type=float, help='Direction vector z-component')
    return parser.parse_args()

def closest_intersection_point(ox, oy, oz, vx, vy, vz, dem_points):
    min_distance = float('inf')
    closest_point = None
    
    for point in dem_points:
        px, py, pz = point['x'], point['y'], point['z']
        
        # Compute the parametric t where the ray intersects the plane z = pz
        t = (pz - oz) / vz if vz != 0 else float('inf')
        
        if t < 0:
            continue
        
        ix = ox + t * vx
        iy = oy + t * vy
        iz = oz + t * vz
        
        # Check if (ix, iy) is within 1 meter of (px, py)
        if abs(ix - px) <= 1 and abs(iy - py) <= 1:
            distance = ((ix - px) ** 2 + (iy - py) ** 2 + (iz - pz) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_point = (ix, iy, iz)
    
    return closest_point

def main():
    args = parse_arguments()
    dem_points = load_dem("dem.txt")
    ox, oy, oz = args.ox, args.oy, args.oz
    vx, vy, vz = args.vx, args.vy, args.vz
    
    closest_point = closest_intersection_point(ox, oy, oz, vx, vy, vz, dem_points)
    
    if closest_point:
        output_file = "out.txt"
        with open(output_file, 'w') as f:
            f.write(f"{ox},{oy},{oz}\n")
            f.write(f"{vx},{vy},{vz}\n")
            f.write(f"{closest_point[0]},{closest_point[1]},{closest_point[2]}\n")
        print(f"Closest intersection point: x={closest_point[0]}, y={closest_point[1]}, z={closest_point[2]}")
    else:
        print("No intersection found.")

if __name__ == "__main__":
    main()
