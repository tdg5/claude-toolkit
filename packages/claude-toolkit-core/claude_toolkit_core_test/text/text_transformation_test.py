from claude_toolkit_core.text.text_transformation import TextTransformation


class TestTextTransformation:
    def test_to_camel_case_single_word(self) -> None:
        assert TextTransformation.to_camel_case("decision") == "decision"

    def test_to_camel_case_two_words(self) -> None:
        assert TextTransformation.to_camel_case("suppress_output") == "suppressOutput"

    def test_to_camel_case_three_words(self) -> None:
        assert TextTransformation.to_camel_case("hook_event_name") == "hookEventName"

    def test_to_camel_case_already_camel(self) -> None:
        assert TextTransformation.to_camel_case("hookEventName") == "hookEventName"

    def test_to_camel_case_empty_string(self) -> None:
        assert TextTransformation.to_camel_case("") == ""
