def main():

        print("Kobtronix....With codesmiths...;)")
      
        print("Welcomes you to pigLatin translator ")
        lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']

        sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
        return sentence[1:] + sentence[0] + "ay"
        
  

def t(str):
        return str[0]+str[1]

if __name__ == "__main__":
        x = main()
        print(x)