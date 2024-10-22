def solution(phone_book):
    answer = True
    phone_book.sort()
    for i, phone in enumerate(phone_book[:-1]):
        target_phone = phone_book[i+1]
        if target_phone[:len(phone)] == phone:
            return False
    return answer
        