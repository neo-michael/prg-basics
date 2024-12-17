results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

print(
    "\n".join(
        map(
            lambda x: (
                f"Min {x} pts: {list(filter(lambda result: result >= x, results))}"
            ),
            (70, 40, 30),
        )
    )
)
