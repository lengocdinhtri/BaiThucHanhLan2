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
    self.btn_sort.set_event_handler("click", self.btn_sort_click)

  def btn_sort_click(self, **event_args):
    input_numbers = self.text_input.text.split()
    
    try:
      numbers = [int(num) for num in input_numbers]
      
      sorted_ascending = self.insertion_sort(numbers.copy(), ascending=True)
      self.text_ascending.text = " ".join(map(str, sorted_ascending))
      
      sorted_descending = self.insertion_sort(numbers.copy(), ascending=False)
      self.text_descending.text = " ".join(map(str, sorted_descending))
    
    except ValueError:
      alert("Please enter valid integers separated by spaces.")
      
  def insertion_sort(self, arr, ascending=True):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] > key) if ascending else (arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

