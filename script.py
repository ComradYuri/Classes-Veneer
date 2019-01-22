# Creates an empty listing list. With methods listings can be added, removed or show the current listing
class Marketplace:
    def __init__(self,):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, sold_listing):
        self.listings.remove(sold_listing)

    def show_listing(self):
        for listing in self.listings:
            return listing


# Creates a client with 4 parameters. With methods a artwork can be added to marketplace listing for a specified price
# The buy_artwork method allows a Client to first check if the artwork is for sale then check if there are enough funds
# in his wallet and then buy the artwork. This removes it from the marketplace listing and transfers the funds
class Client:
    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.is_museum = is_museum
        self.wallet = wallet
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            listing = Listing(artwork, price, self)
            veneer.add_listing(listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork and self.wallet >= (int(listing.price[1])) * 10 ** 6:
                    art_listing = listing
                    break

            if art_listing is not None:
                artwork.owner.wallet += (int(listing.price[1])) * 10 ** 6
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)
                self.wallet += -(int(listing.price[1])) * 10 ** 6


# Creates art class that takes 5 parameters. string repr returns in formatted style the properties of the artwork
class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{}. \"{}\". {}, {}. {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)


# Creates a listing that takes 3 parameters. string repr returns in formatted style the name and price
class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{} - {}.".format(self.art.title, self.price)


# create an instance of Marketplace called Veneer
veneer = Marketplace()
# prints current listings >>> returns 'None' at the moment
print(veneer.show_listing())
# create 2 instances of Client with their name, location, is_museum and current funds
edytta = Client("Edytta Halpirt", None, False, 4000000)
moma = Client("The MOMA", "New York", True, 12000000)
# prints MOMA and edytta's wallets before any purchases
print(moma.wallet)
print(edytta.wallet)

# creates an artwork instance beloning to Edytta Halpirt and then prints it information (string repr)
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
print(girl_with_mandolin)

# Puts a new listing on the marketplace. The artwork is on sale for 6M. It still is owned by Edytta.
# Additionally, the current marketplace listings are printed (Title + price )
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
print(veneer.show_listing())

# MOMA buys artwork from marketplace veneer
moma.buy_artwork(girl_with_mandolin)
# Prints info of artwork with current owner (is MOMA because transaction was successful)
print(girl_with_mandolin)
# prints MOMA and edytta's wallets after any purchases
print(moma.wallet)
print(edytta.wallet)
