def add_contest(contest, some_password, contests):
    contests[contest] = some_password
    return contests


def add_user(contest, some_password, name, score, contests, ranking):
    score = int(score)
    if validate_contest(contest, some_password, contests):
        if name not in ranking.keys():
            ranking[name] = {contest: score}
        else:
            if contest in ranking[name].keys():
                if ranking[name][contest] < score:
                    ranking[name][contest] = score
            else:
                ranking[name][contest] = score
    return ranking


def validate_contest(contest, some_password, contests):
    return contest in contests.keys() and some_password == contests[contest]


def find_best_candidate(ranking: dict):
    name, best_score = '', 0

    for user, contest in ranking.items():
        current_total = 0
        for score in contest.values():
            current_total += score
        if current_total > best_score:
            best_score = current_total
            name = user
    return name, best_score


def sort_ranking(ranking):
    sorted_name_score = dict(sorted(ranking.items()))
    for user, contest in sorted_name_score.items():
        sorted_by_score = dict(sorted(contest.items()))
        sorted_name_score[user] = sorted_by_score
    return sorted_name_score


def format_ranking(best_user, max_score, ranking: dict):
    result = f"Best candidate is {best_user} with total {max_score} points.\n"
    result += 'Ranking:\n'
    for user, contest in ranking.items():
        result += f"{user}\n"
        for major, score in contest.items():
            result += f'#  {major} -> {score}\n'
    return result


contest_data = {}
ranking_results = {}

while (line := input()) != 'end of contests':
    contest_name, contest_password = line.split(':')
    contest_data = add_contest(contest_name, contest_password, contest_data)

while (line := input()) != 'end of submissions':
    contest_name, password, username, points = line.split('=>')
    ranking_results = add_user(contest_name, password, username, points, contest_data, ranking_results)

best_candidate, total_points = find_best_candidate(ranking_results)
output = format_ranking(best_candidate, total_points, sort_ranking(ranking_results))
print(output)
