def  apply_all_func(int_list, *functions):
    results = {}
    try:
        for function in functions:
            results.update({function.__name__: function(int_list)})
        return results
    except TypeError:
        return f'Переданы неверные данные, должно быть только число!'

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
