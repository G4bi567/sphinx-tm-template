class TMConfig:

    title = u"Création d’un forum pour les étudiants du Collège du Sud"
    first_name = 'Gabriel'
    last_name = 'Teixeira Dias'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Janvier'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = "Version intermédiaire"
    repository_url = "https://github.com/{your-docs-url}"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()