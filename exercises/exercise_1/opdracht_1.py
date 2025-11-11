def likes(team: list) -> str:
    """
    
    """
    if len(team) == 0:
        return 'No one likes this'
    elif len(team) == 1:
        return f'Only {team[0]} likes this.'
    elif len(team) == 2:
        firstTeamMember = team[0]
        secondTeamMember = team[1]
        return f'{firstTeamMember} and {secondTeamMember} like it!'
    else:
        return 'Doe normaal joh gek.'

