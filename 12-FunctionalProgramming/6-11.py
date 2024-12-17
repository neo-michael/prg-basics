test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52},
]

print(
    list(
        filter(
            lambda res: res["result"] >= 50 and res["result"] <= 70,
            test_results
        )
    )
)