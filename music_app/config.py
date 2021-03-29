class Config(object):
    """
    A class used to contain the configuration data for the application

    ...

    Attributes
    -------
    SECRET_KEY : str
        a secret key to support server side encryption
    SQLALCHEMY_DATABASE_URI : str
        the connection string to database
    """

    # These can be set to environment varibale and the import using os.environ.get
    SECRET_KEY = '64f8419f29e6247dd50447ad46776715'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///musicapp.db'