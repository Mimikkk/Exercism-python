list_lyric = ['twelve Drummers Drumming, ',
               'eleven Pipers Piping, ',
               'ten Lords-a-Leaping, ',
               'nine Ladies Dancing, ',
               'eight Maids-a-Milking, ',
               'seven Swans-a-Swimming, ',
               'six Geese-a-Laying, ',
               'five Gold Rings, ',
               'four Calling Birds, ',
               'three French Hens, ',
               'two Turtle Doves, ',
               'and a Partridge in a Pear Tree.'
               ]

day_lyric = ['first',
             'second',
             'third',
             'fourth',
             'fifth',
             'sixth',
             'seventh',
             'eighth',
             'ninth',
             'tenth',
             'eleventh',
             'twelfth'
             ]


def recite(start_verse, end_verse):

    output_lyric = []
    for verse in range(start_verse, end_verse + 1):
        verse_lyric = [f'On the {day_lyric[verse - 1]} day of Christmas my true love gave to me: ']
        if verse == 1:
            verse_lyric.append(list_lyric[11][4:])
        else:
            verse_lyric += list_lyric[(12 - verse):]
        output_lyric.append(''.join(verse_lyric))
    return output_lyric
