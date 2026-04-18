def solution(sizes):
    width = []
    height = []
    
    for w, h in sizes:
        if w < h:
            w, h = h, w
        width.append(w)
        height.append(h)
    return max(width) * max(height)

