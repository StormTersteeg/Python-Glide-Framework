import settings
import os

if settings.debug: print(f"\n  {settings.app_name} - Ready\n")

class HTML:
  def __init__(self):
    self.html = ""

  def resourceImport(self, path):
    resource = ""
    if ".js" in path:
      resource = "".join(["<script>", open(path, "r").read(), "</script>"])
      if settings.debug: print("".join(["  [i] ", path]))
    elif ".css" in path:
      resource = "".join(["<style>", open(path, "r").read(), "</style>"])
      if settings.debug: print("".join(["  [i] ", path]))
    elif ".html" in path:
      resource = open(path, "r").read()
      if settings.debug: print("".join(["  [i] ", path]))
    else:
      resource = "".join(["<h3>Import went wrong for: ", path, "</h3>"])
      if settings.debug: print("".join(["  [!] Import went wrong for: ", path]))
    self.html = self.html + resource
  
  def getBody(self):
    return self.html

  def export(self):
    if settings.export_html:
      with open("bin/app.html", "w") as text_file:
        text_file.write(self.html)
    with open("".join(["bin/", settings.file_name]), "w") as text_file:
      text_file.write(f'''
import webview, os
class Api:
  def openChild(self, url):
    window.hide()
    child = webview.create_window(url, url, width=1500, height=850)
  def die(self):
    window.destroy()
    os._exit(0)
  def reload(self):
    os.startfile(__file__)
    self.die()
html = r\'\'\'
''')
      text_file.write(self.html)
      text_file.write(f'''
\'\'\'
api = Api()
window = webview.create_window("{settings.app_name}", html=html, js_api=api)
webview.start(gui='cef')
''')
    if settings.debug: print("  [+] Body exported")

if __name__ == '__main__':
  html = HTML()
  for resource in settings.resources:
    html.resourceImport(resource)
  html.export()

  if settings.preview:
    os.chdir("bin")
    os.startfile(settings.file_name)