class Insect:

    def __init__(self, name="Mia", speed=10, weight=10, age=0, insect_type="bug"):
        self.__name = name
        self.__speed = speed
        self.__weigth = weight
        self.age = age
        self.insect_type = insect_type

    def __del__(self):
        print(f"Object Insect with name {self.__name} destructed")

    def __str__(self):
        return f"Insect name is {self.__name} and it fly with speed {self.__speed} m/s. Its weigth is {self.__weigth}g"

    def __repr__(self):
        return f"Insect(name = {self.__name}, speed = {self.__speed}, weigth = {self.__weigth})"
    
    def main(self):
        """
        Method prints all values of object
        """
        print(f"Name is {self.__name}")
        print(f"Speed is {self.__speed} m/s")
        print(f"Weight is {self.__weigth}g")
        print(f"Age is {self.age}g")
        print(f"Type of insect is {self.insect_type}g")

    def set_data(self, name, speed, weight):
        """
        Method that changes private and locked variables
        """
        self.__name = name
        self.__speed = speed
        self.__weigth = weight

    def get_name(self):
        """
        Method that return name of insect
        """
        
        return self.__name
    
    def get_speed(self):
        """
        Method that return speed of insect
        """

        return self.__speed
    
    def get_weight(self):
        """
        Method that return weight of insect
        """
        return self.__weight


if __name__ == "__main__":
    bee = Insect("Buzz", 50, 20, 1.5, "bee")
    bee.main()
