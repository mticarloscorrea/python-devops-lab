def get_total(cost,items,tax):
    subtotal=0
    for item in items:
        subtotal+=cost.get(item,0)

    total=subtotal+(subtotal*tax)
    return round(total,2)