from calcbackend import *
from genparser import *


class calcParser(Parser):
    def __init__(self):
        super().__init__(
            {
                0: LR0State(
                    0,
                    frozenset(
                        {
                            LR0Item(0, Production(0, 11, [12, 10], "Prog"), 0, set()),
                            LR0Item(
                                1, Production(1, 12, [12, 13, 9], "None"), 0, set()
                            ),
                            LR0Item(
                                2, Production(2, 12, [], "None"), 0, {8, 1, 10, 0, 7}
                            ),
                        }
                    ),
                    {12: 1},
                    False,
                ),
                1: LR0State(
                    1,
                    frozenset(
                        {
                            LR0Item(2, Production(3, 13, [14], "print(E)"), 0, set()),
                            LR0Item(3, Production(0, 11, [12, 10], "Prog"), 1, set()),
                            LR0Item(
                                3, Production(1, 12, [12, 13, 9], "None"), 1, set()
                            ),
                            LR0Item(
                                3,
                                Production(4, 14, [14, 3, 15], "float(E)+float(T)"),
                                0,
                                set(),
                            ),
                            LR0Item(
                                4,
                                Production(5, 14, [14, 4, 15], "float(E)-float(T)"),
                                0,
                                set(),
                            ),
                            LR0Item(5, Production(6, 14, [15], "T"), 0, set()),
                            LR0Item(
                                6,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(
                                7,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(8, Production(9, 15, [16], "St"), 0, set()),
                            LR0Item(
                                9,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                0,
                                set(),
                            ),
                            LR0Item(10, Production(11, 16, [17], "F"), 0, set()),
                            LR0Item(
                                13, Production(14, 17, [8], "memory.recall()"), 0, set()
                            ),
                            LR0Item(12, Production(13, 17, [1, 14, 2], "E"), 0, set()),
                            LR0Item(11, Production(12, 17, [0], "number"), 0, set()),
                        }
                    ),
                    {
                        16: 2,
                        17: 3,
                        1: 4,
                        0: 5,
                        7: 6,
                        8: 7,
                        10: 8,
                        13: 9,
                        14: 10,
                        15: 11,
                    },
                    False,
                ),
                2: LR0State(
                    2,
                    frozenset(
                        {
                            LR0Item(
                                14, Production(9, 15, [16], "St"), 1, {2, 3, 4, 5, 6, 9}
                            )
                        }
                    ),
                    {},
                    False,
                ),
                3: LR0State(
                    3,
                    frozenset(
                        {
                            LR0Item(
                                14, Production(11, 16, [17], "F"), 1, {2, 3, 4, 5, 6, 9}
                            )
                        }
                    ),
                    {},
                    False,
                ),
                4: LR0State(
                    4,
                    frozenset(
                        {
                            LR0Item(
                                1,
                                Production(4, 14, [14, 3, 15], "float(E)+float(T)"),
                                0,
                                set(),
                            ),
                            LR0Item(14, Production(13, 17, [1, 14, 2], "E"), 1, set()),
                            LR0Item(
                                2,
                                Production(5, 14, [14, 4, 15], "float(E)-float(T)"),
                                0,
                                set(),
                            ),
                            LR0Item(3, Production(6, 14, [15], "T"), 0, set()),
                            LR0Item(
                                4,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(
                                5,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(6, Production(9, 15, [16], "St"), 0, set()),
                            LR0Item(
                                7,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                0,
                                set(),
                            ),
                            LR0Item(8, Production(11, 16, [17], "F"), 0, set()),
                            LR0Item(9, Production(12, 17, [0], "number"), 0, set()),
                            LR0Item(
                                11, Production(14, 17, [8], "memory.recall()"), 0, set()
                            ),
                            LR0Item(10, Production(13, 17, [1, 14, 2], "E"), 0, set()),
                        }
                    ),
                    {16: 2, 17: 3, 1: 4, 0: 5, 7: 6, 8: 7, 14: 22, 15: 11},
                    False,
                ),
                5: LR0State(
                    5,
                    frozenset(
                        {
                            LR0Item(
                                14,
                                Production(12, 17, [0], "number"),
                                1,
                                {2, 3, 4, 5, 6, 9},
                            )
                        }
                    ),
                    {},
                    False,
                ),
                6: LR0State(
                    6,
                    frozenset(
                        {
                            LR0Item(1, Production(12, 17, [0], "number"), 0, set()),
                            LR0Item(
                                14,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                1,
                                set(),
                            ),
                            LR0Item(2, Production(13, 17, [1, 14, 2], "E"), 0, set()),
                            LR0Item(
                                3, Production(14, 17, [8], "memory.recall()"), 0, set()
                            ),
                        }
                    ),
                    {0: 5, 17: 21, 8: 7, 1: 4},
                    False,
                ),
                7: LR0State(
                    7,
                    frozenset(
                        {
                            LR0Item(
                                14,
                                Production(14, 17, [8], "memory.recall()"),
                                1,
                                {2, 3, 4, 5, 6, 9},
                            )
                        }
                    ),
                    {},
                    False,
                ),
                8: LR0State(
                    8,
                    frozenset(
                        {LR0Item(14, Production(0, 11, [12, 10], "Prog"), 2, set())}
                    ),
                    {},
                    True,
                ),
                9: LR0State(
                    9,
                    frozenset(
                        {LR0Item(14, Production(1, 12, [12, 13, 9], "None"), 2, set())}
                    ),
                    {9: 20},
                    False,
                ),
                10: LR0State(
                    10,
                    frozenset(
                        {
                            LR0Item(14, Production(3, 13, [14], "print(E)"), 1, {9}),
                            LR0Item(
                                14,
                                Production(4, 14, [14, 3, 15], "float(E)+float(T)"),
                                1,
                                set(),
                            ),
                            LR0Item(
                                14,
                                Production(5, 14, [14, 4, 15], "float(E)-float(T)"),
                                1,
                                set(),
                            ),
                        }
                    ),
                    {3: 16, 4: 17},
                    False,
                ),
                11: LR0State(
                    11,
                    frozenset(
                        {
                            LR0Item(
                                14, Production(6, 14, [15], "T"), 1, {2, 3, 4, 5, 6, 9}
                            ),
                            LR0Item(
                                14,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                1,
                                set(),
                            ),
                            LR0Item(
                                14,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                1,
                                set(),
                            ),
                        }
                    ),
                    {5: 12, 6: 13},
                    False,
                ),
                12: LR0State(
                    12,
                    frozenset(
                        {
                            LR0Item(
                                1,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                0,
                                set(),
                            ),
                            LR0Item(2, Production(11, 16, [17], "F"), 0, set()),
                            LR0Item(
                                3,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                2,
                                set(),
                            ),
                            LR0Item(3, Production(12, 17, [0], "number"), 0, set()),
                            LR0Item(4, Production(13, 17, [1, 14, 2], "E"), 0, set()),
                            LR0Item(
                                5, Production(14, 17, [8], "memory.recall()"), 0, set()
                            ),
                        }
                    ),
                    {16: 15, 17: 3, 0: 5, 1: 4, 8: 7, 7: 6},
                    False,
                ),
                13: LR0State(
                    13,
                    frozenset(
                        {
                            LR0Item(
                                1,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                0,
                                set(),
                            ),
                            LR0Item(2, Production(11, 16, [17], "F"), 0, set()),
                            LR0Item(
                                3,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                2,
                                set(),
                            ),
                            LR0Item(3, Production(12, 17, [0], "number"), 0, set()),
                            LR0Item(4, Production(13, 17, [1, 14, 2], "E"), 0, set()),
                            LR0Item(
                                5, Production(14, 17, [8], "memory.recall()"), 0, set()
                            ),
                        }
                    ),
                    {16: 14, 17: 3, 0: 5, 1: 4, 8: 7, 7: 6},
                    False,
                ),
                14: LR0State(
                    14,
                    frozenset(
                        {
                            LR0Item(
                                6,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                3,
                                {2, 3, 4, 5, 6, 9},
                            )
                        }
                    ),
                    {},
                    False,
                ),
                15: LR0State(
                    15,
                    frozenset(
                        {
                            LR0Item(
                                6,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                3,
                                {2, 3, 4, 5, 6, 9},
                            )
                        }
                    ),
                    {},
                    False,
                ),
                16: LR0State(
                    16,
                    frozenset(
                        {
                            LR0Item(
                                1,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(
                                2,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(
                                3,
                                Production(4, 14, [14, 3, 15], "float(E)+float(T)"),
                                2,
                                set(),
                            ),
                            LR0Item(3, Production(9, 15, [16], "St"), 0, set()),
                            LR0Item(
                                4,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                0,
                                set(),
                            ),
                            LR0Item(5, Production(11, 16, [17], "F"), 0, set()),
                            LR0Item(6, Production(12, 17, [0], "number"), 0, set()),
                            LR0Item(7, Production(13, 17, [1, 14, 2], "E"), 0, set()),
                            LR0Item(
                                8, Production(14, 17, [8], "memory.recall()"), 0, set()
                            ),
                        }
                    ),
                    {16: 2, 17: 3, 1: 4, 0: 5, 7: 6, 8: 7, 15: 19},
                    False,
                ),
                17: LR0State(
                    17,
                    frozenset(
                        {
                            LR0Item(
                                1,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(
                                2,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                0,
                                set(),
                            ),
                            LR0Item(
                                3,
                                Production(5, 14, [14, 4, 15], "float(E)-float(T)"),
                                2,
                                set(),
                            ),
                            LR0Item(3, Production(9, 15, [16], "St"), 0, set()),
                            LR0Item(
                                4,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                0,
                                set(),
                            ),
                            LR0Item(5, Production(11, 16, [17], "F"), 0, set()),
                            LR0Item(6, Production(12, 17, [0], "number"), 0, set()),
                            LR0Item(7, Production(13, 17, [1, 14, 2], "E"), 0, set()),
                            LR0Item(
                                8, Production(14, 17, [8], "memory.recall()"), 0, set()
                            ),
                        }
                    ),
                    {16: 2, 17: 3, 1: 4, 0: 5, 7: 6, 8: 7, 15: 18},
                    False,
                ),
                18: LR0State(
                    18,
                    frozenset(
                        {
                            LR0Item(
                                9,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                1,
                                set(),
                            ),
                            LR0Item(
                                9,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                1,
                                set(),
                            ),
                            LR0Item(
                                9,
                                Production(5, 14, [14, 4, 15], "float(E)-float(T)"),
                                3,
                                {2, 3, 4, 5, 6, 9},
                            ),
                        }
                    ),
                    {5: 12, 6: 13},
                    False,
                ),
                19: LR0State(
                    19,
                    frozenset(
                        {
                            LR0Item(
                                9,
                                Production(7, 15, [15, 5, 16], "float(T)*float(St)"),
                                1,
                                set(),
                            ),
                            LR0Item(
                                9,
                                Production(8, 15, [15, 6, 16], "float(T)/float(St)"),
                                1,
                                set(),
                            ),
                            LR0Item(
                                9,
                                Production(4, 14, [14, 3, 15], "float(E)+float(T)"),
                                3,
                                {2, 3, 4, 5, 6, 9},
                            ),
                        }
                    ),
                    {5: 12, 6: 13},
                    False,
                ),
                20: LR0State(
                    20,
                    frozenset(
                        {
                            LR0Item(
                                1,
                                Production(1, 12, [12, 13, 9], "None"),
                                3,
                                {8, 1, 10, 0, 7},
                            )
                        }
                    ),
                    {},
                    False,
                ),
                21: LR0State(
                    21,
                    frozenset(
                        {
                            LR0Item(
                                4,
                                Production(10, 16, [7, 17], "memory.store(float(F))"),
                                2,
                                {2, 3, 4, 5, 6, 9},
                            )
                        }
                    ),
                    {},
                    False,
                ),
                22: LR0State(
                    22,
                    frozenset(
                        {
                            LR0Item(
                                12,
                                Production(4, 14, [14, 3, 15], "float(E)+float(T)"),
                                1,
                                set(),
                            ),
                            LR0Item(12, Production(13, 17, [1, 14, 2], "E"), 2, set()),
                            LR0Item(
                                12,
                                Production(5, 14, [14, 4, 15], "float(E)-float(T)"),
                                1,
                                set(),
                            ),
                        }
                    ),
                    {2: 23, 3: 16, 4: 17},
                    False,
                ),
                23: LR0State(
                    23,
                    frozenset(
                        {
                            LR0Item(
                                3,
                                Production(13, 17, [1, 14, 2], "E"),
                                3,
                                {2, 3, 4, 5, 6, 9},
                            )
                        }
                    ),
                    {},
                    False,
                ),
            },
            [
                "number",
                "'('",
                "')'",
                "'+'",
                "'-'",
                "'*'",
                "'/'",
                "'S'",
                "'R'",
                "';'",
                "endoffile",
                "Start",
                "Prog",
                "Stmt",
                "E",
                "T",
                "St",
                "F",
            ],
        )

    def eval(self, expression):
        return eval(expression)
