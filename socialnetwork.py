# Creating a model of a social network with basic functions

# network is a list of [name, [locationx, locationy], [friends list], [interest list]]

class Person:
    # creating a person
    def __init__(self, name, location_list, friends_list, interest_list):
        self.name = name
        self.location_list = location_list
        self.friends_list = friends_list
        self.interest_list = interest_list

# optional: allow to read directly from txt file
def init():
    f = open("smallnetwork.txt", "r")
    content = f.read()
    smallnetwork = eval(content)
    network = []        # list of Person objects
    for person in smallnetwork:
        # 0 - name, 1 - location_list, 2 - friends_list, 3 - interest_list
        network.append(Person(person[0], person[1], person[2], person[3]))
    f.close()
    return network

# print names
# return: void, params: none
def get_names():
    for person in network:
        print(person.name)

# gets a list of most popular people
# return: list, params: none
def get_most_popular():
    return get_most_popular_from_list(network)

# gets a list of most popular people from given list
# return: list, params: list
def get_most_popular_from_list(network):
    if len(network) == 0:
        most_popular = None
    else:
        most_popular = [network[0]]
        for person in network:
            if len(person.friends_list) > len(most_popular[0].friends_list):
                most_popular = [person]
            elif len(person.friends_list) == len(most_popular[0].friends_list):
                most_popular.append(person)
    
    most_popular = list_to_string(most_popular)
    return most_popular

# gets a list of most least people
# return: list, params: none
def get_least_popular():

    if len(network) == 0:
        least_popular = None
    else:
        least_popular = [network[0]]
        for person in network:
            if len(person.friends_list) < len(least_popular[0].friends_list):
                least_popular = [person]
            elif len(person.friends_list) == len(least_popular[0].friends_list):
                least_popular.append(person)
    
    least_popular = list_to_string(least_popular)
    return str(least_popular)

def list_to_string(given_list):
    return_list = []
    for elem in given_list:
        return_list.append(elem.name)
    return return_list

# takes a name and returns name of person with most mutual friends
# return: string, params: string
def recommend_friend_for(name):
    most_mutuals = 0
    recommended_friend = None

    for p in network:
        if p.name == name:
            continue
        mutuals = number_of_mutual_friends(name, p.name)
        #print(p.name, mutuals)     # for testing
        if most_mutuals < mutuals:
            recommended_friend = p.name
            most_mutuals = mutuals
    
    return recommended_friend

# takes a name and returns name of person with most shared interests
# return: string], params: string
def recommend_by_interest(name):
    most_mutuals = 0
    recommended_friend = None

    for p in network:
        if p.name == name:
            continue
        mutuals = number_of_shared_interests(name, p.name)
        #print(p.name, mutuals)     # for testing
        if most_mutuals < mutuals:
            recommended_friend = p.name
            most_mutuals = mutuals
    
    return recommended_friend

# takes two names and calculates number of mutuals between them
# return: int, params: string, string
def number_of_mutual_friends(name1, name2):
    person1 = get_person(name1)
    person2 = get_person(name2)

    if name2 in person1.friends_list:
        mutuals = -1 # already friends
    else:
        mutuals = 0
        for friend1 in person1.friends_list:
            for friend2 in person2.friends_list:
                if friend1 == friend2:
                    mutuals += 1
    return mutuals

# takes two names and calculates number of shared interests between them
# return: int, params: string, string
def number_of_shared_interests(name1, name2):
    person1 = get_person(name1)
    person2 = get_person(name2)

    if name2 in person1.friends_list:
        mutuals = -1 # already friends
    else:
        mutuals = 0
        for interest1 in person1.interest_list:
            for interest2 in person2.interest_list:
                if interest1 == interest2:
                    mutuals += 1
    return mutuals

# takes interest and returns most popular person (most friends) with the same interest
# return: string, params: string
def target_ad(interest):
    interest_network = []
    for person in network:
        if interest.lower() in person.interest_list:
            interest_network.append(person)
    
    if len(interest_network) > 0:
        return get_most_popular_from_list(interest_network)
    else:
        return None


# takes a name and returns corresponding person
# return: Person, params: string
def get_person(name):
    for person in network:
        if person.name == name:
            return person

# main method
def main():
    get_names()
    # testing
    print("Most popular person:", get_most_popular())
    print("Least popular person:", get_least_popular())
    x = input("Recommend friend for? (by mutuals): ")
    print("Friend for", x, ":", recommend_friend_for(x))
    y = input("Recommend friend for? (by mutual interests): ")
    print("Friend for", y, ":" recommend_by_interest(y))
    z = ("Target advertisement for which interest? ")
    print(target_ad(z))

network = init()    # global constant, list of Person objects
main()