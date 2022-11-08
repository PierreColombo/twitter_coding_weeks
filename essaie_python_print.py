import tweepy

api = tweepy.API


def count(max_values):
    count_return = 0
    for i in range(max_values):
        count_return += i
        print(f'{i} ---- {count_return}')
    return count_return


count(max_values=10)
