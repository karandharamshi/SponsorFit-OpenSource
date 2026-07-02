from packages.form_filler.safe_fields import is_sensitive_field


def test_sensitive_questions_are_not_safe_to_auto_answer():
    assert is_sensitive_field("Do you require visa sponsorship now or in the future?")
    assert is_sensitive_field("Do you have the right to work in the UK?")
    assert is_sensitive_field("Do you have a disability or need reasonable adjustments?")
    assert is_sensitive_field("Please complete our equality monitoring questions.")
    assert is_sensitive_field("Do you have any criminal convictions?")
    assert is_sensitive_field("Submit application")
