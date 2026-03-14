class TextTransformation:
    """Helper class for text transformations."""

    @staticmethod
    def to_camel_case(snake_str: str) -> str:
        """Convert a snake_case string to camelCase."""
        parts = snake_str.split("_")
        return parts[0] + "".join(word.capitalize() for word in parts[1:])
