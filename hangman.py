import random

WORDS = ["аист", "акула", "бабуин", "баран", "барсук", "бобр", "бык", "варан", "верблюд", "волк", "вомбат", "воробей", "ворон", "выдра",
"голубь", "гусь", "додо", "дятел", "енот", "ехидна", "еж", "жаба", "жираф", "журавль", "заяц", "зебра", "землеройка", "зяблик",
"игуана", "кабан", "казуар", "кайман", "какаду", "кальмар", "камбала", "канарейка", "каракатица", "карп", "кенгуру",
"киви", "кит", "лама", "ламантин", "ласка", "ласточка", "лебедь", "лев", "лемур", "ленивец", "леопард", "лиса", "лягушка",
"мотылек", "муравьед", "муравей", "мангуст", "медведь", "морж", "муха", "мышь", "медуза", "нарвал", "носорог", "орел", "омар", "олень", "овцебык",
"осьминог", "орел", "осел", "оса", "овца", "опоссум", "обезьяна", "паук", "пескарь", "пингвин", "пиранья", "попугай",
"пчела", "рысь", "рыба", "росомаха", "страус", "сурок", "стрекоза", "сорока", "сова", "снегирь", "сокол", "собака", "слон",
"слон", "скорпион", "скворец", "скат", "сельдь", "свинья", "сурикат", "скунс", "слизень", "светлячок", "тюлень", "тукан", "тигр",
"трясогуска", "термит", "тетерев", "тунец", "тритон", "тарантул", "таракан", "тля", "утконос", "уж", "устрица", "улитка", "угорь", "фазан", "фламинго",
"форель", "хорек", "хомяк", "хамелеон", "цапля", "цесарка", "цикада", "черепаха", "червь", "чайка", "шимпанзе", "шиншилла",
"щука", "эму", "ящерица", "ястреб", "як", "ягуар"]


MAX_ERRORS = 10


def return_random_word():
    return random.choice(WORDS)


def handle_user_input():
    user_input = input('Please, input letter: ')
    return user_input


def get_initial_statuses(word):
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses


def is_game_finished(statuses, current_errors):
    if current_errors >= MAX_ERRORS:
        return True

    for status in statuses:
        if not status:
            return False

    return True


def perfom_check_action(word, statuses, letter):
    if letter not in word:
        return False

    for index, l in enumerate(word):
        if letter == l:
            statuses[index] = True

    return True


def print_word(word, statuses):
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end='')
        else:
            print('_', end=' ')
    print()


def main():
    word = return_random_word()
    statuses = get_initial_statuses(word)
    current_errors = 0

    while not is_game_finished(statuses, current_errors):
        print_word(word, statuses)
        print('Errors left: ', MAX_ERRORS - current_errors)
        letter = handle_user_input()
        result = perfom_check_action(word, statuses, letter)

        if not result:
            current_errors += 1

    if current_errors >= MAX_ERRORS:
        print('You lose!')
    else:
        print('You win!')


main()
