from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#
# This is the Python code that makes this feedback form work.
# It's a Python class, with a method that runs when the user
# clicks the SUBMIT button.
#
# When the button is clicked, we send the contents of the
# text boxes to our Server Module. The Server Module records
# the feedback in the database, and sends an email to the
# app's owner (that's you!).
#
# To find the Server Module, look under "Server Code" on the
# left.
#


class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def submit_button_click(self, **event_args):
    # This method runs when the button is clicked.
    # First, we grab the contents of the text boxes:
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text

    # Now we call our Server Module to save our input
    # in the database and send you an email:
    anvil.server.call("add_feedback", name, email, feedback)
    # (Hint: Find ServerModule1 under "Server Code" on the
    # left. Click on the folder icon if you can't see it.)

    # Display something to the user so they know it worked:
    Notification("Feedback submitted!").show()
    self.clear_inputs()

  def clear_inputs(self):
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""
    def hoan_doi(arr, i, j):
      arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                hoan_doi(arr, j, j+1)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        hoan_doi(arr, i, min_idx)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:l+n1]
    R = arr[m+1:m+1+n2]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def in_mang(arr):
    for i in arr:
        print(i, end=' ')
    print()

def main():
    n = int(input("Nhap so luong phan tu: "))
    arr = []

    print("Nhap cac phan tu:")
    for _ in range(n):
        arr.append(int(input()))

    print("Chon thuat toan sap xep:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Merge Sort")
    choice = int(input("Nhap lua chon cua ban: "))

    if choice == 1:
        bubble_sort(arr)
        print("Mang sau khi sap xep bang Bubble Sort:")
        in_mang(arr)
    elif choice == 2:
        insertion_sort(arr)
        print("Mang sau khi sap xep bang Insertion Sort:")
        in_mang(arr)
    elif choice == 3:
        selection_sort(arr)
        print("Mang sau khi sap xep bang Selection Sort:")
        in_mang(arr)
    elif choice == 4:
        merge_sort(arr, 0, n-1)
        print("Mang sau khi sap xep bang Merge Sort:")
        in_mang(arr)
    else:
        print("Lua chon khong hop le!")

if __name__ == "__main__":
    main()
