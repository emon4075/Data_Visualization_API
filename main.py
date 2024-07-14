def main():
    # Importing Modules

    from dataCollection import data_Collection
    from finalPlotting import final_Plot
    from userPompt import title_Prompt

    try:
        # Title
        title_Prompt()

        # Asking User For Contestant Numbers
        contestant_Number = int(input("\t   How Many People You Want To Compare : ").strip())

        # Collecting Data From Codeforces API
        for _ in range(contestant_Number):
            data_Collection()

        # Prompting The User

        final_Plot()

    except Exception as e:
        print(f"An Error Occurred {e}")


if __name__ == "__main__":
    main()
