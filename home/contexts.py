def site_contexts(request):
    """ Site variables """
    name = 'Louise Lynch'
    email = 'l.lynch.engineer@gmail.com'
    twitter = 'https://twitter.com/louiselynch?lang=en'
    linkedin = 'https://www.linkedin.com/in/louiselynch/'
    orcid = 'https://orcid.org/0000-0002-9842-3882'
    footer_name = 'louiselynch'

    contexts = {
        'name': name,
        'email': email,
        'twitter': twitter,
        'linkedin': linkedin,
        'orcid': orcid,
        'footer_name': footer_name,
    }

    return contexts
