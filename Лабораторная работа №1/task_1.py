numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_element_index = 4  # Индекс пропущенного элемента

sum_of_numbers = sum(numbers[:missing_element_index]) + sum(numbers[missing_element_index+1:])
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers
numbers[missing_element_index] = average_of_numbers

print("Измененный список:", numbers)
