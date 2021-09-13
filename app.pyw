import webview
import os

class App:
  def __init__(self):
    self.name = "Glide"
    self.visible = True
    self.doPrints = False
    if self.doPrints: print("\n  Glide - Ready\n")

class HTML:
  def __init__(self):
    self.html = ""

  def resourceImport(self, path):
    resource = ""
    if ".js" in path:
      resource = "".join(["<script>", open(path, "r").read(), "</script>"])
      if app.doPrints: print("".join(["  [i] ", path]))
    elif ".css" in path:
      resource = "".join(["<style>", open(path, "r").read(), "</style>"])
      if app.doPrints: print("".join(["  [i] ", path]))
    elif ".html" in path:
      resource = open(path, "r").read()
      if app.doPrints: print("".join(["  [i] ", path]))
    else:
      resource = "".join(["<h3>Import went wrong for: ", path, "</h3>"])
      if app.doPrints: print("".join(["  [!] Import went wrong for: ", path]))
    self.html = self.html + resource
  
  def getBody(self):
    return self.html

  def export(self):
    with open("glide/export.html", "w") as text_file:
      text_file.write(self.html)
    if app.doPrints: print("  [+] Body exported")

class Api:
  def openChild(self, url):
    window.hide()
    child = webview.create_window(url, url, width=1500, height=850)

  def die(self):
    import os
    os._exit(0)

  def reload(self):
    os.startfile("app.pyw")
    self.die()

app = App()

html = HTML()
html.resourceImport("glide/assets/roboto/roboto.min.css")
html.resourceImport("glide/assets/material-icons/material-icons.min.css")
html.resourceImport("glide/assets/material-4.1.1/material.min.css")
html.resourceImport("glide/assets/custom/custom.css")
html.resourceImport("glide/index.html")
html.resourceImport("glide/assets/jquery-3.5.1/jquery.slim.min.js")
html.resourceImport("glide/assets/popper-1.14.3/popper.min.js")
html.resourceImport("glide/assets/bootstrap-4.1.1/bootstrap.min.js")
html.resourceImport("glide/assets/material-4.1.1/material.min.js")
html.resourceImport("glide/assets/custom/custom.js")
html.export()

if __name__ == '__main__':
  api = Api()
  window = webview.create_window(app.name, html=html.getBody(), js_api=api)
  webview.start(gui='cef')