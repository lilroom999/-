def base_converter(decimal_number, base):
    """Convert decimal number to any base.

    decimal_number : int : The decimal number to be converted
    base : int : The base to convert the decimal number to

    Returns : str : The converted number in the specified base
    """
    if not (2 <= base <= 36):       # 判斷base是否在2~36之間
        return "Invalid base. Base should be between 2 and 36."

    if not (0 <= decimal_number):   # 判斷decimal_number是否大於等於0
        return "Invalid decimal number. Number should be greater than or equal to 0."

    base_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 建立base_digits字串
    result = ""
    while decimal_number:
        remainder = decimal_number % base # 取出餘數
        decimal_number //= base           # 取整數值
        result = base_digits[remainder] + result # 將餘數轉換為對應的字元，並加入result字串
    return result

decimal_number = int(input("Enter decimal number: ")) # 輸入要轉換的十進位數字
base = int(input("Enter base to convert to (2-36): ")) # 輸入要轉換的進制
print("Converted number: ", base_converter(decimal_number, base)) # 印出轉換後的數字
input()