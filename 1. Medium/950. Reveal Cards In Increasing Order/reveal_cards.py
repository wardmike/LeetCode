# Prompt: https://leetcode.com/problems/reveal-cards-in-increasing-order/
# Runtime: 36 ms, faster than 67.20% of Python online submissions for Reveal Cards In Increasing Order.
# Memory Usage: 13.7 MB, less than 59.20% of Python online submissions for Reveal Cards In Increasing Order.


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        startDeck = []

        # following reverse order of card reveal to build starting deck

        startDeck.append(deck.pop(-1))
        
        while len(deck) > 1:
            startDeck.insert(0, deck.pop(-1))
            # bring last card to front
            last = startDeck.pop(-1)
            startDeck.insert(0, last)
        
        # don't bring last card to front on last iteration
        if len(deck) > 0:
            startDeck.insert(0, deck.pop(-1))    
        
        return startDeck
