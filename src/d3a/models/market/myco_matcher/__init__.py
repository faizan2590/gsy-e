from d3a.constants import FLOATING_POINT_TOLERANCE


class MycoMatcher:
    def __init__(self):
        self.offer_bid_pairs = []

    @staticmethod
    def sorting(obj, reverse_order=False):
        if reverse_order:
            # Sorted bids in descending order
            return list(reversed(sorted(
                obj.values(),
                key=lambda b: b.energy_rate)))

        else:
            # Sorted bids in ascending order
            return list(sorted(
                obj.values(),
                key=lambda b: b.energy_rate))

    def _perform_pay_as_bid_matching(self):
        # Pay as bid first
        # There are 2 simplistic approaches to the problem
        # 1. Match the cheapest offer with the most expensive bid. This will favor the sellers
        # 2. Match the cheapest offer with the cheapest bid. This will favor the buyers,
        #    since the most affordable offers will be allocated for the most aggressive buyers.

        # Sorted bids in descending order
        sorted_bids = self.sorting(self.bids, True)

        # Sorted offers in descending order
        sorted_offers = self.sorting(self.offers, True)

        already_selected_bids = set()
        offer_bid_pairs = []
        for offer in sorted_offers:
            for bid in sorted_bids:
                if bid.id not in already_selected_bids and \
                        (offer.energy_rate - bid.energy_rate) <= \
                        FLOATING_POINT_TOLERANCE and offer.seller != bid.buyer:
                    already_selected_bids.add(bid.id)
                    offer_bid_pairs.append(tuple((bid, offer)))
                    break
        return offer_bid_pairs

    def match_offers_bids(self, bids, offers):
        self.bids = bids
        self.offers = offers
        self.offer_bid_pairs = []
        self.offer_bid_pairs = self._perform_pay_as_bid_matching()
