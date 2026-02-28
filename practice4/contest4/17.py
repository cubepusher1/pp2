import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def segment_inside_circle(x1, y1, x2, y2, r):
    # vector from P1 to P2
    dx = x2 - x1
    dy = y2 - y1

    # quadratic coefficients for intersection with circle
    a = dx**2 + dy**2
    b = 2 * (x1*dx + y1*dy)
    c = x1**2 + y1**2 - r**2

    disc = b**2 - 4*a*c

    # No intersection
    if disc <= 0:
        # if both points inside, return distance
        if x1**2 + y1**2 <= r**2 and x2**2 + y2**2 <= r**2:
            return math.hypot(dx, dy)
        else:
            return 0.0

    # find t values for intersections
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc)/(2*a)
    t2 = (-b + sqrt_disc)/(2*a)

    # clamp t to [0,1] to segment
    t_low = max(0, min(t1, t2))
    t_high = min(1, max(t1, t2))

    if t_low > 1 or t_high < 0:
        # segment outside circle
        if x1**2 + y1**2 <= r**2 and x2**2 + y2**2 <= r**2:
            return math.hypot(dx, dy)
        return 0.0

    # compute points of intersection on segment
    ix1 = x1 + dx * t_low
    iy1 = y1 + dy * t_low
    ix2 = x1 + dx * t_high
    iy2 = y1 + dy * t_high

    return math.hypot(ix2 - ix1, iy2 - iy1)

res = segment_inside_circle(x1, y1, x2, y2, r)
print(f"{res:.10f}")