# What I done

- I made a new method `print_total_price` to calculate the total price of the items. 
  - I could've added the same logic into the `print_receipt` method but it was cleaner and better to separate it which allowed for better testing
- It seemed `add.item` already put the items in-order so I didn't have to do anything
- I changed print format from `key - value - price` to `key x value = price`
- I added a boolean parameter `price_first` in the print_receipt to allow price first, 
- Altered the `print_receipt` method to display an error message if there are no items in shopping cart but still somehow tried to print the receipt
- Added method `convert_cents_to_euros` to convert the price to euro format with the € sign e.g. `500 --> €5.00`
- Displaying all items in print_total_price in a list e.g. `Total Price of ['apple x 1', 'banana x 2'] is €5.00`
- Total of 14 tests trying to test everything. Also covering the methods I created `convert_cents_to_euros` and `print_total_price`
