def get_fixed_scale_values(start, end, tk_start, tk_end):
    """get_fixed_scale_values uses the equations of the start and end of the axis
    (eg. start equation: tk_start = start * m + c, end equation: tk_end = end * + c),
    then substitution is applied by subtracting each equation to figure out m,
    then figuring out c with the m value. The result is the gradient(m) and the
    x/y intercept (c)"""
    tk_difference = tk_end - tk_start
    difference = end - start
    m = tk_difference / difference
    c = tk_end - (end * m)
    return m, c


"""Debug y scale"""


def get_y_scale(y, y_start, y_end, y_tk_start, y_tk_end):
    """get_y_scale uses the values of the y axis line to get
    its gradient and y-intercept to apply to the user given
    y co-ordinate, to scale it to the TKinter y co-ordinate
    value"""
    # y_m, y_c = get_fixed_scale_values(y_start, y_end, y_tk_start, y_tk_end)
    # extra_value = y_tk_end
    m = (y_tk_start - y_tk_end) / (y_end - y_start)
    return ((y_end - y) * m) + y_tk_end
    # return (y * -1) * y_m + y_c


def get_x_scale(x, x_start, x_end, x_tk_start, x_tk_end):
    """get_x_scale uses the values of the x axis line to get
    its gradient and x-intercept to apply to the user given
    x co-ordinate, to scale it to the TKinter x co-ordinate
    value"""
    m = (x_tk_start - x_tk_end) / (x_end - x_start)
    return ((x_end - x) * m) + x_tk_end
    # x_m, x_c = get_fixed_scale_values(x_start, x_end, x_tk_start, x_tk_end)
    # return x * x_m + x_c


def main():
    gradient, y_intercept = get_fixed_scale_values(-4, 4, 100, 900)
    y_value = get_y_scale(3, -5, 5, 600, 100)
    x_value = get_x_scale(3, -5, 5, 100, 600)

    print(f"get_fixed_scale_values: {gradient}, {y_intercept}")
    print(f"get_y_scale: {y_value}")
    print(f"get_x_scale: {x_value}")


if __name__ == "__main__":
    main()
