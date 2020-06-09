import cx_Freeze

executables=[cx_Freeze.Executable("TicTacToe.py",
                                  base="Win32GUI",
                                  icon="icon2.ico")]

cx_Freeze.setup(
    name="Tic Tac Toe",
    author="Bharath Gowda",
    options={"build_exe":{"packages":["pygame","random"],
                          "include_files":["icon.png","x.png","o.png","board.png","freesansbold.ttf"]}},executables=executables
    )
