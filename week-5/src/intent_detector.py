def detect_intent(user_input):

    text = user_input.lower()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "greeting"

    elif any(word in text for word in [
        "course", "courses", "program", "programs",
        "branch", "branches", "degree"
    ]):
        return "courses"

    elif any(word in text for word in [
        "fee", "fees", "tuition", "cost", "charges"
    ]):
        return "fees"

    elif any(word in text for word in [
        "admission", "apply", "application", "eligibility"
    ]):
        return "admission"

    elif any(word in text for word in [
        "exam", "examination", "test"
    ]):
        return "examination"

    elif any(word in text for word in [
        "library", "books"
    ]):
        return "library"

    elif any(word in text for word in [
        "placement", "placements", "job",
        "company", "companies"
    ]):
        return "placement"

    elif any(word in text for word in [
        "faculty", "teacher", "professor"
    ]):
        return "faculty"

    elif any(word in text for word in [
        "hostel", "accommodation", "room"
    ]):
        return "hostel"

    elif any(word in text for word in [
        "campus", "facility", "facilities"
    ]):
        return "campus"

    return "unknown"