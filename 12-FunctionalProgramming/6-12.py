medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7},
]


print(
    "\n".join(
        map(
            lambda ele: f"""{ele["country"]}: {
                ','.join(
                    map(
                        lambda x: str(x), 
                        filter(lambda val: str(val).isnumeric(), ele.values())
                    )
                )
            }""",
            filter(
                lambda country: sum(
                    filter(lambda val: str(val).isnumeric(), country.values())
                )
                >= 10,
                medals,
            ),
        )
    )
)
