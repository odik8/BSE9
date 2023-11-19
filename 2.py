#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    dict1 = {1: "one", 2: "two", 3: "three"}

    reversed_dict = {value: key for key, value in dict1.items()}
    return reversed_dict



if __name__ == "__main__":
    print(main())