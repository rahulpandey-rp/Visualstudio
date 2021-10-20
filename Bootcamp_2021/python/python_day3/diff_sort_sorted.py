first_list = [28, 67, 1, 24, 34, 91, 21, 543, 13, 34, 153, 134, 451]
second_list = [28, 67, 1, 24, 34, 91, 21, 543, 13, 34, 153, 134, 451]
# both list have same values
print(first_list, second_list)
# let apply sorted method on first list:
print(f"After applying sorted() method on first_list {sorted(first_list)}")
print(f"The original list after applying sorted method {first_list}")
# let apply sort method on second list:
second_list.sort()
print(f"After applying sort() method on first_list {second_list}")
# the original list is changed
