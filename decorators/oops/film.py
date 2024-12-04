class Film():
    title=str
    rating:float
    runtime:float
    director:str
    genre:str
    language:str

    def set_film(self,title,rating,runtime,director,genre,language):
        self.title=title
        self.rating=rating
        self.runtime=runtime
        self.director=director
        self.genre=genre
        self.language=language


    def film_display(self):   
        print(self.title,self.rating,self.runtime,self.director,self.genre,self.language) 



film_instance1=Film()
film_instance2=Film()
film_instance3=Film()
film_instance4=Film()

film_instance1.set_film("ARM",8.5,2.45,"JITHIN LAL","THRILLER","MALAYALAM")
film_instance2.set_film("KGF",9.0,3,"PRASHANTH NEEL","ACTION","KANNADA")
film_instance3.set_film("JAWAN",8.0,2.45,"ATLEE KUMAR","ACTION","HINDI")
film_instance4.set_film("INTERSTELLAR",9.4,3.02,"CHRISTOPHER NOLAN","SCI-FI","ENGLISH")


film_instance1.film_display()
film_instance2.film_display()
film_instance3.film_display()
film_instance4.film_display()