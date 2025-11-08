from difflib import get_close_matches


def get_best_match(user_question: str, questions: dict) -> str | None:
    