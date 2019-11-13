G90 ;absolute positioning
G1 X0 Y0 Z0 ;Home to corner 1 z0 plane

G91 ;relative positioning
G1 X1 F100 ;to corner 2 z0 plane
G1 Y1 F100 ;to corner 3 z0 plane
G1 X-1 F100 ;to corner 4 z0 plane
G1 Z1 F100 ;to corner 4 z1 plane
G1 Y-1 F100 ;to corner 1 z1 plane
G1 X1 F100 ;to corner 2 z1 plane
G1 Y1 F100 ;to corner 3 z1 plane