def print_receipt(subtotal, tax_rate, tip_rate):
    """
    The function is to print receipts
    """
    str0 = " "  # a space
    str1 = "Subtotal: $"  # 11 characters, but totally 21 characters
    str2 = "     Tax: $"
    str3 = "     Tip: $"
    str4 = "   Total: $"
    tax = str('{0:.2f}'.format(tax_rate*subtotal)) # Print 2 digits after the decimal point
    tip = str('{0:.2f}'.format(tip_rate*subtotal))
    sub = str('{0:.2f}'.format(subtotal))
    ttl = str('{0:.2f}'.format(subtotal + tip_rate*subtotal + tax_rate*subtotal))
    
    print(str1 + str0*(21-len(str1)-len(sub)) + sub)
    print(str2 + str0*(21-len(str2)-len(tax)) + tax)
    print(str3 + str0*(21-len(str3)-len(tip)) + tip)
    print(str0*11 + '='*10)
    print(str4 + str0*(21-len(str4)-len(ttl)) + ttl)

    