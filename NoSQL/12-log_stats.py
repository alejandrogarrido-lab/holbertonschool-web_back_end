#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx

    print("{} logs".format(col.count()))
    print("Methods:")

    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(m, col.count({"method": m})))

    print("{} status check".format(
        col.count({"method": "GET", "path": "/status"})
    ))
