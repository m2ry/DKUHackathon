#importing website package...

from website import create_app

app = create_app()

#only runs when the file is ran directly, not just imported.
if __name__ == 'main':
  app.debug(d
