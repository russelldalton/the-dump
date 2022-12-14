class Senator():
    def __init__(self, district, name, email):
        self.district = district
        self.name = name
        self.email = email

    def districtof(self):
        return self.district
    
    def nameof(self):
        return self.name 
    
    def emailof(self):
        return self.email

def main():
    file = open('MaineSenate.csv','r')
    file.readline()
    senators = {}
    for line in file:
        data=line.split(',')
        data[0] = int(data[0])
        senators[data[0]] = Senator(data[0], data[4] + "," + data[3], data[-1])

    file.close()

    senatelist = list(senators.items())
    senatelist.sort()
    for senator in senatelist:
        print ('{:2} {}'.format(senator[0], senator[1].nameof()))

    print()

    senatelist = list(senators.values())
    senatelist.sort(key = Senator.nameof)
    for senator in senatelist:
        print("{:2} {}".format(senator.districtof(), senator.nameof()))

    print()
    x= int(input("which district do you want to see? "))
    print('{:2} {} {}'.format(x, senators[x].nameof(), senators[x].emailof()))

if __name__ == "__main__": 
    main()
