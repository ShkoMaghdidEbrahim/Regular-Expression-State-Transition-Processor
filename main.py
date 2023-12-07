from time import sleep

class Object :
    def __init__(self, char, to) :
        self.char = char
        self.to = to

def main() :
    global value
    re = "abc|gkf|md"
    numbers_to_skip: int = 1
    objects = []
    regex_array = re.split("|")
    for i in range(len(regex_array)) :
        regex_part = regex_array[i]
        objects.append([])
        for j in range(len(regex_part)) :
            objects[i].append(Object(regex_part[j], numbers_to_skip + 1))
            numbers_to_skip += 1
        if i == len(regex_array).__sub__(2) :
            numbers_to_skip -= 1
    end_state = 0
    for i in range(len(objects)) :
        array = objects[i]
        for j in range(len(array)) :
            if j == len(array) - 1 and i == 0 :
                end_state = array[j].to
            if j == len(array) - 1 :
                array[j].to = end_state
    for object_array in objects :
        for j in range(len(object_array)) :
            if object_array[j].to == end_state and len(object_array) == 1 :
                object_array[j].from_ = 1
            elif j == 0 :
                object_array[j].from_ = 1
    for object_array in objects :
        temp = 1
        for value in object_array :
            print("from " + str(temp) + ",", end = " ")
            print(value.char, end = " ")
            print("goes to " + str(value.to))
            temp = value.to
        print()


if __name__ == "__main__" :
    main()
