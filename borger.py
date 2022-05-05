### Issues ###
# unwanted random.seed() update?
# cant deal with multiple meats


import csv
import random


class Borger:

    def __init__(self, num_meat, num_sauce, num_toppings, cursedlvl):
        """
        
        Parameters
        ----------
        num_meat : INT
            Number of meats to add to borger.
        num_sauce : INT
            Number of sauces to add to borger..
        num_toppings : INT
            Number of toppings to add to borger..
        cursedlvl : INT
            How cursed (weird) the borger will be.

        """
        random.seed()  # could be an unwanted seed update for other files?
        self.cursedlvl = cursedlvl
        self.bun = self.bun()
        self.meat = self.meat(num_meat)
        self.sauce = self.sauce(num_sauce)
        self.toppings = self.toppings(num_toppings)
        self.levels = ["Normal",
                       "Exotic",
                       "Lightly Cursed",
                       "Cursed",
                       "Abomination"]
        self.level = self.levels[cursedlvl - 1]

    def print(self):
        """
        
        Prints bun, meat, sauce, and toppings lists.

        """
        print("Bun: ", self.bun)
        print("Meats: ", self.meat)
        print("Sauces: ", self.sauce)
        print("Toppings: ", self.toppings)
        
    def ordered_print(self):
        """
        
        
        Prints all borger layers in order.

        """
        print(self.ordered_string())
                
    def ordered_string(self):
        """
        
        Returns
        -------
        text : STRING
            All borger layers in order with newline between layers.

        """
        text = ""
        borger = self.get_stack()
        for layer in borger:
            if len(layer) > 0:
                text += ', '.join(layer)
                text += "\n"
        
        return text

    def bun(self):
        """

        Returns
        -------
        bun : LIST
            List containing the bun to use.

        """
        bun = self.getItems('bun.txt')
        bun = self.condense(bun)
        bun = self.selector(bun, 1)
        return bun

    def meat(self, num):
        """

        Parameters
        ----------
        num : INT
            Number of meats to add on the borger.

        Returns
        -------
        meat : LIST
            List containing the meats to use.

        """
        # size - small, medium, large?
        meat = self.getItems('meat.txt')
        meat = self.condense(meat)
        meat = self.selector(meat, num)

        if num > 1:
            meat = self.placement(meat)

        return meat

    def sauce(self, num):
        """

        Parameters
        ----------
        num : INT
            Number of sauces to add on the borger.

        Returns
        -------
        sauce : LIST
            List containing the sauces to use,
            split into the bottom and top layer.

        """
        sauce = self.getItems('sauce.txt')
        sauce = self.condense(sauce)
        sauce = self.selector(sauce, num)
        sauce = self.placement(sauce)
        return sauce

    def toppings(self, num):
        """

        Parameters
        ----------
        num : INT
            Number of toppings to add on the borger.

        Returns
        -------
        toppings : LIST
            List containing the toppings to use,
            split into the bottom and top layer.

        """

        toppings = self.getItems('toppings.txt')
        toppings = self.condense(toppings)
        toppings = self.selector(toppings, num)
        toppings = self.placement(toppings)
        return toppings

    def placement(self, list):
        """

        Parameters
        ----------
        list : LIST
            List of items to split into a bottom and top layer.

        Returns
        -------
        new_list : LIST
            List containing a list of the bottom layer and one of the top.

        """

        random.shuffle(list)
        list_1 = []
        list_2 = []

        for i in range(len(list)):
            if i < (len(list) / 2):
                list_1.append(list[i])
            else:
                list_2.append(list[i])

        new_list = [list_1, list_2]

        return new_list

    def getItems(self, file):
        """

        Parameters
        ----------
        file : STRING
            Filename to use.

        Returns
        -------
        items : LIST
            List of all items in file under the cursed threshold,
            split into list of similarly cursed items.

        """
        items = []
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in reader:
                if i < self.cursedlvl:
                    items.append(row)
                    i += 1
                else:
                    break

        return items

    def condense(self, list):
        """

        Parameters
        ----------
        list : LIST
            List of lists.

        Returns
        -------
        new_list : LIST
            Single list containing items from all sublists.

        """
        new_list = []
        for lvl in list:
            new_list += lvl

        return new_list

    def selector(self, list, num):
        """

        Parameters
        ----------
        list : LIST
            List of items.
        num : INT
            Number of items to select.

        Returns
        -------
        new_list : LIST
            List of selected items.

        """
        new_list = []
        for i in range(num):
            new_list.append(list[random.randrange(len(list))])

        return new_list

    def get_stack(self):
        """

        Returns
        -------
        stack : LIST
            List of all borger items in order of placement.

        """
        # cant deal with multiple meats
        stack = [
            self.bun,
            self.sauce[1],
            self.toppings[1],
            self.meat,
            self.toppings[0],
            self.sauce[0],
            self.bun
        ]
        return stack