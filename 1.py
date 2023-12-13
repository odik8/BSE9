#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    school = {"1a": 20, "1б": 25, "2a": 18, "2б": 23, "3a": 21, "3б": 24, }
    
    school["1a"] += 1

    school["4a"] = 20

    del school["2a"]

    count_of_students = sum(school.values())
    return f"В школе с классами {school} - {count_of_students} учеников"

if __name__ == "__main__":
    print(main())
