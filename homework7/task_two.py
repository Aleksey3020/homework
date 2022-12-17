def is_right_angle_triangle(side_a, side_b, side_c):
    result = {}
    if side_a + side_b > side_c:
        if side_a**2 + side_b**2 == side_c**2:
            result['result'] = True
            result['description'] = "the triangle is right-angled"
        else:
            result['result'] = False
            result['description'] = "the triangle is not right-angled"
    else:
        result['result'] = False
        result['description'] = "no such triangle exists"

    return result


result = is_right_angle_triangle(11, 11, 21)
print(result)
