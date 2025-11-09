from difflib import get_close_matches


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6) # can play around with cutoff for how strict the bot will be


    if matches:
        return matches[0]
    

def chat_bot(knowledge: dict):