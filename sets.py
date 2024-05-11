

# 1. Python Sets Adventure

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

#1
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

mutual_routes = our_routes.intersection(competitor_routes)
print(mutual_routes)

#2

exclusive_our = our_routes.difference(competitor_routes)
print(exclusive_our)
exclusive_competitor = competitor_routes.difference(our_routes)
print(exclusive_competitor)

#3
unique_routes = our_routes.symmetric_difference(competitor_routes)
print(unique_routes)


#========================= 2. Set Operations in Data Analysis==================================

# Task 1: Duplicate Entries Cleanup
# You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.


customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
no_dupes = set(customer_ids)
print(no_dupes)


