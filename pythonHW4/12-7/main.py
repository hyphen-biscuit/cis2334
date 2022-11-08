#Dash Wendt 2033998
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age

def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a', age, 'year-old:', 
heart_rate, 'bpm')

    except ValueError as e:
        print(e)
        print('Could not calculate heart rate info.')
        print()