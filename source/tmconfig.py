class TMConfig:

    title = u"Création d’un forum d'entraide pour les étudiants du Collège du Sud"
    first_name = 'Gabriel'
    last_name = 'Teixeira Dias'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Avril'
    day = u'3'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = ""
    repository_url = "https://github.com/{quasar-projet-true-form}"

    @classmethod
    def date(cls):
        return f"Le {cls.day} {cls.month.lower()} {cls.year}"

tmconfig = TMConfig()