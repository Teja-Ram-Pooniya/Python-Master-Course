# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:01:03 2023

@author: Teja Ram Pooniya
@Program: Python sort User login and logout system
"""

class Event:  # Create an Event class to represent events
    def __init__(self, date, machine, event_type, user):
        self.date = date
        self.machine = machine
        self.type = event_type
        self.user = user

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":  # Corrected the equality operator here
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

# Create sample events as instances of the Event class
events = [
    Event("2023-08-16", "MachineA", "login", "User1"),
    Event("2023-08-16", "MachineA", "login", "User2"),
    Event("2023-08-16", "MachineB", "login", "User3"),
    Event("2023-08-16", "MachineA", "logout", "User1"),
    Event("2023-08-16", "MachineC", "login", "User4"),
]

# Call the functions to get current users and generate a report
current_machine_users = current_users(events)
generate_report(current_machine_users)
