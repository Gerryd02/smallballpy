import statsapi


def main():
    hr_lead = statsapi.league_leaders('homeRuns', season=2022, limit=5)
    rbi_lead = statsapi.league_leaders('rbi', season=2022, limit=5)
    print(statsapi.lookup_team("Mets"))


if __name__ == '__main__':
    main()
