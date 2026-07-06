def solution(today, terms, privacies):
    answer = []

    def to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return y * 12 * 28 + m * 28 + d

    today_days = to_days(today)

    term_dict = {}
    for term in terms:
        kind, month = term.split()
        term_dict[kind] = int(month)
        
    for i, privacy in enumerate(privacies):
        date_str, kind = privacy.split()
        expire_days = to_days(date_str) + (term_dict[kind] * 28)
        
        if expire_days <= today_days:
            answer.append(i + 1)
            
    return answer