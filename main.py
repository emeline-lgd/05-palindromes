"""
Dans cet exercice on cherche a savoir si une chaine de caractère
est un palindrome ou non.
avec les fonction  isprimeispalindrome(p) et main()
"""
#### Fonction secondaire


def ispalindrome(p):

    # votre code ici

    """
    Cette fonction nous permet de retourner un booléen 
    si la chaine de caratere mis en argument "p" est un palindrome (True)  si non (False)
    """
    p = p.lower()
    p = p.translate(str.maketrans("éèêëàâäîïôöùûüç","eeeeaaaiioouuuc"," !:;,?./'()-"))
    if p == p[::-1]:
        return True
    return False

#### Fonction principale


def main():
    """
    main() est la fonction principale qui print si s est un palindrome
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
