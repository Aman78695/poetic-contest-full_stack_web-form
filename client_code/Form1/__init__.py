from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    name=self.name.text
    email=self.email.text
    poem=self.poem.text
    anvil.server.call('poetry_sub',name,email,poem)
    Notification('poem submitted').show()
    self.clear_all()

  def clear_all(self):
    self.name.text=''
    self.email.text=''
    self.poem.text=''