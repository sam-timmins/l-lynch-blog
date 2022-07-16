def site_contexts(request):
    """ Site variables """
    name = 'Louise Lynch'
    email = 'l.lynch.engineer@gmail.com'
    twitter = 'https://twitter.com/louiselynch?lang=en'
    linkedin = 'https://www.linkedin.com/in/louiselynch/'

    contexts = {
        'name': name,
        'email': email,
        'twitter': twitter,
        'linkedin': linkedin,
    }

    return contexts
