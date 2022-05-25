class Ninja:
    def pattern(self):
        rows = int(input("How many rows you want? :"))
        for i in range(rows):
            for j in range(i+1):

                print(i,end=" ")
            print()

        x = 5

        i = 1
        while i <= x:
            j = 1
            while j <= i:
                print("*", end=" ")
                j += 1
            print()
            i += 1
n1 = Ninja()

n1.pattern()