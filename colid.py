# Python 3program to check if a
# string is of the form a^nb^n.

# Returns true str is of the
# form a^nb^n.


def isAnBn(str):
    n = len(str)

    # After this loop 'i' has
    # count of a's
    for i in range(n):
        if (str[i] != 'a'):
            break

    # Since counts of a's and b's should
    # be equal, a should appear exactly
    # n/2 times
    if i * 2 != n:
        return False

    # Rest of the characters must
    # be all 'b'
    for j in range(i, n):
        if str[j] != 'b':
            return False

    return True


# Driver code
if __name__ == "__main__":
    str = "aba"
    print("Yes") if isAnBn(str) else print("No")

# This code is contributed
# by ChitraNayal
