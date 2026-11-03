from pdfjin_ai_cross_reference.core import cross_reference_documents


def test_import():
    assert callable(cross_reference_documents)
