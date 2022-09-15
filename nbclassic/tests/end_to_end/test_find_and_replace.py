"""Test Jupyter find/replace"""


INITIAL_CELLS = ["hello", "hellohello", "abc", "ello"]


def test_find_and_replace(notebook_frontend):
    """ test find and replace on all the cells """
    notebook_frontend.populate(INITIAL_CELLS)

    find_str = "ello"
    replace_str = "foo"

    # replace the strings
    notebook_frontend.find_and_replace(index=0, find_txt=find_str, replace_txt=replace_str)

    # check content of the cells
    assert notebook_frontend.get_cells_contents() == [
        s.replace(find_str, replace_str) for s in INITIAL_CELLS
    ]
