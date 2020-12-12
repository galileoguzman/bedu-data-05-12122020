from helpers import sum_time

items = [
    {
        'duration': {
            'otro': 8162
        }
    },
    {
        'duration': {
            'otro': 82763
        }
    },
    {
        'duration': {
            'otro': 23234
        }
    }
]

new_items = list(map(sum_time, items))
print(new_items)
