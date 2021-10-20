class Article():

    def __init__(self, title, authors, abstract, url):
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.url = url

    def __str__(self):
        return f"{self.title}\n\t{self.authors}\n\t{self.abstract[::100]}\n\t{self.url}"

    @staticmethod
    def new_from_content(content):
        infos = content.split("\\")

        # remove empty strings and \n
        infos_filtered = list(filter(lambda x: bool(x) and x != '\n', infos))

        # vérifier que c'est de longueur 3
        # si oui :

        # 1er élément
        premier_paragraphe = infos_filtered[0]
        title = list(filter(lambda x: 'Title:' in x, premier_paragraphe.split("\n")))
        authors = list(filter(lambda x: 'Authors:' in x, premier_paragraphe.split("\n")))

        # 2e élément = abstract
        abstract = infos_filtered[1]

        # dernier élément = url
        info_url = infos_filtered[-1]
        url = list(filter(lambda x: 'https' in x, info_url.split(" ")))
        return Article(title, authors, abstract, url)



# load txt file in "mail"
with open(r'C:\Users\laeti\Desktop\arXiv.txt') as f:
    mail = f.read()

categories = mail.split("%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%")
# with abstract in categroies[0]
# no abstract in categories[1]

articles_candidates = categories[0].split("------------------------------------------------------------------------------")

for candidate in articles_candidates:
    if candidate.startswith('\n\\'):
        # instance un objet de la classe Article
        mon_article = Article.new_from_content(candidate)
        # récupère le titre, l'abstract et l'url en attribut de classe

        print(mon_article.title)

        action = input("Print abstract (a), URL (u) or go to next one (Enter) ?")

        while action:
            if action.lower() == 'a':
                print(mon_article.abstract) # ou méthode de classe ? mais parait un peu inutile
                action = input("Print abstract (a), URL (u) or go to next one (Enter) ?")
            elif action.lower() == 'u':
                print(mon_article.url)
                action = input("Print abstract (a), URL (u) or go to next one (Enter) ?")
            # elif action.lower() == 'n':
            #     continue
            else:
                action = input("Print abstract (a), URL (u) or go to next one (Enter) ?")