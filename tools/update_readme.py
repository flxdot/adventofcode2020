from tools.setup_repo import write_readme_file

if __name__ == "__main__":
    for year in range(2020, 2021):
        for day in range(1, 9):
            print(f"{year}/{day}")
            write_readme_file(year, day)
