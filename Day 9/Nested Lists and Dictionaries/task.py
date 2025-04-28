# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
nested_list = ["A", "B", ["C", "D"]]

# print(travel_log["France"][2])
print(nested_list[2][1])
print(travel_log["Germany"]["cities_visited"][2])