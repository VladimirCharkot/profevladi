def setup():
    size(300, 300)
    background(226, 208, 152)
    
    n = 13     # cantidad de líneas
    s = 300   # screen size 
    m = 20    # margen
    i = (s - 2 * m) / (n - 1)   # interlineado

    # Horizontales
    x1 = m
    x2 = m + (n - 1) * i
    for c in range(n):
        y1 = m + c * i
        y2 = y1
        line(x1, y1, x2, y2)
        
    # Verticales
    y1 = m
    y2 = m + (n - 1) * i
    for c in range(n):
        x1 = m + c * i
        x2 = x1
        line(x1, y1, x2, y2)
    
    fill(0)  # negro
    circle(m + 3 * i, m + 3 * i, 5)
    circle(m + 9 * i, m + 3 * i, 5)
    circle(m + 3 * i, m + 9 * i, 5)
    circle(m + 9 * i, m + 9 * i, 5)
    
