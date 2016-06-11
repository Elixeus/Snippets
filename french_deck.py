#!/usr/bin/env python
ranks = [str(i) for i in range(2, 11)] + list('JQKA')
suits = list('CDHS')

deck = [(rank, suit) for suit in suits
        for rank in ranks]

print deck[:5]
