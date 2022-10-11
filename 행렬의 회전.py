from re import X


def solution(rows, columns, queries):
    table = []
    answer = []
    for r in range(rows):
        table.append(a for a in range(r*columns+1,(r+1)*columns+1))

    for query in queries:
        query = [x-1 for x in query]
        tmp = query
    return answer