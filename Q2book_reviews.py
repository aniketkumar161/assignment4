class Book:
    def __init__(self,title,auther):
        self.title = title
        self.auther = auther
        self.reviews = []

    def add_reviews(self, reviews):
        self.reviews.append(reviews)
        print("reviwes added sucessfully")

    def count_reviews(self):
        print("total reviews", len(self.reviews))

    def display_reviews(self):
        
        print("title :",self.title)
        print("auther:",self.auther)
        print("reviwes:",)

        for reviwers in self.reviews:
            print("-", reviwers)

Book1 = Book("python basic","aniket")

Book1.add_reviews("Very useful book")
Book1.add_reviews("Easy to understand")
Book1.add_reviews("Good examples")

Book1.count_reviews()
Book1.display_reviews()
